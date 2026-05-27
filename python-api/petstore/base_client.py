import requests

class PetstoreBaseClient:
    BASE_URL = "https://petstore.swagger.io/v2"

    def _get(self, endpoint, **kwargs):
        return requests.get(f"{self.BASE_URL}{endpoint}", **kwargs)

    def _post(self, endpoint, json=None, **kwargs):
        return requests.post(f"{self.BASE_URL}{endpoint}", json=json, **kwargs)

    def _delete(self, endpoint, **kwargs):
        return requests.delete(f"{self.BASE_URL}{endpoint}", **kwargs)
