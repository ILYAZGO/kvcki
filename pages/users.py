from playwright.sync_api import Page, expect
from pages.base_class import *


BUTTON_USERS = '[data-testid="userLink"]'
BUTTON_ADD_USER = '[data-testid="addUserButton"]' # same button for employee
BUTTON_OTMENA = '[data-testid="cancelButton"]'
BUTTON_KORZINA = '[class*="styles_actions"]'

USER_LOGIN_IN_LEFT_MENU = '[class*="headerName"]'
CHECKBOX_MERGE_ALL_TO_ONE = '[name="merge_all_to_one_audio"]'
RECOGNITION_PRIORITY = '[data-testid="count_per_iteration"]'
CHECKBOX_DIARIZATION = '[name="diarization"]'
CHECKBOX_ECONOMIZE = '[id="sttEconomize"]'
CHECKBOX_ADD_PUNCTUATION = '[name="add_punctuation"]'
CHECKBOX_ENGINE_DIARIZATION = '[name="engine_diarization"]'
CHECKBOX_NORMALIZATION = '[name="text_normalization"]'
CHECKBOX_PROFANITY_FILTER = '[name="profanity_filter"]'
CHECKBOX_LITERATURE_STYLE = '[name="literature_text"]'
CHECKBOX_PHONE_FORMATTING = '[name="phone_formatting"]'


class Users(BaseClass):
    def __init__(self, page: Page):
        super().__init__(page)
        self.button_users = page.locator(BUTTON_USERS)
        self.button_add_user = page.locator(BUTTON_ADD_USER)
        self.select_role = page.locator(SELECT_ROLE).locator("svg")


    def go_to_users_list(self):
        self.page.wait_for_selector(BUTTON_USERS)
        self.button_users.click()
        self.page.wait_for_timeout(1000)
        self.page.wait_for_selector('[class="circular-progress"]', state='hidden', timeout=self.timeout)

    def press_button_add_user(self):
        self.button_add_user.click()
        self.page.wait_for_selector(MODAL_WINDOW, timeout=self.timeout)
        self.page.wait_for_timeout(500)

    def set_user(self, name, login, password, email, phone, user_lang,comment, role):
        self.page.wait_for_selector(INPUT_NAME)
        self.input_name.clear()
        self.input_name.type(name, delay=10)
        self.page.wait_for_selector(f'[value="{name}"]')
        self.input_login.clear()
        self.input_login.type(login, delay=10)
        self.page.wait_for_selector(f'[value="{login}"]')
        self.input_password.clear()
        self.input_password.type(password, delay=10)
        self.page.wait_for_selector(f'[value="{password}"]')
        self.input_email.clear()
        self.input_email.type(email, delay=10)
        self.page.wait_for_selector(f'[value="{email}"]')
        self.input_phone.clear()
        self.input_phone.type(phone, delay=10)
        self.page.wait_for_selector(f'[value="{phone}"]')
        self.input_comment.clear()
        self.input_comment.fill(comment)
        self.page.wait_for_timeout(500)
        self.select_user_lang.click()
        self.page.wait_for_selector(MENU)
        self.menu.get_by_text(user_lang, exact=True).click()
        self.page.wait_for_timeout(500)
        self.select_role.click()
        self.page.wait_for_selector(MENU)
        self.menu.get_by_text(role, exact=True).click()
        self.page.wait_for_timeout(500)

    def set_operator(self, name, login, password, phone, email, comment, user_lang):
        self.page.wait_for_selector(INPUT_NAME)
        self.input_name.clear()
        self.input_name.type(name, delay=10)
        self.page.wait_for_selector(f'[value="{name}"]')
        self.input_login.clear()
        self.input_login.type(login, delay=10)
        self.page.wait_for_selector(f'[value="{login}"]')
        self.input_phone.clear()
        self.input_phone.type(phone, delay=10)
        self.page.wait_for_selector(f'[value="{phone}"]')
        self.input_email.clear()
        self.input_email.type(email, delay=10)
        self.page.wait_for_selector(f'[value="{email}"]')
        self.input_comment.clear()
        self.input_comment.fill(comment)
        self.page.wait_for_timeout(500)
        self.select_user_lang.click()
        self.page.wait_for_selector(MENU)
        self.menu.get_by_text(user_lang, exact=True).click()
        self.page.wait_for_timeout(500)
        self.input_password.clear()
        self.input_password.type(password, delay=10)
        self.page.wait_for_selector(f'[value="{password}"]')

    def set_stt(self, language, engine, model):
        self.select_language.click()
        self.page.wait_for_selector(MENU)
        self.page.get_by_text(language, exact=True).click()
        self.page.wait_for_timeout(1000)

        self.select_engine.click()
        self.page.wait_for_selector(MENU)
        self.page.get_by_text(engine, exact=True).click()
        self.page.wait_for_timeout(1000)

        self.select_model.click()
        self.page.wait_for_selector(MENU)
        self.page.get_by_text(model, exact=True).click()
        self.page.wait_for_timeout(1000)

    def set_industry(self, industry):
        self.page.locator(SELECT_INDUSTRY).locator("svg").click()
        self.page.wait_for_selector(MENU)
        self.page.locator(SELECT_INDUSTRY).get_by_text(industry, exact=True).click()
        self.page.wait_for_timeout(500)

    def set_industry_and_partner(self, industry, partner):
        self.page.locator(SELECT_INDUSTRY).locator("svg").click()
        self.page.wait_for_selector(MENU)
        self.page.locator(SELECT_INDUSTRY).get_by_text(industry, exact=True).click()
        self.page.wait_for_timeout(500)
        self.page.locator(SELECT_PARTNER).locator("svg").click()
        self.page.wait_for_selector(MENU)
        self.page.locator(SELECT_PARTNER).get_by_text(partner, exact=True).click()

    def delete_added_user(self):
        self.page.wait_for_timeout(500)
        self.page.wait_for_selector(BUTTON_KORZINA)
        self.page.locator(BUTTON_KORZINA).click()
        self.page.wait_for_timeout(500)
        self.page.wait_for_selector(MODAL_WINDOW)
        self.page.locator(BUTTON_ACCEPT).click()

    def press_button_add_in_modal(self):
        self.page.wait_for_timeout(500)
        self.page.locator(BUTTON_ACCEPT).click()
        self.page.wait_for_selector(MODAL_WINDOW, state="hidden")
        self.page.wait_for_selector(INPUT_PHONE, timeout=self.timeout)

