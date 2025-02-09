from playwright.sync_api import Page, expect
from pages.base_class import BaseClass

BUTTON_USERS = '[data-testid="userLink"]'

class AdminBar(BaseClass):
    def __init__(self, page: Page):
        super().__init__(page)
        self.button_users = page.locator(BUTTON_USERS)
        self.block_admin_bar = page.locator('[data-testid="adminBar"]')
        self.back_arrow = page.locator('[data-testid="adminBar"]').get_by_role("button")
        self.language = page.locator('[class*="styles_langHandler"]')
        self.languages_menu = page.locator('[role="listbox"]')

    def back_arrow_click(self):
        """Back arrow click"""
        self.back_arrow.click()

    def change_lang(self, current, to):
        """Change language"""
        self.language.get_by_role("button", name=current).click()
        self.page.wait_for_timeout(500)
        self.languages_menu.get_by_role("option", name=to).click()
        self.page.wait_for_selector('[class*="Hint_question__title"]')







