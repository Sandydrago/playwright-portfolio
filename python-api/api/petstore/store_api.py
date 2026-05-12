from .base_api import BaseAPI
from .models.order import Order


class StoreAPI(BaseAPI):
    """
    Client for Petstore /store endpoints.
    """

    # -----------------------------
    # Place an order for a pet
    # -----------------------------
    def place_order(self, order: Order) -> Order:
        data = self._request(
            method="POST",
            endpoint="/store/order",
            expected_status=200,
            json_body=order.__dict__,
        )
        return Order.from_json(data)

    # -----------------------------
    # Get order by ID
    # -----------------------------
    def get_order(self, order_id: int) -> Order:
        data = self._request(
            method="GET",
            endpoint=f"/store/order/{order_id}",
            expected_status=200,
        )
        return Order.from_json(data)

    # -----------------------------
    # Delete order
    # -----------------------------
    def delete_order(self, order_id: int) -> None:
        self._request(
            method="DELETE",
            endpoint=f"/store/order/{order_id}",
            expected_status=200,
        )

    # -----------------------------
    # Get inventory
    # -----------------------------
    def get_inventory(self) -> dict:
        return self._request(
            method="GET",
            endpoint="/store/inventory",
            expected_status=200,
        )
