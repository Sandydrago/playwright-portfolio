import pytest
from api.petstore.store_api import StoreAPI
from api.petstore.models.order import Order
from api.petstore.exceptions import NotFoundError


@pytest.fixture
def base_url():
    return "https://petstore.swagger.io/v2"


@pytest.fixture
def store_api(base_url):
    return StoreAPI(base_url)


@pytest.fixture
def sample_order():
    return Order(
        id=777777,
        petId=999999,
        quantity=1,
        shipDate="2025-01-01T00:00:00.000Z",
        status="placed",
        complete=True,
    )


# -----------------------------
# Positive tests
# -----------------------------
def test_place_order(store_api, sample_order):
    created = store_api.place_order(sample_order)
    assert created.id == sample_order.id
    assert created.petId == sample_order.petId


def test_get_order(store_api, sample_order):
    store_api.place_order(sample_order)
    order = store_api.get_order(sample_order.id)
    assert order.id == sample_order.id
    assert order.status == "placed"


def test_delete_order(store_api, sample_order):
    store_api.place_order(sample_order)
    store_api.delete_order(sample_order.id)
    with pytest.raises(NotFoundError):
        store_api.get_order(sample_order.id)


def test_get_inventory(store_api):
    inventory = store_api.get_inventory()
    assert isinstance(inventory, dict)


# -----------------------------
# Negative tests
# -----------------------------
def test_get_order_not_found(store_api):
    with pytest.raises(NotFoundError):
        store_api.get_order(123456789)
