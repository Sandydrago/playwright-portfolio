import os
import pytest
from pages.home_page import HomePage
from pages.docs_page import DocsPage
from datetime import datetime

@pytest.fixture
def home(page):
    home_page = HomePage(page)
    home_page.navigate()
    return home_page


@pytest.fixture
def docs(page):
    return DocsPage(page)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Run all other hooks to get the report object
    outcome = yield
    report = outcome.get_result()

    # We only care about actual test failures
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page", None)
        if page:
            os.makedirs("screenshots", exist_ok=True)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            test_name = item.name.replace("/", "_").replace("\\", "_")

            filename = f"screenshots/{test_name}_{timestamp}.png"
            page.screenshot(path=filename)

            print(f"\n❌ Screenshot saved: {filename}")