from re import search

from playwright.sync_api import Page, expect
from pages.base_class import BaseClass, BUTTON_SUBMIT

from utils.variables import wait_until_visible


NAYDENO_ZVONKOV = '[class*="CallsHeader_callsTitleText"]'
FIRST_PAGE_PAGINATION = '[aria-label="page 1"]'
CALL_DATE_AND_TIME = '//html/body/div/div/div[2]/div/div[3]/div[2]/div[1]/div/div/div/div/div[1]/div[1]/div[1]/div[2]/div/p'
CHANGE_SORT = '//*[@id="root"]/div/div[2]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/div/div[2]/div'
COMMENT_AREA = '[class*="styles_content_"]'
ALL_COMMENTS_AREA = '[class*="styles_withAllComments_"]'
SELECT_WITH_SEARCH_MANUAL_TAGS = '[data-testid="CustomSelectWithSearch"]'
TAG = '[data-testid*="tag-"]'
MODAL_WINDOW = '[role="dialog"]'

INPUT_CLIENT_NUMBER = '[data-testid="filters_client_phone"]'
INPUT_CLIENT_DICT_OR_TEXT = '[data-testid="filters_client_phrases"]'
INPUT_EMPLOYEE_NUMBER = '[data-testid="filters_operator_phone"]'
INPUT_EMPLOYEE_DICT_OR_TEXT = '[data-testid="filters_operator_phrases"]'
INPUT_TIME = '[data-testid="filters_call_time_interval"]'
INPUT_CALL_DURATION = '[data-testid="filters_call_duration"]'
INPUT_ID = '[data-testid="filters_any_id"]'
INPUT_BY_TAGS = '[data-testid="filters_search_by_tags"]'


BUTTON_CALLS_ACTION = '[data-testid="calls_actions_actions-btn"]'    # (...) button
BUTTON_CLEAR = '[data-testid="calls_btns_clear"]'

BUTTON_EXPAND_CALL = '[data-testid="call_expand"]'
BUTTON_ADD_COMMENT = '[class*="styles_addButton"]'
BUTTON_ADD_COMMENT_TITLE = '[class*="styles_addTitleButton"]'

COMMUNICATIONS_SEARCH = "//h6[contains(text(),'Поиск по коммуникациям')]"

OPEN_CALL_AREA = '[class="MuiAccordion-region"]'
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


