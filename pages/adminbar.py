from playwright.sync_api import Page, expect
from pages.base_class import BaseClass

BUTTON_USERS = '[data-testid="userLink"]'

class AdminBar(BaseClass):
    def __init__(self, page: Page):
        BaseClass.__init__(self, page)
        self.button_users = page.locator('[data-testid="userLink"]')
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



# USERS_LIST = "#react-select-2-input"
#

# BLOCK_ADMIN_BAR = '[data-testid="adminBar"]'
#
#
# def go_to_user(name, page="page: Page"):
#     page.locator(USERS_LIST).fill(name)
#     page.wait_for_timeout(300)
#     page.get_by_text(name, exact=True).click()
#     page.wait_for_selector('[class*="CallsHeader"]')
#
# def change_lang(current, to, page="page: Page"):
#     page.locator('[class*="styles_langHandler"]').get_by_role("button", name=current).click()
#     page.wait_for_timeout(300)
#     page.get_by_role("option", name=to).click()
#     page.wait_for_selector('[class*="Hint_question__title"]')








