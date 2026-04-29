from api.base_api import BaseAPI

class TodosAPI(BaseAPI):
    def __init__(self, base_url: str):
        super().__init__(base_url)
        self.endpoint = "todos"

    def get_todo(self, todo_id: int):
        return self.get(f"{self.endpoint}/{todo_id}")

    def create_todo(self, payload: dict):
        return self.post(self.endpoint, json=payload)

    def update_todo(self, todo_id: int, payload: dict):
        return self.patch(f"{self.endpoint}/{todo_id}", json=payload)

    def delete_todo(self, todo_id: int):
        return self.delete(f"{self.endpoint}/{todo_id}")
