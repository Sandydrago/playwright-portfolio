import pytest_asyncio
from playwright.async_api import async_playwright

@pytest_asyncio.fixture
async def request_context():
    async with async_playwright() as p:
        context = await p.request.new_context(base_url="https://petstore.swagger.io/v2")
        yield context
        await context.dispose()
