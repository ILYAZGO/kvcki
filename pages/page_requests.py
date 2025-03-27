#from playwright.sync_api import Page, expect
from pages.base_class import *

BUTTON_DICTS = '[data-testid="markup_nav_dicts"]'
BUTTON_ADD_DICT = '[data-testid="markup_addDict"]'
BUTTON_CHECK_LIST = '[data-testid="markup_nav_checklists"]'
BUTTON_GPT = '[data-testid="markup_nav_gpt"]'


class PageRequests(BaseClass):
    def __init__(self, page: Page):
        super().__init__(page)
        self.button_gpt = page.locator(BUTTON_GPT)
        self.button_dicts = page.locator(BUTTON_DICTS)
        self.button_check_list = page.locator(BUTTON_CHECK_LIST)


    def click_dicts(self):
        self.button_dicts.click()
        self.page.wait_for_selector(BUTTON_ADD_DICT)
        self.page.wait_for_load_state(state="load", timeout=self.timeout)

    def click_check_list(self):
        """Go to check lists"""
        self.button_check_list.click()
        self.page.wait_for_timeout(500)

    def click_gpt(self):
        self.button_gpt.click()
        self.page.wait_for_selector('[filter="url(#filter0_b_4973_59500)"]', timeout=self.timeout)
        self.page.wait_for_timeout(500)










