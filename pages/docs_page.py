from playwright.sync_api import Page
from pages.base_page import BasePage

class DocsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.title_header = page.locator("h1")

    def get_title_text(self):
        return self.title_header.inner_text()