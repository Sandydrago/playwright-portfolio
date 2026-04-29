import pytest
from testdata.loader import load_json

@pytest.fixture(scope="session")
def users():
    return load_json("users.json")

@pytest.fixture(scope="session")
def payloads():
    return load_json("payloads.json")
