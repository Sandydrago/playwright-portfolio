from playwright.sync_api import Page
from pages.base_page import BasePage
from pages.components.nav_bar import NavBar

class DocsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.nav = NavBar(page)
        self.title_header = page.get_by_role("heading", level=1)

    def get_title_text(self):
        self.log_step("Reading Docs page title")
        self.wait_for_page_ready()
        return self.title_header.inner_text()

    def assert_title_contains(self, text: str):
        self.log_step(f"Asserting Docs page title contains '{text}'")
        self.assert_text(self.title_header, text)

