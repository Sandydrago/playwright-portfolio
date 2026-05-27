from .base_client import PetstoreBaseClient

class OrdersClient(PetstoreBaseClient):

    def get_order(self, order_id):
        return self._get(f"/store/order/{order_id}")

    def place_order(self, order_payload):
        return self._post("/store/order", json=order_payload)

    def delete_order(self, order_id):
        return self._delete(f"/store/order/{order_id}")
