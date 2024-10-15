from utils.variables import wait_until_visible

USERS_LIST = "#react-select-2-input"
FIRST_DATE = '[placeholder="Начальная дата"]'
LAST_DATE = '[placeholder="Конечная дата"]'
ALERT = '[role="alert"]'
SNACKBAR = '[class*="SnackbarItem"]'

BUTTON_NASTROIKI = '[value="settings"]'
BUTTON_OPOVESHENIA = '[href*="/notifications"]'
BLOCK_LEFT_MENU = '[class*="styles_list_"]'

LEFT_MENU_ITEM = "[class='styles_content__MNyQa']"
BLOCK_PERSONAL_INFO = '[class*="LeftMenuLayout_content"]'

BUTTON_PERSONAL_INFO = '[href*="/profile"]'

BUTTON_RIGHTS = '[href*="/access-rights"]'
BUTTON_SAVE_IN_RIGHTS = '[data-testid="acceptButton"]'
BLOCK_ONE_RIGHT = '[class*="styles_toggleItem_"]'

BUTTON_ACTIONS_WITH_CALLS = '[href*="/actions-with-calls"]'
BLOCK_ACTION_SELECT = '[class="action-block"]'

BUTTON_WORD_PROCESSING = '[href*="/word-processing"]'
SELECT_LANGUAGE = '[data-testid="stt_language"]'
SELECT_ENGINE = '[data-testid="stt_engine"]'
SELECT_MODEL = '[data-testid="stt_model"]'

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

BUTTON_QUOTAS = '[href*="settings/quotas"]'
INPUT_QUOTA_TIME = '[name="time"]'

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



BUTTON_GPT_QUOTAS = '[href*="quotas/gpt-quotas"]'
BLOCK_GPT_QUOTAS = '[class*="styles_quotasWrapper"]'
BLOCK_CHAT_GPT = '[class*="styles_ChatGPTwrapper"]'
BLOCK_YANDEX_GPT = '[class*="styles_YandexGPTwrapper"]'
INPUT_NEW_QUOTA = '[placeholder="Новое значение"]'
BLOCK_WITH_SAVE_BUTTON = '[class*="styles_saveButton"]'
BUTTON_SAVE = '[type="submit"]'
BLOCK_WITH_AMOUNT = '[class*="styles_amount_"]'


BUTTON_ADDRESS_BOOK = '[href*="/address-book"]'
INPUT_ADDRESS_BOOK = '[class*="AddressBookTextArea"]'

BUTTON_EMPLOYEES = '[href*="settings/employees"]'
BUTTON_DOBAVIT_POLZOVATELIA = BUTTON_DOBAVIT_SOTRUDNIKA = '[data-testid="addUserButton"]'

INPUT_LOGIN = '[name="login"]'
INPUT_NAME = '[name="name"]'
INPUT_EMAIL = '[name="email"]'
INPUT_PHONE = '[name="phoneNumber"]'
INPUT_COMMENT = '[name="comment"]'
INPUT_NEW_PASSWORD = '[name="newPassword"]'
INPUT_NEW_PASSWORD_REPEAT = '[name="newPasswordRepeat"]'

SELECT_PARTNER = '[data-testid="selectPartner"]'
SELECT_INDUSTRY = '[data-testid="selectIndustry"]'
SELECT_TIMEZONE = '[data-testid="selectTimezone"]'
SELECT_MENU = '[class*="-menu"]'
MODAL_WINDOW = '[role="dialog"]'


def click_settings(page="page: Page"):
    page.wait_for_selector(BUTTON_NASTROIKI, timeout=wait_until_visible)
    page.locator(BUTTON_NASTROIKI).click()
    page.wait_for_timeout(500)
    page.wait_for_selector(INPUT_LOGIN)
    page.wait_for_timeout(500)


def click_notifications(page="page: Page"):
    page.locator(BUTTON_OPOVESHENIA).click()
    page.wait_for_timeout(1000)


def click_personal_info(page="page: Page"):
    page.locator(BUTTON_PERSONAL_INFO).click()
    page.wait_for_selector(INPUT_LOGIN)


def click_employees(page="page: Page"):
    page.locator(BUTTON_EMPLOYEES).click()
    page.wait_for_selector(BUTTON_DOBAVIT_SOTRUDNIKA)


def click_rights(page="page: Page"):
    page.locator(BUTTON_RIGHTS).click()
    page.wait_for_selector('[class*="FooterButtons"]')

def click_actions_with_calls(page="page: Page"):
    page.locator(BUTTON_ACTIONS_WITH_CALLS).click()
    page.wait_for_selector(BLOCK_ACTION_SELECT)

def click_word_processing(page="page: Page"):
    page.locator(BUTTON_WORD_PROCESSING).click()
    page.wait_for_selector(SELECT_LANGUAGE)

def click_engine_select(page="page: Page"):
    page.locator(SELECT_ENGINE).locator('[type="text"]').click()
    page.wait_for_selector(SELECT_MENU)

def click_model_select(page="page: Page"):
    page.locator(SELECT_MODEL).locator('[type="text"]').click()
    page.wait_for_selector(SELECT_MENU)

def choose_option(optionNumber, page="page: Page"):
    page.locator(SELECT_MENU).locator(f'[id$="-option-{optionNumber}"]').click()

def click_submit_in_word_processing(page="page: Page"):
    page.locator(BLOCK_WITH_BUTTON).locator(BUTTON_SAVE).click()
    page.wait_for_timeout(500)

