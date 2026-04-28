import pytest
from pages.home_page import HomePage
from pages.docs_page import DocsPage

@pytest.fixture
def home(page):
    home_page = HomePage(page)
    home_page.navigate()
    return home_page

@pytest.fixture
def docs(page):
    return DocsPage(page)
