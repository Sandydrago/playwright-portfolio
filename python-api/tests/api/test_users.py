import pytest
from api.petstore.users_api import UsersAPI
from api.petstore.models.user import User
from api.petstore.exceptions import NotFoundError, UnauthorizedError


@pytest.fixture
def base_url():
    return "https://petstore.swagger.io/v2"


@pytest.fixture
def users_api(base_url):
    return UsersAPI(base_url)


@pytest.fixture
def sample_user():
    return User(
        id=888888,
        username="testuser123",
        firstName="Test",
        lastName="User",
        email="testuser@example.com",
        password="password123",
        phone="123-456-7890",
        userStatus=1,
    )


# -----------------------------
# Positive tests
# -----------------------------
def test_create_user(users_api, sample_user):
    created = users_api.create_user(sample_user)
    assert created.username == sample_user.username
    assert created.email == sample_user.email