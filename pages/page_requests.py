#from playwright.sync_api import Page, expect
from pages.base_class import *

BUTTON_DICTS = '[data-testid="markup_nav_dicts"]'

class PageRequests(BaseClass):
    def __init__(self, page: Page):
        super().__init__(page)
        self.button_dicts = page.locator(BUTTON_DICTS)








