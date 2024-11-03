from playwright.sync_api import Page, expect
from pages.base_class import *

from utils.variables import wait_until_visible

BUTTON_CREATE_REPORT_IN_MENU = '[href*="/report/create"]'
BUTTON_GENERATE_REPORT = '[data-testid="reportMake"]'

class Reports(BaseClass):
    def __init__(self, page: Page):
        BaseClass.__init__(self, page)
        self.button_generate_report = page.locator(BUTTON_GENERATE_REPORT)

    def press_create_report(self):
        self.page.wait_for_selector(BUTTON_CREATE_REPORT_IN_MENU)
        self.page.locator(BUTTON_CREATE_REPORT_IN_MENU).click()
        self.page.wait_for_selector(BUTTON_GENERATE_REPORT)

    def press_generate_report(self):
        self.page.wait_for_timeout(500)
        self.button_generate_report.click()
        self.page.wait_for_selector('[data-id="0"]', timeout=self.timeout)

# time period
YESTERDAY = "button[value='yesterday']"
WEEK = "button[value='this_week']"
MONTH = "button[value='this_month']"
YEAR = "button[value='this_year']"
ALL_TIME = "button[value='all_time']"
FIRST_DATE = "//input[@placeholder='Начальная дата']"
LAST_DATE = "//input[@placeholder='Конечная дата']"

BUTTON_UPRAVLENIE_SPISKOM_OT4ETOV = '[href*="/reports"]'
BUTTON_CREATE_REPORT_IN_MANAGEMENT = '[data-testid="addUserButton"]'
BUTTON_KORZINA = '[aria-label="Удалить"]'
BUTTON_UDALIT= BUTTON_CREATE = '[data-testid="acceptButton"]'

BUTTON_SAVE_AS_NEW = '[data-testid="reportNewSave"]'
BUTTON_REPORT_UPDATE = '[data-testid="reportUpdate"]'
BUTTON_CHANGE_FILTERS = '[data-testid="report_filters_addCriterias"]'
BUTTON_COLLAPSE_EXPAND = '[class*="ShowHideCheck_checkTitle"]'
BUTTON_ADD_COLUMN = '[data-testid="report_rows_addColumn"]'
BUTTON_ADD_ROW = '[data-testid="report_rows_addRow"]'

# PO_TEGAM_SECOND = ".css-19bb58m"
# PO_TEGAM_THIRD = ".css-12ol9ef"

TUPO_CLICK = ".styles_questionTitle__WSOwz"

INPUT_REPORT_NAME = '[name="report_name"]'

BUTTON_LUPA = '[type="submit"]'

BUTTON_TAG_VALUE_IN_ADDITIONAL_PARAMS = '[data-testid="tagNameChange"]'
BUTTON_AVERAGE_NUMBER_TAG_VALUE = '[data-testid="avgNumTagChange"]'
BUTTON_CHECKLIST_POINT_IN_ADDITIONAL_PARAMS = '[data-testid="checklistChange"]'
BUTTON_CHECKLIST_POINT_PERCENT_IN_ADDITIONAL_PARAMS = '[data-testid="checklistChangePercent"]'
BUTTON_CHECKLIST_QUESTION_POINT_IN_ADDITIONAL_PARAMS = '[data-testid="checklistQuestionChange"]'
BUTTON_CHECKLIST_QUESTION_POINT_PERCENT_IN_ADDITIONAL_PARAMS = '[data-testid="checklistQuestionChangePercent"]'
BUTTON_CHECKLIST_FREQUENT_ANSWER_FOR_QUESTION_IN_ADDITIONAL_PARAMS = '[data-testid="checklistAnswerAvg"]'
BUTTON_COMMENT_IN_ADDITIONAL_PARAMS = '[data-testid="commentary"]'
CHECKBOX_COMMUNICATIONS_ADD_PARAMS = '[data-testid="show_calls_count"]'
CHECKBOX_SUM_TIME_ADD_PARAMS = '[data-testid="show_minutes"]'
CHECKBOX_PERCENTAGE_FROM_REPORT_ADD_PARAMS = '[data-testid="show_percentage"]'
CHECKBOX_PERCENTAGE_FROM_ROW_ADD_PARAMS = '[data-testid="show_percentage_from_all_calls_row"]'
CHECKBOX_PERCENTAGE_FROM_COLUMN_ADD_PARAMS = '[data-testid="show_percentage_from_all_calls_col"]'
CHECKBOX_PERCENTAGE_FROM_ROW_CELL_ADD_PARAMS = '[data-testid="show_percentage_from_sum_calls_row"]'
CHECKBOX_PERCENTAGE_FROM_COLUMN_CELL_ADD_PARAMS = '[data-testid="show_percentage_from_sum_calls_col"]'
CHECKBOX_CLIENT_TALK_TIME_ADD_PARAMS = '[data-testid="show_client_time"]'
CHECKBOX_CLIENT_TALK_TIME_PERCENT_ADD_PARAMS = '[data-testid="show_client_time_percentage"]'
CHECKBOX_OPERATOR_TALK_TIME_ADD_PARAMS = '[data-testid="show_operator_time"]'
CHECKBOX_OPERATOR_TALK_TIME_PERCENT_ADD_PARAMS = '[data-testid="show_operator_time_percentage"]'
CHECKBOX_SILENCE_DURATION_ADD_PARAMS = '[data-testid="show_silence_time"]'
CHECKBOX_SILENCE_DURATION_PERCENT_ADD_PARAMS = '[data-testid="show_silence_time_percentage"]'
CHECKBOX_CLIENTS_PHONES_ADD_PARAMS = '[data-testid="show_client_phones"]'
CHECKBOX_OPERATORS_PHONES_ADD_PARAMS = '[data-testid="show_operator_phones"]'

