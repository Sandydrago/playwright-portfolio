import pytest
from petstore.orders_client import OrdersClient

@pytest.fixture
def store_api():
    return OrdersClient()

@pytest.fixture
def sample_order():
    return {
        "id": 777777,
        "petId": 999999,
        "quantity": 1,
        "shipDate": "2025-01-01T00:00:00.000Z",
        "status": "placed",
        "complete": True
    }

# -----------------------------
# Positive tests
# -----------------------------
def test_place_order(store_api, sample_order):
    response = store_api.place_order(sample_order)
    assert response.status_code == 200
    body = response.json()
    assert body["id"] == sample_order["id"]
    assert body["petId"] == sample_order["petId"]

def test_get_order(store_api, sample_order):
    store_api.place_order(sample_order)
    response = store_api.get_order(sample_order["id"])
    assert response.status_code == 200
    body = response.json()
    assert body["id"] == sample_order["id"]
    assert body["status"] == "placed"

def test_delete_order(store_api, sample_order):
    store_api.place_order(sample_order)
    delete_response = store_api.delete_order(sample_order["id"])
    assert delete_response.status_code in [200, 204]

    # After deletion, Petstore returns 404
    get_response = store_api.get_order(sample_order["id"])
    assert get_response.status_code == 404

def test_get_inventory(store_api):
    response = store_api._get("/store/inventory")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

# -----------------------------
# Negative tests
# -----------------------------
def test_get_order_not_found(store_api):
    response = store_api.get_order(123456789)
    assert response.status_code == 404
