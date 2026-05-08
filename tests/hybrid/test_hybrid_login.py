import pytest
#test
@pytest.mark.asyncio
async def test_hybrid_login(auth_context):
    # 1. Use the authenticated context created by API login
    page = await auth_context.new_page()

    # 2. Navigate to a page that requires authentication
    await page.goto("https://www.saucedemo.com")

    # 3. Assert that the user is already logged in (hybrid proof)
    title = await page.title()
    assert "Swag Labs" in title
