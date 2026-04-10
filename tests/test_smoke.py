from playwright.sync_api import Page
import os

def test_screenshot_per_browser(page: Page, browser_name: str):
    os.makedirs("screenshots", exist_ok=True)

    page.goto("https://playwright.dev/")

    filename = f"screenshots/{browser_name}.png"
    page.screenshot(path=filename)

    print(f"Saved → {filename}")