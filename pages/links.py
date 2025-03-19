from playwright.sync_api import Page, expect
from pages.base_class import *


class Links(BaseClass):
    def __init__(self, page: Page):
        super().__init__(page)

    def assert_url(self, link):
        self.page.wait_for_selector('[alt="Imot.io loader"]', state="hidden")
        expect(self.page).to_have_url(link)