import requests
# test this was GIT and I'm an idiot
class BaseAPI:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/") + "/"

    def get(self, endpoint, **kwargs):
        return requests.get(f"{self.base_url}{endpoint}", **kwargs)

    def post(self, endpoint, json=None, **kwargs):
        return requests.post(f"{self.base_url}{endpoint}", json=json, **kwargs)

    def put(self, endpoint, json=None, **kwargs):
        return requests.put(f"{self.base_url}{endpoint}", json=json, **kwargs)

    def delete(self, endpoint, **kwargs):
        return requests.delete(f"{self.base_url}{endpoint}", **kwargs)