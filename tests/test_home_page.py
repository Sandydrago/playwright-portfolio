import re
from playwright.sync_api import expect

def test_home_page_title(home):
    print(home.page.title())
    expect(home.page).to_have_title(re.compile("Playwright"))