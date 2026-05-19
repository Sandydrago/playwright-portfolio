from dataclasses import dataclass
from typing import Optional

category: Optional[Category]


@dataclass
class Category:
    id: int
    name: str

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

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

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

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

    def to_dict(self):
        return {
            "id": self.id,
            "category": self.category.to_dict() if self.category else None,
            "name": self.name,
            "photoUrls": self.photoUrls,
            "tags": [tag.to_dict() for tag in self.tags] if self.tags else [],
            "status": self.status
        }
    
    @staticmethod
    def from_json(data: Dict[str, Any]) -> "Pet":
         return Pet(
            id=data.get("id"),
            name=data.get("name", ""),
            category=Category.from_json(data["category"]) if data.get("category") else None,
            photoUrls=data.get("photoUrls", []),
            tags=[Tag.from_json(tag) for tag in data.get("tags", [])],
            status=data.get("status", "available")
    )

