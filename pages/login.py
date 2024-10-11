from playwright.sync_api import Page, expect
from pages.base_class import BaseClass

BUTTON_VOITI = "[type='submit']" #have in base class also

ALERT_MESSAGE = '[class*="MuiAlert-message"]'

class LoginPage(BaseClass):
    def __init__(self, page: Page):
        BaseClass.__init__(self, page)
        self.profile_button = page.locator('[aria-label="Профиль"]').get_by_role("button")
        self.alert = page.locator('[class*="MuiAlert-message"]')


    def quit_from_profile(self):
        self.profile_button.click()
        self.menu.get_by_text("Выйти", exact=True).click()



# def quit_from_profile(page="page: Page"):
#     page.locator('[aria-label="Профиль"]').get_by_role("button").click()
#     page.get_by_text("Выйти", exact=True).click()
