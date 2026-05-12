from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class User:
    id: int
    username: str
    firstName: str
    lastName: str
    email: str
    password: str
    phone: str
    userStatus: int

    @staticmethod
    def from_json(data: Dict[str, Any]) -> "User":
        return User(
            id=data["id"],
            username=data["username"],
            firstName=data["firstName"],
            lastName=data["lastName"],
            email=data["email"],
            password=data["password"],
            phone=data["phone"],
            userStatus=data["userStatus"]
        )
