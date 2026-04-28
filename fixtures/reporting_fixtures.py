import os
from datetime import datetime
import pytest

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page", None)
        if page:
            os.makedirs("screenshots", exist_ok=True)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            test_name = item.name.replace("/", "_").replace("\\", "_")

            filename = f"screenshots/{test_name}_{timestamp}.png"
            page.screenshot(path=filename)

            print(f"\n❌ Screenshot saved: {filename}")
