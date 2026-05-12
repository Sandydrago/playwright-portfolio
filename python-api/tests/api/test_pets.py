import pytest
from api.petstore.pets_api import PetsAPI
from api.petstore.models.pet import Pet, Category, Tag
from api.petstore.exceptions import NotFoundError, ValidationError


@pytest.fixture
def base_url():
    return "https://petstore.swagger.io/v2"


@pytest.fixture
def pets_api(base_url):
    return PetsAPI(base_url)


@pytest.fixture
def sample_pet():
    return Pet(
        id=999999,
        name="TestDog",
        category=Category(id=1, name="Dogs"),
        photoUrls=["http://example.com/dog.jpg"],
        tags=[Tag(id=1, name="friendly")],
        status="available",
    )


# -----------------------------
# Positive tests
# -----------------------------
def test_add_pet(pets_api, sample_pet):
    created = pets_api.add_pet(sample_pet)
    assert created.id == sample_pet.id
    assert created.name == "TestDog"


def test_get_pet(pets_api, sample_pet):
    pets_api.add_pet(sample_pet)
    pet = pets_api.get_pet(sample_pet.id)
    assert pet.id == sample_pet.id
    assert pet.name == sample_pet.name


def test_update_pet(pets_api, sample_pet):
    pets_api.add_pet(sample_pet)
    sample_pet.name = "UpdatedDog"
    updated = pets_api.update_pet(sample_pet)
    assert updated.name == "UpdatedDog"


def test_find_by_status(pets_api):
    pets = pets_api.find_by_status("available")
    assert isinstance(pets, list)
    if pets:
        assert isinstance(pets[0], Pet)


# -----------------------------
# Negative tests
# -----------------------------
def test_get_pet_not_found(pets_api):
    with pytest.raises(NotFoundError):
        pets_api.get_pet(123456789)


def test_add_pet_invalid_data(pets_api):
    bad_pet = {
        "id": "not-an-int",
        "name": 123,
    }
    with pytest.raises(ValidationError):
        pets_api._request(
            method="POST",
            endpoint="/pet",
            expected_status=200,
            json_body=bad_pet,
        )
