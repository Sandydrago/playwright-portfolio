from playwright.sync_api import Page
from pages.base_page import BasePage

class NavBar(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.menu_button = page.get_by_role("button", name="Toggle navigation")
        self.get_started = page.get_by_role("link", name="Get Started")
        self.docs = page.get_by_role("link", name="Docs")

    def ensure_menu_open(self):
        if self.menu_button.is_visible():
            self.menu_button.click()

    def click_get_started(self):
        self.log_step("Clicking 'Get Started' in NavBar")
        self.ensure_menu_open()
        self.safe_click(self.get_started)

    def click_docs(self):
        self.log_step("Clicking 'Docs' in NavBar")
        self.ensure_menu_open()
        self.safe_click(self.docs)
