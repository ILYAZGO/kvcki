#from playwright.sync_api import Page, expect
from pages.base_class import *

DEALS_FOUND = '[class*="_dealsHeaderInner_"]'

class Deals(BaseClass):
    def __init__(self, page: Page):
        super().__init__(page)

        self.deals_found = page.locator(DEALS_FOUND)
        self.deal_date = page.locator('[class*="_dealDate_"]')
        self.communications_count = page.locator('[class*="_communicationsCount_"]')
        self.score_percent = page.locator('[class*="_scorePercent_"]')
        self.deal_score = page.locator('[class*="_callScore_"]')







