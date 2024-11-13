from playwright.sync_api import Page, expect
from pages.base_class import *

from utils.variables import wait_until_visible

BUTTON_ADDRESS_BOOK = '[href*="/address-book"]'
INPUT_ADDRESS_BOOK = '[class*="AddressBookTextArea"]'

BUTTON_PERSONAL_INFO = '[href*="/profile"]'
BUTTON_RIGHTS = '[href*="/access-rights"]'
BUTTON_EMPLOYEES = '[href*="settings/employees"]'
BUTTON_QUOTAS = '[href*="settings/quotas"]'
INPUT_QUOTA_TIME = '[name="time"]'

BLOCK_LEFT_MENU = '[class*="styles_list_"]'
LEFT_MENU_ITEM = "[class='styles_content__MNyQa']"
BLOCK_PERSONAL_INFO = '[class*="LeftMenuLayout_content"]'
BUTTON_SAVE_IN_RIGHTS = '[data-testid="acceptButton"]'
BLOCK_ONE_RIGHT = '[class*="styles_toggleItem_"]'

INPUT_LOGIN = '[name="login"]'
INPUT_NAME = '[name="name"]'
INPUT_EMAIL = '[name="email"]'
INPUT_PHONE = '[name="phoneNumber"]'
INPUT_COMMENT = '[name="comment"]'
INPUT_NEW_PASSWORD = '[name="newPassword"]'
INPUT_NEW_PASSWORD_REPEAT = '[name="newPasswordRepeat"]'

BUTTON_DOBAVIT_POLZOVATELIA = BUTTON_DOBAVIT_SOTRUDNIKA = '[data-testid="addUserButton"]'

SELECT_PARTNER = '[data-testid="selectPartner"]'
SELECT_INDUSTRY = '[data-testid="selectIndustry"]'
SELECT_TIMEZONE = '[data-testid="selectTimezone"]'

BUTTON_ACTIONS_WITH_CALLS = '[href*="/actions-with-calls"]'
BLOCK_ACTION_SELECT = '[class="action-block"]'
BUTTON_WORD_PROCESSING = '[href*="/word-processing"]'

class Settings(BaseClass):
    def __init__(self, page: Page):
        BaseClass.__init__(self, page)
        self.button_address_book = page.locator(BUTTON_ADDRESS_BOOK)
        self.input_address_book = page.locator(INPUT_ADDRESS_BOOK)
        self.button_personal_info = page.locator(BUTTON_PERSONAL_INFO)
        self.button_rights = page.locator(BUTTON_RIGHTS)
        # self.button_employees = page.locator(BUTTON_EMPLOYEES)
        self.button_word_pocessing = page.locator(BUTTON_WORD_PROCESSING)
        self.button_quotas = page.locator(BUTTON_QUOTAS)
        self.button_save_in_rights = page.locator(BUTTON_SAVE_IN_RIGHTS)
        self.input_quota_time = page.locator(INPUT_QUOTA_TIME)
        self.input_login = page.locator(INPUT_LOGIN)
        self.input_timezone = page.locator(SELECT_TIMEZONE)
        self.select_industry = page.locator(SELECT_INDUSTRY)
        self.select_partner = page.locator(SELECT_PARTNER)


    def click_address_book(self):
        """Click address book button"""
        self.button_address_book.click()
        self.page.wait_for_selector(INPUT_ADDRESS_BOOK)

    def fill_address_book(self, text: str):
        """Fill address book with text"""
        self.input_address_book.clear()
        self.page.wait_for_timeout(1000)
        self.input_address_book.fill(text)
        self.page.wait_for_timeout(1000)

    def assert_address_book_text(self, text: str):
        """Check address book text"""
        expect(self.input_address_book).to_contain_text([text])

    def click_personal_info(self):
        self.button_personal_info.click()
        self.page.wait_for_selector(INPUT_LOGIN)

    def click_rights(self):
        self.button_rights.click()
        self.page.wait_for_timeout(1000)
        self.page.wait_for_selector('[data-testid="acceptButton"]')

    # def click_employees(self):
    #     self.button_employees.click()
    #     self.page.wait_for_load_state(state="load", timeout=self.timeout)
    #     self.page.wait_for_selector('[role="grid"]')

    def click_word_processing(self):
        self.button_word_pocessing.click()
        self.page.wait_for_selector(SELECT_LANGUAGE)

    def click_quota(self):
        self.button_quotas.click()
        self.page.wait_for_timeout(500)
        self.page.wait_for_selector('[role="grid"]')

    def fill_quota_time(self, minutes: str):
        self.page.wait_for_timeout(500)
        self.input_quota_time.clear()
        self.page.wait_for_timeout(500)
        self.input_quota_time.type(minutes, delay=30)

    def press_add_in_quotas(self):
        """Working in table and modal window"""
        self.page.get_by_role("button", name="Добавить", exact=True).click()
        self.page.wait_for_selector(MODAL_WINDOW)

    def press_save(self):
        self.page.get_by_role("button", name="Сохранить").click()
        self.page.wait_for_timeout(500)

    def press_save_in_rights(self):
        self.button_save_in_rights.click()
        self.page.wait_for_timeout(500)

    def click_actions_with_calls(self):
        self.page.locator(BUTTON_ACTIONS_WITH_CALLS).click()
        self.page.wait_for_selector(BLOCK_ACTION_SELECT)

    def go_to_operator_from_table(self):
        self.page.locator('[aria-rowindex="2"]').locator('[class="rs-table-cell rs-table-cell-first"]').click()
        self.page.wait_for_load_state(state="load", timeout=self.timeout)
        self.page.wait_for_selector(INPUT_LOGIN)

    def change_login(self, login):
        self.page.wait_for_selector(INPUT_LOGIN)
        self.input_login.clear()
        self.input_login.type(login, delay=30)

    def change_industry(self, industry):
        self.select_industry.click()
        self.page.wait_for_selector(MENU)
        self.menu.get_by_text(industry, exact=True).click()

    def change_partner(self, partner):
        self.select_partner.click()
        self.page.wait_for_selector(MENU)
        self.page.locator(MENU).get_by_text(partner, exact=True).click()

    def click_all_checkboxes_on_page(self):
        # Находим все чекбоксы на странице
        checkboxes = self.page.query_selector_all('input[type="checkbox"]')
        # Выполняем клик на каждом чекбоксе
        for checkbox in checkboxes:
            if not checkbox.is_checked():
                checkbox.click()

    def fill_personal_information_admin_and_manager(self, name, email, phone, comment, timezone):
        """admin and manager can see and write comment"""
        self.page.wait_for_timeout(500)
        self.input_name.clear()
        self.input_name.type(name, delay=30)
        self.page.wait_for_selector(f'[value="{name}"]')
        self.input_email.clear()
        self.input_email.type(email, delay=30)
        self.page.wait_for_selector(f'[value="{email}"]')
        self.input_phone.clear()
        self.input_phone.type(phone, delay=30)
        self.page.wait_for_selector(f'[value="{phone}"]')
        self.input_comment.clear()
        self.input_comment.fill(comment)
        self.page.wait_for_timeout(500)
        self.input_timezone.locator('[role="combobox"]').click()
        self.page.get_by_text(timezone).click()
        self.page.wait_for_selector(f'[value="{timezone}"]', state="hidden")

    def fill_personal_information_user_and_operator(self, name, email, phone, timezone):
        """user and operator cant see and write comment"""
        self.page.wait_for_timeout(500)
        self.input_name.clear()
        self.input_name.type(name, delay=30)
        self.page.wait_for_selector(f'[value="{name}"]')
        self.input_email.clear()
        self.input_email.type(email, delay=30)
        self.page.wait_for_selector(f'[value="{email}"]')
        self.input_phone.clear()
        self.input_phone.type(phone, delay=30)
        self.page.wait_for_selector(f'[value="{phone}"]')
        self.page.wait_for_timeout(500)
        self.input_timezone.locator('[role="combobox"]').click()
        self.page.wait_for_selector(MENU)
        self.menu.get_by_text(timezone).click()
        self.page.wait_for_selector(f'[value="{timezone}"]', state="hidden")
        self.page.wait_for_timeout(500)

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