class Communications(BaseClass):
    def __init__(self, page: Page):
        BaseClass.__init__(self, page)
        self.button_find_communications = page.locator('[data-testid="calls_btns_find"]')
        self.button_calls_action = page.locator(BUTTON_CALLS_ACTION)
        self.button_expand_call = page.locator(BUTTON_EXPAND_CALL)
        self.button_add_comment = page.locator(BUTTON_ADD_COMMENT)
        self.button_cross_in_manual_tags = page.locator('[class*="_manualGroup_"]').locator('[type="button"]')
        self.button_submit_in_word_processing = page.locator(BLOCK_WITH_BUTTON).locator(BUTTON_SUBMIT)
        self.communications_found = page.locator('[class*="CallsHeader_callsTitleText"]')
        self.sort = page.locator(CHANGE_SORT)
        self.tag = page.locator(TAG)
        self.button_clear = page.locator(BUTTON_CLEAR)
        self.call_date_and_time = page.locator(CALL_DATE_AND_TIME)
        self.just_click = page.locator(COMMUNICATIONS_SEARCH)
        self.input_client_number = page.locator(INPUT_CLIENT_NUMBER).locator('[type="text"]')
        self.input_client_dict_or_text = page.locator(INPUT_CLIENT_DICT_OR_TEXT).locator('[type="text"]')
        self.input_employee_number = page.locator(INPUT_EMPLOYEE_NUMBER).locator('[type="text"]')
        self.input_employee_dict_or_text = page.locator(INPUT_EMPLOYEE_DICT_OR_TEXT).locator('[type="text"]')
        self.input_time = page.locator(INPUT_TIME).locator('[type="text"]')
        self.input_call_duration = page.locator(INPUT_CALL_DURATION).locator('[type="text"]')
        self.input_id = page.locator(INPUT_ID).locator('[type="text"]')
        self.input_by_tags = page.locator(INPUT_BY_TAGS).locator('[type="text"]')
        self.input_manual_tag_name = page.locator(SELECT_WITH_SEARCH_MANUAL_TAGS).locator('[type="text"]')


    def assert_check_period_dates(self, begin: str, end: str):
        """Check first and last dates"""
        self.page.wait_for_timeout(500)
        expect(self.first_date).to_have_value(begin)
        expect(self.last_date).to_have_value(end)

    def assert_check_period_dates_disabled(self):
        """Check that dates disabled if all-time"""
        expect(self.first_date).to_be_disabled()
        expect(self.last_date).to_be_disabled()

    def press_find_communications_more_than_50(self):
        """If more than 50, waiting pagination"""
        self.page.wait_for_timeout(1000)
        self.button_find_communications.click()
        self.page.wait_for_timeout(500)
        self.page.wait_for_selector(NAYDENO_ZVONKOV, timeout=self.timeout)
        self.page.wait_for_timeout(500)
        self.page.wait_for_selector(FIRST_PAGE_PAGINATION, timeout=self.timeout)

    def press_find_communications_less_than_50(self):
        """If less than 50, not waiting pagination"""
        self.page.wait_for_timeout(1500)
        self.button_find_communications.click()
        self.page.wait_for_timeout(1000)
        self.page.wait_for_selector(NAYDENO_ZVONKOV, timeout=self.timeout)
        self.page.wait_for_timeout(1000)

    def assert_communications_found(self, text: str):
        expect(self.communications_found.nth(0)).to_have_text(text, timeout=self.timeout)

    def change_sort(self, sort_type):
        """Change sort"""
        self.sort.click()
        self.menu.get_by_text(sort_type).click()
        self.page.wait_for_selector(FIRST_PAGE_PAGINATION, timeout=self.timeout)

    def assert_call_date_and_time(self, text: str):
        expect(self.call_date_and_time).to_have_text(text, timeout=self.timeout)

    def fill_client_number(self, text: str):
        """Fill filter client number"""
        self.input_client_number.type(text, delay=30)
        self.page.wait_for_timeout(500)
        self.just_click.click()  # tupo click

    def fill_employee_number(self, text: str):
        """Fill filter employee number"""
        self.input_employee_number.type(text, delay=30)
        self.page.wait_for_timeout(500)
        self.just_click.click()  # tupo click

    def fill_time(self, time: str):
        """Fill exact time"""
        self.input_time.type(time, delay=30)
        self.page.wait_for_timeout(500)
        self.just_click.click()  # tupo click

    def fill_id(self, id: str):
        """Fill ID"""
        self.input_id.type(id, delay=30)
        self.page.wait_for_timeout(500)
        self.just_click.click()  # tupo click

    def fill_search_length(self, value: str):
        """Fill search length"""
        self.page.wait_for_timeout(300)
        self.input_call_duration.clear()
        self.page.wait_for_timeout(300)
        self.input_call_duration.type(value, delay=30)
        self.page.wait_for_timeout(500)
        self.just_click.click()  # tupo click

    def fill_client_dict_or_text(self, search_text: str, result_text: str):
        """Fill client dict or text"""
        self.input_client_dict_or_text.clear()
        self.input_client_dict_or_text.type(search_text, delay=30)
        self.page.wait_for_timeout(300)
        self.menu.get_by_text(result_text).click()
        self.just_click.click()  # tupo click

    def fill_employee_dict_or_text(self, search_text: str, result_text: str):
        """Fill employee dict or text"""
        self.input_employee_dict_or_text.clear()
        self.input_employee_dict_or_text.type(search_text, delay=30)
        self.page.wait_for_timeout(300)
        self.menu.get_by_text(result_text).click()
        self.just_click.click()  # tupo click

    def fill_by_tag(self, text: str):
        """Fill by tag"""
        self.page.wait_for_timeout(1000)
        self.input_by_tags.type(text, delay=30)
        self.page.wait_for_timeout(1500)
        self.menu.locator('[id*="-option-0"]').get_by_text(text, exact=True).click()
        self.just_click.click()  # tupo click
        self.page.wait_for_timeout(500)

    def press_clear_button(self):
        """Press clear button"""
        self.button_clear.click()

    def press_calls_action_button_in_list(self, number: int):
        """(...) in list"""
        self.button_calls_action.nth(number).click()
        self.page.wait_for_selector('[class*="-menu"]')

    # def click_settings(self):
    #     """Click Settings"""
    #     self.page.wait_for_selector(BUTTON_SETTINGS, timeout=self.timeout)
    #     self.page.locator(BUTTON_SETTINGS).click()
    #     self.page.wait_for_timeout(500)
    #     self.page.wait_for_selector(INPUT_LOGIN)
    #     self.page.wait_for_timeout(500)

    def expand_call(self):
        """Expand call"""
        self.page.wait_for_selector(BUTTON_EXPAND_CALL, timeout=self.timeout)
        self.page.wait_for_timeout(500)
        self.button_expand_call.click()
        self.page.wait_for_selector(ALL_COMMENTS_AREA, timeout=self.timeout)

    def press_cross_in_manual_tags(self):
        """Press + in manual tags"""
        self.page.wait_for_timeout(500)
        self.button_cross_in_manual_tags.click()
        self.page.wait_for_selector(SELECT_WITH_SEARCH_MANUAL_TAGS)

    def add_manual_tag_name(self, text: str):
        self.input_manual_tag_name.type(text, delay=30)
        self.page.wait_for_timeout(1000)

    def delete_manual_tag_from_call_header(self, number: int):
        self.page.wait_for_timeout(500)
        self.page.locator('[class*="MuiAccordionSummary-content"]').locator('[fill="#d9f7be"]').nth(number).click()
        self.page.wait_for_selector('[role="tooltip"]')
        self.page.locator('[role="tooltip"]').get_by_text("Удалить").click()
        self.page.wait_for_selector(MODAL_WINDOW)
        self.modal_window.locator(BUTTON_SUBMIT).click()
        self.page.wait_for_selector(MODAL_WINDOW, state="hidden", timeout=self.timeout)

    def delete_manual_tag_from_manual_tags(self, number: int):
        self.page.wait_for_timeout(500)
        self.page.locator('[class*="_manualGroup_"]').locator('[fill="#d9f7be"]').nth(number).click()
        self.page.wait_for_selector('[role="tooltip"]')
        self.page.locator('[role="tooltip"]').get_by_text("Удалить").click()
        self.page.wait_for_selector(MODAL_WINDOW)
        self.modal_window.locator(BUTTON_SUBMIT).click()
        self.page.wait_for_selector(MODAL_WINDOW, state="hidden", timeout=self.timeout)

    def assert_tags_have_count(self, count: int):
        expect(self.tag).to_have_count(count, timeout=self.timeout)

    def press_add_comment(self):
        self.button_add_comment.click()
        self.page.wait_for_selector('[class*="styles_textareaWrapper"]')

    def choose_option(self, option_number: int):
        self.menu.locator(f'[id$="-option-{option_number}"]').click()

    def click_submit_in_word_processing(self):
        self.page.wait_for_timeout(500)
        self.button_submit_in_word_processing.click()
        self.page.wait_for_timeout(500)










