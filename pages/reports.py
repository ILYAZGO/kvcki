
# time period
YESTERDAY = "button[value='yesterday']"
WEEK = "button[value='this_week']"
MONTH = "button[value='this_month']"
YEAR = "button[value='this_year']"
ALL_TIME = "button[value='all_time']"
FIRST_DATE = "//input[@placeholder='Начальная дата']"
LAST_DATE = "//input[@placeholder='Конечная дата']"

BUTTON_OT4ETI = '[value="reports"]'
BUTTON_UPRAVLENIE_SPISKOM_OT4ETOV = '[href*="/reports"]'
BUTTON_CREATE_REPORT_IN_MANAGEMENT = '[data-testid="addUserButton"]'
BUTTON_KORZINA = '[aria-label="Удалить"]'
BUTTON_UDALIT = '[data-testid="acceptButton"]'
BUTTON_CREATE_REPORT_IN_MENU = '[href*="/report/create"]'

BUTTON_GENERATE_REPORT = '[data-testid="reportMake"]'
BUTTON_SAVE_AS_NEW = '[data-testid="reportNewSave"]'
BUTTON_REPORT_UPDATE = '[data-testid="reportUpdate"]'
BUTTON_CHANGE_FILTERS = '[data-testid="report_filters_addCriterias"]'
BUTTON_COLLAPSE_EXPAND = '[class*="ShowHideCheck_checkTitle"]'
BUTTON_ADD_COLUMN = '[data-testid="report_rows_addColumn"]'
BUTTON_ADD_ROW = '[data-testid="report_rows_addRow"]'

PO_TEGAM_SECOND = ".css-19bb58m"
PO_TEGAM_THIRD = ".css-12ol9ef"

TUPO_CLICK = ".styles_questionTitle__WSOwz"

INPUT_REPORT_NAME = '[name="report_name"]'
INPUT_SEARCH = '[name="searchString"]'
BUTTON_LUPA = '[type="submit"]'


def choose_preiod_date(firstDate, lastDate, page="page: Page"):
    page.wait_for_selector('[data-testid="reportMake"]')
    page.locator(FIRST_DATE).click()
    page.locator(FIRST_DATE).fill(firstDate)
    page.wait_for_timeout(500)
    page.locator(LAST_DATE).click()
    page.locator(LAST_DATE).fill(lastDate)
    page.wait_for_timeout(500)
    page.keyboard.press("Enter")
    page.wait_for_timeout(500)


def press_add_column(page="page: Page"):
    page.locator(BUTTON_ADD_COLUMN).click()

def press_add_row(page="page: Page"):
    page.locator(BUTTON_ADD_ROW).click()



def click_checkbox_in_tag_and_value(number, page="page: Page"):
    page.locator(f'[data-testid="report_columns_column_{number}_tagCheckbox"]').click()

def click_checkbox_in_tag_list(number, page="page: Page"):
    page.locator(f'[data-testid="report_columns_column_{number}_tagListCheckbox"]').click()


def press_generate_report(page="page: Page"):
    page.locator(BUTTON_GENERATE_REPORT).click()
    page.wait_for_selector('[data-id="0"]')

def press_save_as_new(page="page: Page"):
    page.locator(BUTTON_SAVE_AS_NEW).click()
    page.wait_for_selector('[class="modal-btns"]')

def press_save_current(page="page: Page"):
    page.locator(BUTTON_REPORT_UPDATE).click()
    page.wait_for_selector('[class="modal-btns"]')


def collapse_expand_report(page="page: Page"):
    page.locator(BUTTON_COLLAPSE_EXPAND).click()


def change_grouping_period(period, page="page: Page"):
    page.get_by_text("По дням", exact=True).click()
    page.get_by_text(period, exact=True).click()


def delete_current_report(page="page: Page"):
    page.locator('[class=" css-izdlur"]').click()
    page.get_by_text("Удалить шаблон", exact=True).click()
    page.get_by_role("button", name="Удалить").click()


def fill_column_by_tag_and_value(number, tagName, tagValue, page="page: Page"):
    page.locator(f'[data-testid="report_columns_column_{number}_select"]').click()
    page.locator('[class*="menu"]').get_by_text("Тегу и значениям", exact=True).click()
    page.wait_for_timeout(200)
    page.locator(f'[data-testid="report_columns_column_{number}_tagSelect"]').click()
    page.wait_for_timeout(200)
    page.locator('[class*="menu"]').get_by_text(tagName, exact=True).click()
    page.wait_for_timeout(200)
    page.locator(f'[data-testid="report_columns_column_{number}_tagValues"]').click()
    page.wait_for_timeout(200)
    page.locator('[class*="menu"]').get_by_text(tagValue, exact=True).click()
    page.wait_for_timeout(200)
    page.locator('[class*="subtitle1 styles_searchTitleLeftText"]').click()


