import pytest_asyncio
from playwright.async_api import async_playwright
from helpers.api.petstore_user_api import PetstoreUserAPI

@pytest_asyncio.fixture
async def auth_context():
    playwright = await async_playwright().start()

    # 1. Create API request context
    request_context = await playwright.request.new_context(base_url="https://petstore.swagger.io/v2")

    # 2. Login via API
    api = PetstoreUserAPI(request_context, "https://petstore.swagger.io/v2")
    await api.login("standard_user", "secret_sauce")

    # 3. Create browser context
    browser = await playwright.chromium.launch()
    context = await browser.new_context()

    # Give the context to the test
    yield context

    # Cleanup AFTER the test
    await context.close()
    await browser.close()
    await playwright.stop()
