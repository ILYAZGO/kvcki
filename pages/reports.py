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
BUTTON_CREATE_REPORT_IN_MENU = '[href*="create"]'

PO_TEGAM_SECOND = ".css-19bb58m"
PO_TEGAM_THIRD = ".css-12ol9ef"

TUPO_CLICK = ".styles_questionTitle__WSOwz"

INPUT_REPORT_NAME = '[name="report_name"]'
INPUT_SEARCH = '[name="searchString"]'
BUTTON_LUPA = '[type="submit"]'


def change_grouping_period(period, page="page: Page"):
    page.get_by_text("По дням", exact=True).click()
    page.get_by_text(period, exact=True).click()

def delete_current_report(page="page: Page"):
    page.locator('[class=" css-izdlur"]').click()
    page.get_by_text("Удалить шаблон", exact=True).click()
    page.get_by_role("button", name="Удалить").click()