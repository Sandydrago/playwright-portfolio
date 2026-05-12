class ApiError(Exception):
    """Base class for all API-related errors."""
    pass


class NotFoundError(ApiError):
    """Raised when the API returns a 404 Not Found."""
    pass


class ValidationError(ApiError):
    """Raised when the API returns a 400 Bad Request or invalid data."""
    pass


class UnauthorizedError(ApiError):
    """Raised when the API returns a 401 Unauthorized."""
    pass


class ForbiddenError(ApiError):
    """Raised when the API returns a 403 Forbidden."""
    pass


class ConflictError(ApiError):
    """Raised when the API returns a 409 Conflict."""
    pass


class ServerError(ApiError):
    """Raised when the API returns a 5xx server error."""
    pass
