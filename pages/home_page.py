from playwright.sync_api import Page
from pages.base_page import BasePage
from pages.components.nav_bar import NavBar

class HomePage(BasePage):
    URL = "https://playwright.dev/"

    def __init__(self, page: Page):
        super().__init__(page)
        self.nav = NavBar(page)

    def navigate(self):
        self.log_step("Navigating to Playwright homepage")
        super().navigate(self.URL)
        self.wait_for_page_ready()