def click_quota(page="page: Page"):
    page.locator(BUTTON_QUOTAS).click()
    page.wait_for_timeout(500)
    page.wait_for_selector('[aria-colcount="6"]')


def click_address_book(page="page: Page"):
    page.locator(BUTTON_ADDRESS_BOOK).click()
    page.wait_for_selector(INPUT_ADDRESS_BOOK)


def fill_quota_time(minutes, page="page: Page"):
    page.locator(INPUT_QUOTA_TIME).clear()
    page.locator(INPUT_QUOTA_TIME).fill(minutes)


def press_add_in_quotas(page="page: Page"):
    page.get_by_role("button", name="Добавить", exact=True).click()
    page.wait_for_selector(MODAL_WINDOW)



def fill_address_book(Text, page="page: Page"):
    page.locator(INPUT_ADDRESS_BOOK).clear()
    page.wait_for_timeout(800)
    page.locator(INPUT_ADDRESS_BOOK).fill(Text)
    page.wait_for_timeout(800)


def choose_preiod_date(firstDate, lastDate, page="page: Page"):
    page.locator(FIRST_DATE).click()
    page.locator(FIRST_DATE).fill(firstDate)
    page.wait_for_timeout(500)
    page.locator(LAST_DATE).click()
    page.locator(LAST_DATE).fill(lastDate)
    page.wait_for_timeout(500)
    page.keyboard.press("Enter")


def change_login(login, page="page: Page"):
    page.wait_for_selector(INPUT_LOGIN)
    page.locator(INPUT_LOGIN).clear()
    page.locator(INPUT_LOGIN).fill(login)


def fill_personal_information_admin_and_manager(name, email, phone, comment, timezone, page="page: Page"):
    #  admin and manager can see and write comment
    page.wait_for_timeout(500)
    page.locator(INPUT_NAME).fill(name)
    page.wait_for_selector(f'[value="{name}"]')
    page.locator(INPUT_EMAIL).fill(email)
    page.wait_for_selector(f'[value="{email}"]')
    page.locator(INPUT_PHONE).fill(phone)
    page.wait_for_selector(f'[value="{phone}"]')
    page.locator(INPUT_COMMENT).fill(comment)
    page.wait_for_timeout(200)
    page.locator(SELECT_TIMEZONE).locator('[role="combobox"]').click()
    page.get_by_text(timezone).click()
    page.wait_for_selector(f'[value="{timezone}"]', state="hidden")


def fill_personal_information_user_and_operator(name, email, phone, timezone, page="page: Page"):
    #  user and operator cant see and write comment
    page.locator(INPUT_NAME).fill(name)
    page.wait_for_selector(f'[value="{name}"]')
    page.locator(INPUT_EMAIL).fill(email)
    page.wait_for_selector(f'[value="{email}"]')
    page.locator(INPUT_PHONE).fill(phone)
    page.wait_for_selector(f'[value="{phone}"]')
    page.locator(SELECT_TIMEZONE).locator('[role="combobox"]').click()
    page.get_by_text(timezone).click()
    page.wait_for_selector(f'[value="{timezone}"]', state="hidden")
    page.wait_for_timeout(300)


def change_industry(industry, page="page: Page"):
    page.locator(SELECT_INDUSTRY).click()
    page.wait_for_selector(SELECT_MENU)
    page.locator(SELECT_MENU).get_by_text(industry, exact=True).click()


def change_partner(partner, page="page: Page"):
    page.locator(SELECT_PARTNER).click()
    page.wait_for_selector(SELECT_MENU)
    page.locator(SELECT_MENU).get_by_text(partner, exact=True).click()


def go_to_user(name, page="page: Page"):
    page.wait_for_selector(USERS_LIST)
    page.locator(USERS_LIST).fill(name)
    page.wait_for_selector(SELECT_MENU)
    page.locator(SELECT_MENU).get_by_text(name, exact=True).click()
    page.wait_for_selector('[class*="CallsHeader"]', timeout=wait_until_visible)


def go_to_operator_from_table(page="page: Page"):
    page.wait_for_selector('[role="gridcell"]')
    page.locator('[aria-rowindex="2"]').locator('[class="rs-table-cell rs-table-cell-first"]').click()
    page.wait_for_timeout(1000)
    page.wait_for_selector(INPUT_LOGIN)


def go_to_admin_or_manager(name, page="page: Page"):
    page.wait_for_selector(USERS_LIST)
    page.locator(USERS_LIST).fill(name)
    page.wait_for_selector(SELECT_MENU)
    page.locator(SELECT_MENU).get_by_text(name, exact=True).click()
    page.wait_for_timeout(2000)


def press_save(page="page: Page"):
    page.get_by_role("button", name="Сохранить").click()
    page.wait_for_timeout(1000)


def press_save_in_rights(page="page: Page"):
    page.locator(BUTTON_SAVE_IN_RIGHTS).click()
    page.wait_for_timeout(500)


def click_all_checkboxes_on_page(page="page: Page"):
    # Находим все чекбоксы на странице
    checkboxes = page.query_selector_all('input[type="checkbox"]')
    # Выполняем клик на каждом чекбоксе
    for checkbox in checkboxes:
        if not checkbox.is_checked():
            checkbox.click()


def all_checkboxes_to_be_checked(page="page: Page"):
    page.wait_for_timeout(500)
    # Находим все чекбоксы на странице
    checkboxes = page.query_selector_all('input[type="checkbox"]')
    page.wait_for_timeout(500)
    # Проверяем состояние каждого чекбокса
    all_checked = all(checkbox.is_checked() for checkbox in checkboxes)
    return all_checked

