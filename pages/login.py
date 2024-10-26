from playwright.sync_api import Page, expect
from pages.base_class import BaseClass, BUTTON_SUBMIT

#BUTTON_VOITI = "[type='submit']" #have in base class also

ALERT_MESSAGE = '[class*="MuiAlert-message"]'

class LoginPage(BaseClass):
    def __init__(self, page: Page):
        BaseClass.__init__(self, page)
        self.profile_button = page.locator('[aria-label="Профиль"]').get_by_role("button")
        self.alert = page.locator(ALERT_MESSAGE)
        self.button_enter = page.locator(BUTTON_SUBMIT)


    def quit_from_profile(self):
        self.profile_button.click()
        self.menu.get_by_text("Выйти", exact=True).click()

    def assert_quited(self):
        expect(self.button_enter).to_be_visible()

    def assert_alert_visible(self, text: str):
        expect(self.alert).to_be_visible()
        expect(self.alert).to_contain_text(text)