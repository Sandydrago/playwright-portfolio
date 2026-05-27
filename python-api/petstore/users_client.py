from .base_client import PetstoreBaseClient

class UsersClient(PetstoreBaseClient):

    def get_user(self, username):
        return self._get(f"/user/{username}")

    def create_user(self, user_payload):
        return self._post("/user", json=user_payload)
