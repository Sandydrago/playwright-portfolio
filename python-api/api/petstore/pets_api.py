from typing import List
from .base_api import BaseAPI
from .models.pet import Pet


class PetsAPI(BaseAPI):
    """
    Client for Petstore /pet endpoints.
    """

    # -----------------------------
    # Create a new pet
    # -----------------------------
    def add_pet(self, pet: Pet) -> Pet:
        data = self._request(
            method="POST",
            endpoint="/pet",
            expected_status=200,
            json_body=pet.__dict__,
        )
        return Pet.from_json(data)

    # -----------------------------
    # Get pet by ID
    # -----------------------------
    def get_pet(self, pet_id: int) -> Pet:
        data = self._request(
            method="GET",
            endpoint=f"/pet/{pet_id}",
            expected_status=200,
        )
        return Pet.from_json(data)

    # -----------------------------
    # Update an existing pet
    # -----------------------------
    def update_pet(self, pet: Pet) -> Pet:
        data = self._request(
            method="PUT",
            endpoint="/pet",
            expected_status=200,
            json_body=pet.__dict__,
        )
        return Pet.from_json(data)

    # -----------------------------
    # Delete a pet
    # -----------------------------
    def delete_pet(self, pet_id: int) -> None:
        self._request(
            method="DELETE",
            endpoint=f"/pet/{pet_id}",
            expected_status=200,
        )

    # -----------------------------
    # Find pets by status
    # -----------------------------
    def find_by_status(self, status: str) -> List[Pet]:
        data = self._request(
            method="GET",
            endpoint=f"/pet/findByStatus?status={status}",
            expected_status=200,
        )
        return [Pet.from_json(item) for item in data]
