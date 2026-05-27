import pytest
from petstore.pets_client import PetsClient

@pytest.fixture
def pets_api():
    return PetsClient()

@pytest.fixture
def sample_pet():
    return {
        "id": 999999,
        "name": "TestDog",
        "category": {"id": 1, "name": "Dogs"},
        "photoUrls": ["http://example.com/dog.jpg"],
        "tags": [{"id": 1, "name": "friendly"}],
        "status": "available"
    }

# -----------------------------
# Positive tests
# -----------------------------
def test_add_pet(pets_api, sample_pet):
    response = pets_api.add_pet(sample_pet)
    assert response.status_code == 200
    assert response.json()["id"] == sample_pet["id"]

def test_get_pet(pets_api, sample_pet):
    pets_api.add_pet(sample_pet)
    response = pets_api.get_pet(sample_pet["id"])
    assert response.status_code == 200
    assert response.json()["name"] == sample_pet["name"]

def test_update_pet(pets_api, sample_pet):
    pets_api.add_pet(sample_pet)
    sample_pet["name"] = "UpdatedDog"
    response = pets_api.add_pet(sample_pet)
    assert response.status_code == 200
    assert response.json()["name"] == "UpdatedDog"

def test_find_by_status(pets_api):
    response = pets_api.find_by_status("available")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# -----------------------------
# Negative tests
# -----------------------------
def test_get_pet_not_found(pets_api):
    response = pets_api.get_pet(123456789)
    assert response.status_code == 404

def test_add_pet_invalid_data(pets_api):
    bad_pet = {"id": "not-an-int", "name": 123}
    response = pets_api.add_pet(bad_pet)
    assert response.status_code in [400, 500]
