from playwright.sync_api import expect

def test_home_to_docs_navigation(home, docs):
    home.click_get_started()
    expect(home.page).to_have_url("https://playwright.dev/docs/intro")

    title = docs.get_title_text()
    assert "Playwright" in title