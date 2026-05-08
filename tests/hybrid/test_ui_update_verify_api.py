import pytest
from helpers.api.petstore_user_api import PetstoreUserAPI

@pytest.mark.asyncio
async def test_ui_update_verify_api(auth_context, request_context):
    base_url = "https://petstore.swagger.io/v2"
    user_api = PetstoreUserAPI(request_context, base_url)

    # 1. Create user via API
    payload = {
        "id": 98765,
        "username": "sandra_ui_test",
        "firstName": "Sandra",
        "lastName": "UIUpdate",
        "email": "sandra@example.com",
        "password": "Password123!",
        "phone": "555-555-5555",
        "userStatus": 1
    }

    create_response = await user_api.create_user(payload)
    assert create_response.ok

    # 2. Login via API
    login_response = await user_api.login(payload["username"], payload["password"])
    assert login_response.ok

    # 3. Open UI authenticated
    page = await auth_context.new_page()
    await page.goto("https://www.saucedemo.com")

    # 4. Simulate a UI update (e.g., user changes their last name)
    new_last_name = "UpdatedFromUI"
    await page.evaluate(f"document.body.innerHTML = '<h1>{new_last_name}</h1>'")

    # 5. Update user via API to reflect UI change
    payload["lastName"] = new_last_name
    update_response = await user_api.update_user(payload["username"], payload)
    assert update_response.ok

    # 6. Verify via API
    get_response = await user_api.get_user(payload["username"])
    user_data = await get_response.json()

    assert user_data["lastName"] == new_last_name
