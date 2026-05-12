from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class Order:
    id: int
    petId: int
    quantity: int
    shipDate: str
    status: str  # placed | approved | delivered
    complete: bool

    @staticmethod
    def from_json(data: Dict[str, Any]) -> "Order":
        return Order(
            id=data["id"],
            petId=data["petId"],
            quantity=data["quantity"],
            shipDate=data["shipDate"],
            status=data["status"],
            complete=data["complete"]
        )
