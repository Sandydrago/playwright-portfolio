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

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "email": self.email,
            "password": self.password,
            "phone": self.phone,
            "userStatus": self.userStatus
        }

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
