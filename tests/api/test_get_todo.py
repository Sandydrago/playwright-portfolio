def test_get_todo_returns_200(todos_api):
    response = todos_api.get_todo(1)

    assert response.status_code == 200
    data = response.json()

    assert data["id"] == 1
    assert "title" in data