CHECKBOX_AVERAGE_POINT_CHECKLIST_ADD_PARAMS = '[data-testid="show_checklist_average"]'
CHECKBOX_AVERAGE_POINT_CHECKLIST_PERCENT_ADD_PARAMS = '[data-testid="show_checklist_average_percent"]'
CHECKBOX_FIRST_COMM_TIME_ADD_PARAMS = '[data-testid="show_first_call_dt"]'
CHECKBOX_LAST_COMM_TIME_ADD_PARAMS = '[data-testid="show_last_call_dt"]'

CHECKBOX_POINTS_SUM_ADD_PARAMS = '[data-testid="show_points"]'
CHECKBOX_POINTS_MAX_SUM_ADD_PARAMS = '[data-testid="show_max_points"]'

BUTTON_ADD_PARAMS_APPLY = '[data-testid="report_settings_apply"]'
BUTTON_KORZINA_IN_ADD_PARAMS = '[data-testid*="delete_btn_view_"]'

SELECT_WITH_ADDITIONAL_PARAM = '[class*="AdditionalParams_additionalSelect_"]'


def press_create_report_in_management(page="page: Page"):
    page.wait_for_timeout(500)
    page.locator(BUTTON_CREATE_REPORT_IN_MANAGEMENT).click()
    page.wait_for_selector(BUTTON_GENERATE_REPORT)

def press_report_management(page="page: Page"):
    page.wait_for_selector(BUTTON_UPRAVLENIE_SPISKOM_OT4ETOV)
    page.locator(BUTTON_UPRAVLENIE_SPISKOM_OT4ETOV).click()
    page.wait_for_selector('[role="table"]', timeout=wait_until_visible)

def press_add_column(page="page: Page"):
    page.locator(BUTTON_ADD_COLUMN).click()
    page.wait_for_timeout(500)


def press_add_row(page="page: Page"):
    page.locator(BUTTON_ADD_ROW).click()
    page.wait_for_timeout(500)


def click_checkbox_in_tag_and_value(number, page="page: Page"):
    page.locator(f'[data-testid="report_columns_column_{number}_tagCheckbox"]').click()


def click_checkbox_in_tag_list(number, page="page: Page"):
    page.locator(f'[data-testid="report_columns_column_{number}_tagListCheckbox"]').click()

def press_save_as_new(page="page: Page"):
    page.wait_for_timeout(500)
    page.locator(BUTTON_SAVE_AS_NEW).click()
    page.wait_for_selector('[class="modal-btns"]')


def press_save_current(page="page: Page"):
    page.locator(BUTTON_REPORT_UPDATE).click()
    page.wait_for_selector('[class="modal-btns"]')


def collapse_expand_report(page="page: Page"):
    page.locator(BUTTON_COLLAPSE_EXPAND).click()
    page.wait_for_timeout(500)


def change_grouping_period(period, page="page: Page"):
    page.get_by_text("По дням", exact=True).click()
    page.get_by_text(period, exact=True).click()


def delete_current_report(page="page: Page"):
    page.locator('[class=" css-izdlur"]').click()
    page.get_by_text("Удалить шаблон", exact=True).click()
    page.get_by_role("button", name="Удалить").click()


