class BaseAPI:
    def __init__(self, request_context, base_url: str):
        self.request = request_context
        self.base_url = base_url.rstrip("/") + "/"
# test
    async def get(self, endpoint, **kwargs):
        return await self.request.get(f"{self.base_url}{endpoint}", **kwargs)

    async def post(self, endpoint, data=None, **kwargs):
        return await self.request.post(
            f"{self.base_url}{endpoint}",
            data=data,
            **kwargs
        )

    async def put(self, endpoint, data=None, **kwargs):
        return await self.request.put(
            f"{self.base_url}{endpoint}",
            data=data,
            **kwargs
        )

    async def delete(self, endpoint, **kwargs):
        return await self.request.delete(f"{self.base_url}{endpoint}", **kwargs)