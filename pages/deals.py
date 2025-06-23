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

        self.deal_communication_date = page.locator('[class*="_singleDealBlock_"]').locator('[class*="_operatorTagsBlockData_"]')
        self.deal_communication_score_percent = page.locator('[class*="_singleDealBlock_"]').locator('[class*="_scorePercent_"]')
        self.deal_communication_score = page.locator('[class*="_singleDealBlock_"]').locator('[class*="_callScore_"]')

        self.deal_communication_operator_phone = page.locator('[class*="_singleDealBlock_"]').locator('[class*="_operatorPhone_"]')
        self.deal_communication_client_phone = page.locator('[class*="_singleDealBlock_"]').locator('[class*="_clientTagsBlockPhone_"]')
        self.deal_communication_duration = page.locator('[class*="_singleDealBlock_"]').locator('[class*="_clientTagsBlockDuration_"]')

        self.deal_communication_score = page.locator('[class*="_singleDealBlock_"]').locator('[class*="_callScore_"]')
        self.deal_communication_deal_tags_block = page.locator('[class*="_singleDealBlock_"]').locator('[class*="_dealTagsBlock_"]')

        self.blue_tag = page.locator('[class*="_blueTag_"]')
        self.deal_tags_block = page.locator('[class*="_dealTagsBlock_"]')
        self.deal_tag = page.locator('[class*="_lightBlueTag_"]')
        self.deal_button_retag = page.locator('[aria-label="Перетегировать"]')

    def download_deal(self):
        self.button_calls_list_download.click()
        self.page.wait_for_selector(MENU)





