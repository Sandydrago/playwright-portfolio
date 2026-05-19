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

    def to_dict(self):
        return {
          "id": self.id,
          "petId": self.petId,
           "quantity": self.quantity,
           "shipDate": self.shipDate,
           "status": self.status,
          "complete": self.complete
        }

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