USERS_LIST = "#react-select-2-input"

# time period
YESTERDAY = '[value="yesterday"]'
WEEK = '[value="this_week"]'
MONTH = '[value="this_month"]'
YEAR = '[value="this_year"]'
ALL_TIME = '[value="all_time"]'
FIRST_DATE = '[placeholder="Начальная дата"]'
LAST_DATE = '[placeholder="Конечная дата"]'

# inputs
INPUT_PO_TEGAM = '[data-testid="filters_search_by_tags"]'
INPUT_PO_TEGAM_NEW = '//html/body/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div[4]/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/input'
#INPUT_VREMYA_ZVONKA = '[data-testid="filters_call_time_interval"]'
#INPUT_DLITELNOST_ZVONKA = '[data-testid="filters_call_duration"]'
INPUT_NOMER_CLIENTA = '[data-testid="filters_client_phone"]'
INPUT_NOMER_SOTRUDNIKA = '[data-testid="filters_operator_phone"]'
#INPUT_SLOVAR_ILI_TEXT_CLIENT = '[data-testid="filters_client_phrases"]'
#INPUT_SLOVAR_ILI_TEXT_SOTRUDNIK = '[data-testid="filters_operator_phrases"]'

INPUT_TEMPLATE_NAME = '[id="name"]'
# buttons
#BUTTON_COMMUNICATIONS = '[href*="/calls"]'
BUTTON_FIND_COMMUNICATIONS = '[data-testid="calls_btns_find"]'
BUTTON_CALLS_LIST_DOWNLOAD = '[data-testid="calls_actions_download"]'

BUTTON_ZVONKI = "button[value='calls']"
BUTTON_DOBAVIT_USLOVIE = "//button[contains(text(),'Добавить условие')]"