BUTTON_CONSUMPTION_HISTORY = '[href*="-consumption-history"]'
BUTTON_CONSUMPTION_HISTORY_AUDIO = '[href*="-consumption-history/audio"]'
BUTTON_CONSUMPTION_HISTORY_GPT = '[href*="-consumption-history/gpt"]'
BUTTON_CONSUMPTION_HISTORY_CHATS = '[href*="-consumption-history/dialogs"]'
SEARCH_IN_CONSUMPTION_AUDIO = '[data-testid="AudioCommunications_searchBySource"]'
SEARCH_IN_CONSUMPTION_GPT = '[data-testid="GPTCommunications_searchBySource"]'
SEARCH_IN_CONSUMPTION_CHATS = '[data-testid="DialogsCommunications_searchBySource"]'
CALENDAR_IN_CONSUMPTION = '[class="ant-space-item"]'
TOTAL_AUDIO_MIN = '[class*="communicationsStyles_totalValueInMinutes_"]'
TOTAL_AUDIO_HOURS = '[class*="communicationsStyles_totalValueInHours_"]'
TOTAL_GPT_MONEY = '[class*="communicationsStyles_gptValuesWrapper_"]'
TOTAL_CHATS = '[class*="communicationsStyles_chatsValuesWrapper_"]'

BUTTON_TARIFFICATION = '[href*="/settings/billing"]'
BUTTON_RATES = '[href*="/settings/billing/aboutRates"]'
BUTTON_WRITEOFFS = '[href*="/settings/billing/writeoffs"]'
BUTTON_CHARGES = '[href*="/settings/billing/payments"]'
MESSAGE_TARIFFICATION_EMPTY = '[class*="styles_firstLine__"]'
SEARCH_IN_TARIFFICATION = '[data-testid="Writeoffs_search"]'
TOTAL_IN_TABLE = '[class*="style_valuesWrapper_"]'

BUTTON_GPT_QUOTAS = '[href*="quotas/gpt-quotas"]'
BLOCK_GPT_QUOTAS = '[class*="styles_quotasWrapper"]'
BLOCK_CHAT_GPT = '[class*="styles_ChatGPTwrapper"]'
BLOCK_YANDEX_GPT = '[class*="styles_YandexGPTwrapper"]'
INPUT_NEW_QUOTA = '[placeholder="Новое значение"]'
BLOCK_WITH_SAVE_BUTTON = '[class*="styles_saveButton"]'
BLOCK_WITH_AMOUNT = '[class*="styles_amount_"]'


def all_checkboxes_to_be_checked(page="page: Page"):
    page.wait_for_timeout(500)
    # Находим все чекбоксы на странице
    checkboxes = page.query_selector_all('input[type="checkbox"]')
    page.wait_for_timeout(500)
    # Проверяем состояние каждого чекбокса
    all_checked = all(checkbox.is_checked() for checkbox in checkboxes)
    return all_checked

