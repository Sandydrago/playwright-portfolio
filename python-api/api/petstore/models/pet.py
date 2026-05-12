from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass
class Category:
    id: int
    name: str

    @staticmethod
    def from_json(data: Dict[str, Any]) -> "Category":
        return Category(
            id=data["id"],
            name=data["name"]
        )


@dataclass
class Tag:
    id: int
    name: str

    @staticmethod
    def from_json(data: Dict[str, Any]) -> "Tag":
        return Tag(
            id=data["id"],
            name=data["name"]
        )


@dataclass
class Pet:
    id: int
    name: str
    category: Category
    photoUrls: List[str]
    tags: List[Tag]
    status: str  # available | pending | sold

    @staticmethod
    def from_json(data: Dict[str, Any]) -> "Pet":
        return Pet(
            id=data["id"],
            name=data["name"],
            category=Category.from_json(data["category"]),
            photoUrls=data["photoUrls"],
            tags=[Tag.from_json(tag) for tag in data.get("tags", [])],
            status=data["status"]
        )