BUTTON_SAVE_TEMPLATE = '[data-testid="calls_btns_save-temp"]'



#BUTTON_SUBMIT = '[type="submit"]'
BUTTON_KRESTIK = '[data-testid="CloseIcon"]'


# other
ALERT = '[role="alert"]'
# MODAL_WINDOW = '[role="dialog"]'
CURRENT_TEMPLATE_NAME = '[data-testid="templatesCalls"]'
AUDIO_PLAYER = '[class*="react-audio-player"]'


CHANGE_LOGIC_OPERATOR = '//*[@id="root"]/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div[4]/div[2]/div/div[2]/div/div/div/div/div/div/div[1]/div/div/div[2]/div'

MENU = '[class*="-menu"]'


SELECT_LANGUAGE = '[data-testid="stt_language"]'
SELECT_ENGINE = '[data-testid="stt_engine"]'
SELECT_MODEL = '[data-testid="stt_model"]'






# def change_filter(filterType, elementNumber, page="page: Page"):
#     # button click
#     page.locator(".css-b62m3t-container").get_by_text("Изменить фильтры").click()  # button click
#     # choose filter with element number. first - 0, second - 1, etc
#     page.locator(".css-woue3h-menu").get_by_text(filterType, exact=True).nth(elementNumber).click()


# def choose_filter_value(filterValue, page="page: Page"):
#     # input click
#     page.locator("(//div[contains(@class,'css-12ol9ef')])[8]").first.click()
#     # choose filter value
#     page.locator(".css-1lq1yle-menu").get_by_text(filterValue).click()
#     # tupo click
#     page.locator(COMMUNICATIONS_SEARCH).click()


def press_find_communications(page="page: Page"):
    page.wait_for_timeout(1000)
    page.locator(BUTTON_FIND_COMMUNICATIONS).click()
    page.wait_for_timeout(500)
    page.wait_for_selector(NAYDENO_ZVONKOV, timeout=wait_until_visible)
    page.wait_for_timeout(500)



# def remove_filter_value(filterValue, page="page: Page"):
#     page.locator(f'[aria-label="Remove {filterValue}"]').click()
#     page.locator(COMMUNICATIONS_SEARCH).click()


# def fill_search_length(value, page="page: Page"):
#     page.wait_for_timeout(200)
#     page.locator(INPUT_CALL_DURATION).locator('[type="text"]').clear()
#     page.wait_for_timeout(200)
#     page.locator(INPUT_CALL_DURATION).locator('[type="text"]').type(value, delay=100)
#     page.wait_for_timeout(400)


# def change_sort(sortType, page="page: Page"):
#     page.locator(CHANGE_SORT).click()
#     page.get_by_text(sortType).click()
#     page.wait_for_selector(FIRST_PAGE_PAGINATION, timeout=wait_until_visible)

def press_save_template(page="page: Page"):
    page.locator(BUTTON_SAVE_TEMPLATE).click()
    page.wait_for_timeout(200)
    page.wait_for_selector(MODAL_WINDOW, timeout=wait_until_visible)

def press_rename_template(page="page: Page"):
    page.locator('[class=" css-izdlur"]').click()
    page.get_by_text("Переименовать", exact=True).click()
    page.wait_for_selector(MODAL_WINDOW, timeout=wait_until_visible)

def press_delete_template(page="page: Page"):
    page.locator('[class=" css-izdlur"]').click()
    page.get_by_text("Удалить", exact=True).click()
    page.wait_for_selector(MODAL_WINDOW, timeout=wait_until_visible)

def press_calls_action_button_in_list(number, page="page: Page"):
    page.locator(BUTTON_CALLS_ACTION).nth(number).click()
    page.wait_for_selector(MENU)

def press_calls_list_download_button(number, page="page: Page"):
    page.locator(BUTTON_CALLS_LIST_DOWNLOAD).nth(number).click()
    page.wait_for_selector(MENU)

def press_ex_button_in_expanded_call(page="page: Page"):
    page.locator('[class="MuiAccordion-region"]').locator('[aria-label="Excel экспорт"]').locator('[type="button"]').click()
    page.wait_for_selector(MODAL_WINDOW)

def click_submit_in_word_processing(page="page: Page"):
    page.wait_for_timeout(500)
    page.locator(BLOCK_WITH_BUTTON).locator(BUTTON_SUBMIT).click()
    page.wait_for_timeout(500)