def fill_column_by_tag_and_value(number, tagName, tagValue, page="page: Page"):
    page.locator(f'[data-testid="report_columns_column_{number}_select"]').click()
    page.locator(MENU).get_by_text("Тегу и значениям", exact=True).click()
    page.wait_for_timeout(400)
    page.locator(f'[data-testid="report_columns_column_{number}_tagSelect"]').click()
    page.wait_for_timeout(400)
    page.locator(MENU).get_by_text(tagName, exact=True).click()
    page.wait_for_timeout(400)
    page.locator(f'[data-testid="report_columns_column_{number}_tagValues"]').click()
    page.wait_for_timeout(400)
    page.locator('[class*="EnhancedSelect_selectOptions"]').get_by_text(tagValue, exact=True).click()
    page.wait_for_timeout(400)
    page.locator('[class*="subtitle1 styles_searchTitleLeftText"]').click()


def fill_column_by_tag_list(number, *args, page="page: Page"):
    page.locator(f'[data-testid="report_columns_column_{number}_select"]').click()
    page.locator(MENU).get_by_text("По списку тегов", exact=True).click()
    page.locator(f'[data-testid="report_columns_column_{number}__tagListValues"]').click()
    for i in args:
        page.locator('[class*="EnhancedSelect_selectOptions"]').get_by_text(i, exact=True).click()
    page.locator('[class*="subtitle1 styles_searchTitleLeftText"]').click()


def fill_column_by_filter(number, columnName, tagName, tagValue, page="page: Page"):
    page.locator(f'[data-testid="report_columns_column_{number}_select"]').click()
    page.locator(MENU).get_by_text("Точный фильтр", exact=True).click()
    page.locator(f'[data-testid="report_columns_column_{number}_searchInput"]').locator('[type="text"]').fill(columnName)
    page.locator(f'[data-testid="report_columns_column_{number}_searchFilters"]').click()
    page.wait_for_timeout(500)
    page.locator(MENU).get_by_text(tagName, exact=True).click()
    page.locator('[class*="subtitle1 styles_searchTitleLeftText"]').click()
    page.locator('[data-testid="report_columns"]').get_by_text("Все").click()
    page.locator(MENU).get_by_text(tagValue, exact=True).click()
    page.locator('[class*="subtitle1 styles_searchTitleLeftText"]').click()


def fill_column_by_communication(number, page="page: Page"):
    page.locator(f'[data-testid="report_columns_column_{number}_select"]').click()
    page.locator(MENU).get_by_text("По количеству коммуникаций", exact=True).click()


def fill_row_by_date(number, select, time, page="page: Page"):
    page.locator(f'[data-testid="report_rows_row_{number}_select"]').click()
    page.locator(MENU).get_by_text(select, exact=True).click()
    page.locator(f'[data-testid="report_rows_row_{number}_time"]').click()
    page.locator(MENU).get_by_text(time, exact=True).click()


def fill_row_operator_phone(number, select, page="page: Page"):
    page.locator(f'[data-testid="report_rows_row_{number}_select"]').click()
    page.locator(MENU).get_by_text(select, exact=True).click()


def fill_row_without_grouping(number, select, page="page: Page"):
    page.locator(f'[data-testid="report_rows_row_{number}_select"]').click()
    page.locator(MENU).get_by_text(select, exact=True).click()


def fill_row_communications(number, select, page="page: Page"):
    page.locator(f'[data-testid="report_rows_row_{number}_select"]').click()
    page.locator('[class*="menu"]').get_by_text(select, exact=True).click()


def fill_row_by_tag_and_value(number, select, tagName, tagValue, page="page: Page"):
    page.locator(f'[data-testid="report_rows_row_{number}_select"]').click()
    page.locator(MENU).get_by_text(select, exact=True).click()
    page.wait_for_timeout(400)
    page.locator(f'[data-testid="report_rows_row_{number}_tagSelect"]').click()
    page.wait_for_timeout(400)
    page.locator(MENU).get_by_text(tagName, exact=True).click()
    page.wait_for_timeout(400)
    page.locator(f'[data-testid="report_rows_row_{number}_tagValues"]').click()
    page.wait_for_timeout(400)
    page.locator('[class*="EnhancedSelect_selectOptions"]').get_by_text(tagValue, exact=True).click()
    page.wait_for_timeout(400)
    page.locator('[class*="subtitle1 styles_searchTitleLeftText"]').click()

def fill_row_by_tag_list(number, select, tagName, page="page: Page"):
    page.locator(f'[data-testid="report_rows_row_{number}_select"]').click()
    page.locator(MENU).get_by_text(select, exact=True).click()
    page.wait_for_timeout(200)
    page.locator(f'[data-testid="report_rows_row_{number}__tagListValues"]').click()
    page.wait_for_timeout(200)
    page.locator('[class*="EnhancedSelect_selectOptions"]').get_by_text(tagName, exact=True).click()
    page.wait_for_timeout(200)
    page.locator('[class*="subtitle1 styles_searchTitleLeftText"]').click()

