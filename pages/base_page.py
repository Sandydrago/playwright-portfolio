from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    # -----------------------------
    # Navigation
    # -----------------------------
    def navigate(self, url: str):
        self.page.goto(url)

    def wait_for_url_contains(self, text: str, timeout: int = 5000):
        expect(self.page).to_have_url(lambda url: text in url, timeout=timeout)

    # -----------------------------
    # Assertions
    # -----------------------------
    def assert_text(self, locator, expected: str):
        expect(locator).to_have_text(expected)

    def assert_visible(self, locator):
        expect(locator).to_be_visible()

    # -----------------------------
    # Interaction helpers
    # -----------------------------
    def safe_click(self, locator):
        locator.wait_for(state="visible")
        locator.click()

    def click_and_wait_for_navigation(self, locator):
        with self.page.expect_navigation():
            locator.click()

    # -----------------------------
    # Page readiness
    # -----------------------------
    def wait_for_page_ready(self):
        self.page.wait_for_load_state("domcontentloaded")

    # -----------------------------
    # Artifacts
    # -----------------------------
    def screenshot(self, name: str):
        self.page.screenshot(path=f"screenshots/{name}.png")

    # -----------------------------
    # Logging
    # -----------------------------
    def log_step(self, message: str):
        print(f"\n➡️  {message}")
