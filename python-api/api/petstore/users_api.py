from .base_api import BaseAPI
from .models.user import User


class UsersAPI(BaseAPI):
    """
    Client for Petstore /user endpoints.
    """

    # -----------------------------
    # Create a new user
    # -----------------------------
    def create_user(self, user: User) -> User:
        data = self._request(
            method="POST",
            endpoint="/user",
            expected_status=200,
            json_body=user.__dict__,
        )
        return User.from_json(data)

    # -----------------------------
    # Get user by username
    # -----------------------------
    def get_user(self, username: str) -> User:
        data = self._request(
            method="GET",
            endpoint=f"/user/{username}",
            expected_status=200,
        )
        return User.from_json(data)

    # -----------------------------
    # Login user
    # -----------------------------
    def login(self, username: str, password: str) -> str:
        data = self._request(
            method="GET",
            endpoint=f"/user/login?username={username}&password={password}",
            expected_status=200,
        )
        return data.get("message", "")

    # -----------------------------
    # Logout user
    # -----------------------------
    def logout(self) -> None:
        self._request(
            method="GET",
            endpoint="/user/logout",
            expected_status=200,
        )
