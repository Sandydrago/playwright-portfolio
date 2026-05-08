# Root conftest.py test I'm an idiot
# This file simply imports fixture modules so pytest auto-discovers them.
import pytest
from api.todos_api import TodosAPI
from config.config_loader import get_config
from fixtures.page_fixtures import *
from fixtures.reporting_fixtures import *

from config.config_loader import get_config
@pytest.fixture(scope="session")
def config():
    return get_config()

@pytest.fixture
def todos_api():
    return TodosAPI("https://jsonplaceholder.typicode.com")

pytest_plugins = [
    "fixtures.auth_context"
]

pytest_plugins = [
    "fixtures.auth_context",
    "fixtures.request_context"
]
