USEDESK_TOKEN = "979be5305c275d4e3bce559f3c563e5721e66c61"

from pages.base_class import *
from playwright.sync_api import Page, expect

INPUT_API_TOKEN = '[data-testid="api_token"]'
INPUT_CALLS_LIMIT = '[name="maxNewCalls"]'

BUTTON_INTEGRACII_IN_MENU = '[href*="settings/integrations"]'
BUTTON_PODKLU4IT = ".styles_goToIntegrationsList__KXaHU"
BUTTON_SAVE = '[data-testid="AccessKeysTab_submit"]'
BUTTON_INTEGRACII = ".styles_firstTitle__iaGwm"
BUTTON_SOZDAT = '[data-testid="StartTaskModalContent_submit"]'
BUTTON_PLAY = '[aria-label="Запуск интеграции"]'
BUTTON_KORZINA = "div[class='styles_button__xgQ1q'] button[type='button']"
BUTTON_UDALIT_INTEGRACIYU = '[data-testid="SettingsCell_deleteBtn"]'
BUTTON_OK_IN_DATE = "button[class='ant-btn ant-btn-primary ant-btn-sm']"
NAYDENO_ZVONKOV_INTEGRATION = '//*[@id="root"]/div/div[3]/div/div[3]/div[1]/div/p'
LOGIN_IN_LEFT_MENU = ".MuiTypography-root.MuiTypography-body1.styles_headerLogin__eWAxf.css-pd9d9b"


class Integrations(BaseClass):
    def __init__(self, page: Page):
        BaseClass.__init__(self, page)
        self.input_token = page.locator(INPUT_API_TOKEN).locator('[type="text"]')
        self.button_save = page.locator(BUTTON_SAVE)
        self.button_ok_in_dates = page.locator(BUTTON_OK_IN_DATE)
        self.input_calls_limit = page.locator(INPUT_CALLS_LIMIT)
        self.button_play = page.locator(BUTTON_PLAY).locator('[type="button"]')

    def input_api_token(self):
        self.page.wait_for_selector(INPUT_API_TOKEN)
        self.input_token.type(USEDESK_TOKEN, delay=20)

    def press_save(self):
        self.button_save.click()
        self.page.wait_for_selector(MODAL_WINDOW, state="hidden")

    def set_date(self, first_date: str):
        self.first_date.click()
        self.page.wait_for_selector(BUTTON_OK_IN_DATE)
        self.first_date.fill(first_date)
        self.page.wait_for_timeout(700)
        self.button_ok_in_dates.click()
        self.page.wait_for_timeout(1500)
        self.button_ok_in_dates.click()
        self.page.wait_for_timeout(700)

    def set_calls_limit(self, calls_limit: str):
        self.input_calls_limit.type(calls_limit, delay=20)

    def delete_integration(self):
        self.page.locator(BUTTON_KORZINA).click()
        self.page.wait_for_selector(MODAL_WINDOW)
        self.page.wait_for_timeout(500)
        self.page.locator(BUTTON_UDALIT_INTEGRACIYU).click()
        self.page.wait_for_timeout(1000)

    def press_play(self):
        self.page.wait_for_selector(BUTTON_PLAY)
        self.button_play.click()








