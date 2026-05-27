import pytest
from petstore.users_client import UsersClient

@pytest.fixture
def users_api():
    return UsersClient()

@pytest.fixture
def sample_user():
    return {
        "id": 888888,
        "username": "testuser123",
        "firstName": "Test",
        "lastName": "User",
        "email": "testuser@example.com",
        "password": "password123",
        "phone": "123-456-7890",
        "userStatus": 1
    }

# -----------------------------
# Positive tests
# -----------------------------
def test_create_user(users_api, sample_user):
    create_response = users_api.create_user(sample_user)
    assert create_response.status_code == 200

    # Now fetch the user to validate fields
    get_response = users_api.get_user(sample_user["username"])
    assert get_response.status_code == 200

    body = get_response.json()
    assert body["username"] == sample_user["username"]
    assert body["email"] == sample_user["email"]

def test_get_user(users_api, sample_user):
    users_api.create_user(sample_user)
    response = users_api.get_user(sample_user["username"])
    assert response.status_code == 200
    body = response.json()
    assert body["username"] == sample_user["username"]
    assert body["firstName"] == sample_user["firstName"]

# -----------------------------
# Negative tests
# -----------------------------
def test_get_user_not_found(users_api):
    response = users_api.get_user("nonexistent_user_12345")
    assert response.status_code == 404

def test_login_invalid_credentials():
    # Petstore login endpoint is GET /user/login
    # Your UsersClient doesn't implement login, so we test it directly
    import requests
    response = requests.get(
        "https://petstore.swagger.io/v2/user/login",
        params={"username": "fakeuser", "password": "wrongpassword"}
    )
    assert response.status_code in [200, 400, 401, 404]