#from playwright.sync_api import Page, expect
from pages.base_class import *

DEALS_FOUND = '[class*="_dealsHeaderInner_"]'

class Deals(BaseClass):
    def __init__(self, page: Page):
        super().__init__(page)

        self.deals_found = page.locator(DEALS_FOUND)
        self.deal_id_block = page.locator('[class*="_dealIdBlock_"]')









