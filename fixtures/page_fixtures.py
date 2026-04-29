import pytest
from pages.home_page import HomePage
from pages.docs_page import DocsPage

@pytest.fixture
def home(page, config):
    page.goto(config.BASE_URL)
    return HomePage(page)


@pytest.fixture
def docs(page):
    return DocsPage(page)
