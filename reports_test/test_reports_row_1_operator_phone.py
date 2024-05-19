from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.reports import *
import pytest

'''generate report with filter with communications and check all that possible'''

@pytest.mark.reports
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    auth(ECOTELECOM, ECOPASS, page)
    '''go to reports'''
    page.locator(BUTTON_OT4ETI).click()
    '''click create report'''
    page.locator(BUTTON_CREATE_REPORT_IN_MENU).click()

    choose_preiod_date("01/01/2022", "31/12/2022", page)

    add_checklist_to_report("Второй чеклист (тоже нужен для автотестов, не трогать)", page)

    ''''''
    fill_row_operator_phone("1", "Номеру сотрудника", page)

    fill_column_by_communication("0", page)

    press_generate_report(page)

    expect(page.locator('[aria-label="251"]')).to_be_visible()
    expect(page.locator('[aria-label="266"]')).to_be_visible()
    expect(page.locator('[aria-label="122"]')).to_be_visible()
    expect(page.locator('[data-id="0"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("10")
    expect(page.locator('[data-id="1"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("5")
    expect(page.locator('[data-id="2"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("1")
    expect(page.locator('[data-id="3"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("4")
    expect(page.locator('[data-id="20"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("1")
    expect(page.locator('[data-id="21"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("63")

    collapse_expand_report(page)
    page.wait_for_selector(BUTTON_ADD_COLUMN)

    expect(page.locator('[aria-label="Remove Второй чеклист (тоже нужен для автотестов, не трогать)"]')).to_be_visible()
    # check row
    expect(page.locator('[data-testid="report_rows_row_1_select"]')).to_have_text("Номеру сотрудника")
    # check column
    expect(page.locator('[data-testid="report_columns_column_0_select"]')).to_have_text("По количеству коммуникаций")



