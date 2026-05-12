import json
import logging
import requests
from typing import Any, Dict, Optional

from .exceptions import (
    ApiError,
    NotFoundError,
    ValidationError,
    UnauthorizedError,
    ForbiddenError,
    ConflictError,
    ServerError,
)


class BaseAPI:
    """
    Base class for all Petstore API clients.
    Handles:
    - HTTP requests
    - Logging
    - Error handling
    - JSON parsing
    """

    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

        # Configure logging
        self.logger = logging.getLogger(self.__class__.__name__)
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
            self.logger.setLevel(logging.INFO)

    # -----------------------------
    # Core request method
    # -----------------------------
    def _request(
        self,
        method: str,
        endpoint: str,
        expected_status: int,
        json_body: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:

        url = f"{self.base_url}{endpoint}"

        # Log request
        self.logger.info(f"REQUEST: {method} {url}")
        if json_body:
            self.logger.info(f"REQUEST BODY: {json.dumps(json_body, indent=2)}")

        response = self.session.request(method, url, json=json_body)

        # Log response
        self.logger.info(f"RESPONSE STATUS: {response.status_code}")
        try:
            self.logger.info(f"RESPONSE BODY: {json.dumps(response.json(), indent=2)}")
        except Exception:
            self.logger.info("RESPONSE BODY: <non-JSON response>")

        # Validate status code
        if response.status_code != expected_status:
            self._handle_error(response)

        # Parse JSON
        try:
            return response.json()
        except Exception:
            raise ApiError("Response did not contain valid JSON")

    # -----------------------------
    # Error handling
    # -----------------------------
    def _handle_error(self, response: requests.Response):
        status = response.status_code

        if status == 400:
            raise ValidationError(response.text)
        if status == 401:
            raise UnauthorizedError(response.text)
        if status == 403:
            raise ForbiddenError(response.text)
        if status == 404:
            raise NotFoundError(response.text)
        if status == 409:
            raise ConflictError(response.text)
        if 500 <= status <= 599:
            raise ServerError(response.text)

        raise ApiError(f"Unexpected status code {status}: {response.text}")
