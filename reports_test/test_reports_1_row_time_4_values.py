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

    page.locator(BUTTON_CHANGE_FILTERS).click()
    page.locator('[id="Фильтровать по числовым тегам"]').click()
    page.mouse.wheel(delta_x=0, delta_y=10000)
    page.get_by_text("По чеклистам").nth(1).click()
    page.locator(TUPO_CLICK).click()
    page.locator('[autocorrect=off]').nth(0).fill("чеклист")
    page.get_by_text("Второй чеклист (тоже нужен для автотестов, не трогать)", exact=True).click()
    page.locator('[class*="subtitle1 styles_searchTitleLeftText"]').click()

    '''value 0'''
    fill_row_by_date("0", "Времени", "По дням", page)

    fill_column_by_communication("0", page)

    press_generate_report(page)

    expect(page.locator('[aria-label="08-02-2022"]')).to_be_visible()
    expect(page.locator('[aria-label="09-02-2022"]')).to_be_visible()
    expect(page.locator('[aria-label="10-02-2022"]')).to_be_visible()
    expect(page.locator('[data-id="0"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("10")
    expect(page.locator('[data-id="1"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("38")
    expect(page.locator('[data-id="2"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("15")
    expect(page.locator('[data-id="3"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("63")

    collapse_expand_report(page)
    page.wait_for_selector(BUTTON_ADD_COLUMN)

    expect(page.locator('[aria-label="Remove Второй чеклист (тоже нужен для автотестов, не трогать)"]')).to_be_visible()
    # check row
    expect(page.locator('[data-testid="report_rows_row_0_select"]')).to_have_text("Времени")
    expect(page.locator('[data-testid="report_rows_row_0_time"]')).to_have_text("По дням")
    # check column
    expect(page.locator('[data-testid="report_columns_column_0_select"]')).to_have_text("По количеству коммуникаций")

    '''value 1'''
    fill_row_by_date("0", "Времени", "По неделям", page)

    press_generate_report(page)

    expect(page.locator('[aria-label="6 неделя, 2022"]')).to_be_visible()
    expect(page.locator('[data-id="0"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("63")
    expect(page.locator('[data-id="1"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("63")

    collapse_expand_report(page)
    page.wait_for_selector(BUTTON_ADD_COLUMN)

    expect(page.locator('[aria-label="Remove Второй чеклист (тоже нужен для автотестов, не трогать)"]')).to_be_visible()
    # check row
    expect(page.locator('[data-testid="report_rows_row_0_select"]')).to_have_text("Времени")
    expect(page.locator('[data-testid="report_rows_row_0_time"]')).to_have_text("По неделям")
    # check column
    expect(page.locator('[data-testid="report_columns_column_0_select"]')).to_have_text("По количеству коммуникаций")

    '''value 2'''
    fill_row_by_date("0", "Времени", "По месяцам", page)

    press_generate_report(page)

    expect(page.locator('[aria-label="02-2022"]')).to_be_visible()
    expect(page.locator('[data-id="0"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("63")
    expect(page.locator('[data-id="1"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("63")

    collapse_expand_report(page)
    page.wait_for_selector(BUTTON_ADD_COLUMN)

    expect(page.locator('[aria-label="Remove Второй чеклист (тоже нужен для автотестов, не трогать)"]')).to_be_visible()
    # check row
    expect(page.locator('[data-testid="report_rows_row_0_select"]')).to_have_text("Времени")
    expect(page.locator('[data-testid="report_rows_row_0_time"]')).to_have_text("По месяцам")
    # check column
    expect(page.locator('[data-testid="report_columns_column_0_select"]')).to_have_text("По количеству коммуникаций")

    '''value 3'''
    fill_row_by_date("0", "Времени", "По часам", page)

    press_generate_report(page)

    expect(page.locator('[aria-label="08-02-2022 10:00 - 11:00"]')).to_be_visible()
    expect(page.locator('[data-id="0"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("4")
    expect(page.locator('[data-id="1"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("3")
    expect(page.locator('[data-id="2"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("2")
    expect(page.locator('[data-id="3"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("1")
    expect(page.locator('[data-id="4"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("3")
    expect(page.locator('[data-id="17"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("7")
    expect(page.locator('[data-id="18"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("63")

    collapse_expand_report(page)
    page.wait_for_selector(BUTTON_ADD_COLUMN)

    expect(page.locator('[aria-label="Remove Второй чеклист (тоже нужен для автотестов, не трогать)"]')).to_be_visible()
    # check row
    expect(page.locator('[data-testid="report_rows_row_0_select"]')).to_have_text("Времени")
    expect(page.locator('[data-testid="report_rows_row_0_time"]')).to_have_text("По часам")
    # check column
    expect(page.locator('[data-testid="report_columns_column_0_select"]')).to_have_text("По количеству коммуникаций")