def fill_column_by_tag_list(number, *args, page="page: Page"):
    page.locator(f'[data-testid="report_columns_column_{number}_select"]').click()
    page.locator('[class*="menu"]').get_by_text("По списку тегов", exact=True).click()
    page.locator(f'[data-testid="report_columns_column_{number}__tagListValues"]').click()
    for i in args:
        page.locator('[class*="menu"]').get_by_text(i, exact=True).click()
    page.locator('[class*="subtitle1 styles_searchTitleLeftText"]').click()

def fill_column_by_filter(number, columnName, tagName, tagValue, page="page: Page"):
    page.locator(f'[data-testid="report_columns_column_{number}_select"]').click()
    page.locator('[class*="menu"]').get_by_text("Точный фильтр", exact=True).click()
    page.locator(f'[data-testid="report_columns_column_{number}_searchInput"]').locator('[type="text"]').fill(columnName)
    page.locator(f'[data-testid="report_columns_column_{number}_searchFilters"]').click()
    page.wait_for_timeout(300)
    page.locator('[class*="menu"]').get_by_text(tagName, exact=True).click()
    page.locator('[class*="subtitle1 styles_searchTitleLeftText"]').click()
    page.locator('[data-testid="report_columns"]').get_by_text("Все").click()
    page.locator('[class*="menu"]').get_by_text(tagValue, exact=True).click()
    page.locator('[class*="subtitle1 styles_searchTitleLeftText"]').click()

def fill_column_by_communication(number, page="page: Page"):
    page.locator(f'[data-testid="report_columns_column_{number}_select"]').click()
    page.locator('[class*="menu"]').get_by_text("По количеству коммуникаций", exact=True).click()

def fill_row_by_date(number, select, time, page="page: Page"):
    page.locator(f'[data-testid="report_rows_row_{number}_select"]').click()
    page.locator('[class*="menu"]').get_by_text(select, exact=True).click()
    page.locator(f'[data-testid="report_rows_row_{number}_time"]').click()
    page.locator('[class*="menu"]').get_by_text(time, exact=True).click()

def fill_row_operator_phone(number, select, page="page: Page"):
    page.locator(f'[data-testid="report_rows_row_{number}_select"]').click()
    page.locator('[class*="menu"]').get_by_text(select, exact=True).click()


def fill_row_without_grouping(number, select, page="page: Page"):
    page.locator(f'[data-testid="report_rows_row_{number}_select"]').click()
    page.locator('[class*="menu"]').get_by_text(select, exact=True).click()

def fill_row_communications(number, select, page="page: Page"):
    page.locator(f'[data-testid="report_rows_row_{number}_select"]').click()
    page.locator('[class*="menu"]').get_by_text(select, exact=True).click()


def fill_row_by_tag_and_value(number, select, tagName, tagValue, page="page: Page"):
    page.locator(f'[data-testid="report_rows_row_{number}_select"]').click()
    page.locator('[class*="menu"]').get_by_text(select, exact=True).click()
    page.wait_for_timeout(200)
    page.locator(f'[data-testid="report_rows_row_{number}_tagSelect"]').click()
    page.wait_for_timeout(200)
    page.locator('[class*="menu"]').get_by_text(tagName, exact=True).click()
    page.wait_for_timeout(200)
    page.locator(f'[data-testid="report_rows_row_{number}_tagValues"]').click()
    page.wait_for_timeout(200)
    page.locator('[class*="menu"]').get_by_text(tagValue, exact=True).click()
    page.wait_for_timeout(200)
    page.locator('[class*="subtitle1 styles_searchTitleLeftText"]').click()

def click_checkbox_row_in_tag_and_value(number, page="page: Page"):
    page.locator(f'[data-testid="report_rows_row_{number}_tagCheckbox"]').click()


def add_checklist_to_report(checkListName, page="page: Page"):
    page.locator(BUTTON_CHANGE_FILTERS).click()
    page.locator('[id="Фильтровать по числовым тегам"]').click()
    page.mouse.wheel(delta_x=0, delta_y=10000)
    page.get_by_text("По чеклистам").nth(1).click()
    page.locator(TUPO_CLICK).click()
    page.locator('[autocorrect=off]').nth(0).fill("автотест")
    page.get_by_text(checkListName, exact=True).click()
    page.locator('[class*="subtitle1 styles_searchTitleLeftText"]').click()