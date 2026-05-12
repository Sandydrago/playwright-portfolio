import pytest
from testdata.loader import load_json

@pytest.fixture(scope="session")
def user_data():
    return load_json("users.json")

@pytest.fixture(scope="session")
def payloads_data():
    return load_json("payloads.json")
