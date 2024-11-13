from utils.variables import wait_until_visible
from playwright.sync_api import Page, expect
from pages.base_class import *


BUTTON_USERS = '[data-testid="userLink"]'
BUTTON_ADD_USER = BUTTON_DOBAVIT_SOTRUDNIKA = '[data-testid="addUserButton"]'


class Users(BaseClass):
    def __init__(self, page: Page):
        BaseClass.__init__(self, page)
        self.button_users = page.locator(BUTTON_USERS)
        self.button_add_user = page.locator(BUTTON_ADD_USER)
        self.select_role = page.locator(SELECT_ROLE).locator("svg")

    def go_to_users_list(self):
        self.page.wait_for_selector(BUTTON_USERS)
        self.button_users.click()
        self.page.wait_for_timeout(500)
        self.page.wait_for_selector('[class="circular-progress"]', state='hidden', timeout=self.timeout)

    def press_button_add_user(self):
        self.button_add_user.click()
        self.page.wait_for_selector(INPUT_NAME)
        self.page.wait_for_timeout(500)

    def set_user(self, name, login, password, email, phone, comment, role):
        self.page.wait_for_selector(INPUT_NAME)
        self.input_name.clear()
        self.input_name.type(name, delay=30)
        self.page.wait_for_selector(f'[value="{name}"]')
        self.input_login.clear()
        self.input_login.type(login, delay=30)
        self.page.wait_for_selector(f'[value="{login}"]')
        self.input_password.clear()
        self.input_password.type(password, delay=30)
        self.page.wait_for_selector(f'[value="{password}"]')
        self.input_email.clear()
        self.input_email.type(email, delay=30)
        self.page.wait_for_selector(f'[value="{email}"]')
        self.input_phone.clear()
        self.input_phone.type(phone, delay=30)
        self.page.wait_for_selector(f'[value="{phone}"]')
        self.input_comment.clear()
        self.input_comment.fill(comment)
        self.page.wait_for_timeout(500)
        self.select_role.click()
        self.page.wait_for_selector(MENU)
        self.menu.get_by_text(role, exact=True).click()
        self.page.wait_for_timeout(500)

    def set_operator(self, name, login, password, phone, email, comment):
        self.page.wait_for_selector(INPUT_NAME)
        self.input_name.clear()
        self.input_name.type(name, delay=30)
        self.page.wait_for_selector(f'[value="{name}"]')
        self.input_login.clear()
        self.input_login.type(login, delay=30)
        self.page.wait_for_selector(f'[value="{login}"]')
        self.input_phone.clear()
        self.input_phone.type(phone, delay=30)
        self.page.wait_for_selector(f'[value="{phone}"]')
        self.input_email.clear()
        self.input_email.type(email, delay=30)
        self.page.wait_for_selector(f'[value="{email}"]')
        self.input_comment.clear()
        self.input_comment.fill(comment)
        self.page.wait_for_timeout(500)
        self.input_password.clear()
        self.input_password.type(password, delay=30)
        self.page.wait_for_selector(f'[value="{password}"]')


BUTTON_OTMENA = '[data-testid="cancelButton"]'
BUTTON_KRESTIK = '[data-testid="closePopupButton"]'
BUTTON_DOBAVIT = '[data-testid="acceptButton"]'

BUTTON_KORZINA = '[class*="styles_actions"]'
BUTTON_PODTVERDIT = '[data-testid="acceptButton"]'
BUTTON_SOTRUDNIKI_UDALIT = "//button[contains(text(),'Удалить')]"

INPUT_NEW_PASSWORD = '[name="newPassword"]'
INPUT_NEW_PASSWORD_REPEAT = '[name="newPasswordRepeat"]'

USER_LOGIN_IN_LEFT_MENU = '[class*="headerName"]'
CHECKBOX_MERGE_ALL_TO_ONE = '[name="merge_all_to_one_audio"]'
RECOGNITION_PRIORITY = '[data-testid="count_per_iteration"]'
CHECKBOX_DIARIZATION = '[name="diarization"]'
CHECKBOX_ECONOMIZE = '[id="sttEconomize"]'
CHECKBOX_USE_WEBHOOK = '[name="use_webhook"]'
CHECKBOX_ADD_PUNCTUATION = '[name="add_punctuation"]'
CHECKBOX_ENGINE_DIARIZATION = '[name="engine_diarization"]'
CHECKBOX_NORMALIZATION = '[name="text_normalization"]'
CHECKBOX_PROFANITY_FILTER = '[name="profanity_filter"]'
CHECKBOX_LITERATURE_STYLE = '[name="literature_text"]'
CHECKBOX_PHONE_FORMATTING = '[name="phone_formatting"]'
BLOCK_WITH_BUTTON = '[class*="STT_controlButtonsBlock"]'

SELECT_ROLE = '[data-testid="selectRole"]'
SELECT_INDUSTRY = '[data-testid="selectIndustry"]'
SELECT_PARTNER = '[data-testid="selectPartner"]'
SELECT_MENU = '[class*="-menu"]'

FIRST_PAGE_PAGINATION = '[aria-label="1"]'
FIRST_ROW_IN_USERS_LIST = '[aria-rowindex="2"]'
USERS_TABLE = '[class="rs-table-body-wheel-area"]'


def press_button_add_employee(page="page: Page"):
    page.wait_for_selector(BUTTON_DOBAVIT_SOTRUDNIKA)
    page.locator(BUTTON_DOBAVIT_SOTRUDNIKA).click()
    page.wait_for_selector(INPUT_NAME)


def set_industry(industry, page="page: Page"):
    page.locator(SELECT_INDUSTRY).locator("svg").click()
    page.wait_for_selector(SELECT_MENU)
    page.locator(SELECT_INDUSTRY).get_by_text(industry, exact=True).click()
    page.wait_for_timeout(500)


def set_industry_and_partner(industry, partner, page="page: Page"):
    page.locator(SELECT_INDUSTRY).locator("svg").click()
    page.wait_for_selector(SELECT_MENU)
    page.locator(SELECT_INDUSTRY).get_by_text(industry, exact=True).click()
    page.wait_for_timeout(500)
    page.locator(SELECT_PARTNER).locator("svg").click()
    page.wait_for_selector(SELECT_MENU)
    page.locator(SELECT_PARTNER).get_by_text(partner, exact=True).click()


def set_stt(language, engine, model, page="page: Page"):
    page.locator(SELECT_LANGUAGE).click()
    page.wait_for_selector(SELECT_MENU)
    page.get_by_text(language, exact=True).click()
    page.wait_for_timeout(1000)

    page.locator(SELECT_ENGINE).click()
    page.wait_for_selector(SELECT_MENU)
    page.get_by_text(engine, exact=True).click()
    page.wait_for_timeout(1000)

    page.locator(SELECT_MODEL).click()
    page.wait_for_selector(SELECT_MENU)
    page.get_by_text(model, exact=True).click()
    page.wait_for_timeout(1000)

def delete_added_user(page="page: Page"):
    page.wait_for_timeout(500)
    page.wait_for_selector(BUTTON_KORZINA)
    page.locator(BUTTON_KORZINA).click()
    page.wait_for_timeout(500)
    page.wait_for_selector(BUTTON_PODTVERDIT)
    page.locator(BUTTON_PODTVERDIT).click()

def press_button_add_in_modal(page="page: Page"):
    page.wait_for_timeout(500)
    page.locator(BUTTON_DOBAVIT).click()
    page.wait_for_selector(MODAL_WINDOW, state="hidden")
    #page.wait_for_timeout(1000)
    #page.wait_for_selector(INPUT_PHONE)
