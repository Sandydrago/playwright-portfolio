from helpers.api.base_api import BaseAPI
from helpers.api.endpoints import USER_ENDPOINT

class PetstoreUserAPI(BaseAPI):
    def __init__(self, request_context, base_url: str):
        super().__init__(request_context, base_url)
        self.endpoint = USER_ENDPOINT

    async def create_user(self, payload: dict):
        return await self.post(self.endpoint, data=payload)

    async def get_user(self, username: str):
        return await self.get(f"{self.endpoint}/{username}")

    async def update_user(self, username: str, payload: dict):
        return await self.put(f"{self.endpoint}/{username}", data=payload)

    async def delete_user(self, username: str):
        return await self.delete(f"{self.endpoint}/{username}")

    async def login(self, username: str, password: str):
        return await self.get(f"{self.endpoint}/login?username={username}&password={password}")