def click_checkbox_row_in_tag_and_value(number, page="page: Page"):
    page.locator(f'[data-testid="report_rows_row_{number}_tagCheckbox"]').click()

def click_checkbox_row_in_tag_list(number, page="page: Page"):
    page.locator(f'[data-testid="report_rows_row_{number}_tagListCheckbox"]').click()


def add_checklist_to_report(checkListName, page="page: Page"):
    page.locator(BUTTON_CHANGE_FILTERS).click()
    page.locator('[id="Фильтровать по числовым тегам"]').click()
    page.mouse.wheel(delta_x=0, delta_y=10000)
    page.get_by_text("По чеклистам").nth(1).click()
    page.locator(TUPO_CLICK).click()
    page.locator('[autocorrect=off]').nth(0).type("автотест", delay=100)
    page.wait_for_timeout(500)
    page.get_by_text(checkListName, exact=True).first.click()
    page.locator('[class*="subtitle1 styles_searchTitleLeftText"]').click()


# additional params

def click_apply_in_additional_params(page="page: Page"):
    page.locator(BUTTON_ADD_PARAMS_APPLY).click()
    page.wait_for_selector(MODAL_WINDOW, state="hidden", timeout=wait_until_visible)

def click_gear_in_rows(page="page: Page"):
    page.locator('[data-testid="report_rows_row_1_settings_btn"]').click()
    page.wait_for_selector(MODAL_WINDOW)

def click_gear_in_columns(columnNumber, page="page: Page"):
    page.locator(f'[data-testid="report_columns_column_{columnNumber}_settings_btn"]').click()
    page.wait_for_selector(MODAL_WINDOW)

def click_add_param_tag_value(page="page: Page"):
    page.locator(BUTTON_TAG_VALUE_IN_ADDITIONAL_PARAMS).click()
    page.wait_for_selector(SELECT_WITH_ADDITIONAL_PARAM)

def click_add_param_avg_number_tag_value(page="page: Page"):
    page.locator(BUTTON_AVERAGE_NUMBER_TAG_VALUE).click()
    page.wait_for_selector(SELECT_WITH_ADDITIONAL_PARAM)

def click_add_param_checklist_point(page="page: Page"):
    page.locator(BUTTON_CHECKLIST_POINT_IN_ADDITIONAL_PARAMS).click()
    page.wait_for_selector(SELECT_WITH_ADDITIONAL_PARAM)
    page.wait_for_timeout(500)

def click_add_param_checklist_point_percent(page="page: Page"):
    page.locator(BUTTON_CHECKLIST_POINT_PERCENT_IN_ADDITIONAL_PARAMS).click()
    page.wait_for_selector(SELECT_WITH_ADDITIONAL_PARAM)
    page.wait_for_timeout(500)

def click_add_param_checklist_question_point(page="page: Page"):
    page.locator(BUTTON_CHECKLIST_QUESTION_POINT_IN_ADDITIONAL_PARAMS).click()
    page.wait_for_selector(SELECT_WITH_ADDITIONAL_PARAM)
    page.wait_for_timeout(500)

def click_add_param_checklist_question_point_percent(page="page: Page"):
    page.locator(BUTTON_CHECKLIST_QUESTION_POINT_PERCENT_IN_ADDITIONAL_PARAMS).click()
    page.wait_for_selector(SELECT_WITH_ADDITIONAL_PARAM)
    page.wait_for_timeout(500)

def click_add_param_checklist_frequent_answer_for_question(page="page: Page"):
    page.locator(BUTTON_CHECKLIST_FREQUENT_ANSWER_FOR_QUESTION_IN_ADDITIONAL_PARAMS).click()
    page.wait_for_selector(SELECT_WITH_ADDITIONAL_PARAM)
    page.wait_for_timeout(500)

def click_add_param_comment(page="page: Page"):
    page.locator(BUTTON_COMMENT_IN_ADDITIONAL_PARAMS).click()
    page.wait_for_selector(SELECT_WITH_ADDITIONAL_PARAM)
    page.wait_for_timeout(500)

def type_value_to_select(value, page="page: Page"):
    page.locator(SELECT_WITH_ADDITIONAL_PARAM).locator('[type="text"]').click(force=True)
    page.wait_for_selector(MENU)
    page.wait_for_timeout(500)
    page.locator(MENU).get_by_text(value, exact=True).click()

def delete_select(page="page: Page"):
    page.locator(MODAL_WINDOW).locator(BUTTON_KORZINA_IN_ADD_PARAMS).click()
    page.wait_for_selector(SELECT_WITH_ADDITIONAL_PARAM, state="hidden")
