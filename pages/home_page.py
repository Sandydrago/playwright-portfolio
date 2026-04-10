from playwright.sync_api import Page
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.get_started_button = page.locator("text=Get Started")

    def navigate(self):
        super().navigate("https://playwright.dev/")

    def click_get_started(self):
        self.get_started_button.click()