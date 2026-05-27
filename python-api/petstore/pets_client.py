from .base_client import PetstoreBaseClient

class PetsClient(PetstoreBaseClient):

    def get_pet(self, pet_id):
        return self._get(f"/pet/{pet_id}")

    def add_pet(self, pet_payload):
        return self._post("/pet", json=pet_payload)

    def delete_pet(self, pet_id):
        return self._delete(f"/pet/{pet_id}")

    def find_by_status(self, status):
        return self._get(f"/pet/findByStatus?status={status}")

