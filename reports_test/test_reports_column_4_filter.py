from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.reports import *
import pytest

'''generate report with filter, 4 columns with filter and check all that possible'''


@pytest.mark.independent
@pytest.mark.reports
def test_example(base_url, page: Page) -> None:
    page.goto(base_url, timeout=wait_until_visible)
    '''login'''
    auth(ECOTELECOM, ECOPASS, page)
    '''go to reports'''
    page.locator(BUTTON_OT4ETI).click()
    '''click create report'''
    page.locator(BUTTON_CREATE_REPORT_IN_MENU).click()

    choose_preiod_date("01/01/2022", "31/12/2022", page)

    add_checklist_to_report("Второй чеклист (тоже нужен для автотестов, не трогать)", page)

    # 0
    fill_column_by_filter("0", "zero", "test tag", "test q", page)

    # add column
    press_add_column(page)

    # 1
    fill_column_by_filter("1", "first", "Клиент-должность", "Монтажник Восток", page)

    # add column
    press_add_column(page)

    # 2
    fill_column_by_filter("2", "second", "Должность", "Бухгалтер", page)

    # add column
    press_add_column(page)

    # 3
    fill_column_by_filter("3", "third", "Клиент", "Customer", page)

    press_generate_report(page)

    expect(page.locator('[aria-label="08-02-2022"]')).to_be_visible()
    expect(page.locator('[aria-label="09-02-2022"]')).to_be_visible()
    expect(page.locator('[aria-label="10-02-2022"]')).to_be_visible()
    expect(page.locator('[data-id="0"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("5")
    expect(page.locator('[data-id="1"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("8")
    expect(page.locator('[data-id="2"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("6")
    expect(page.locator('[data-id="3"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("19")

    collapse_expand_report(page)
    page.wait_for_selector(BUTTON_ADD_COLUMN)

    expect(page.locator('[aria-label="Remove Второй чеклист (тоже нужен для автотестов, не трогать)"]')).to_be_visible()

    # check column
    expect(page.locator('[data-testid="report_columns_column_0_select"]')).to_have_text("Точный фильтр")
    expect(page.locator('[data-testid="report_columns_column_1_select"]')).to_have_text("Точный фильтр")
    expect(page.locator('[data-testid="report_columns_column_2_select"]')).to_have_text("Точный фильтр")
    expect(page.locator('[data-testid="report_columns_column_3_select"]')).to_have_text("Точный фильтр")
    # check tagSelect
    expect(page.locator('[data-testid="report_columns_column_0_searchInput"]').locator('[type="text"]')).to_have_value("zero")
    expect(page.locator('[data-testid="report_columns_column_1_searchInput"]').locator('[type="text"]')).to_have_value("first")
    expect(page.locator('[data-testid="report_columns_column_2_searchInput"]').locator('[type="text"]')).to_have_value("second")
    expect(page.locator('[data-testid="report_columns_column_3_searchInput"]').locator('[type="text"]')).to_have_value("third")

    # check tags
    expect(page.locator('[data-testid="report_columns"]').get_by_text("test q")).to_be_visible()
    expect(page.locator('[data-testid="report_columns"]').get_by_text("Монтажник Восток")).to_be_visible()
    expect(page.locator('[data-testid="report_columns"]').get_by_text("Бухгалтер")).to_be_visible()
    expect(page.locator('[data-testid="report_columns"]').get_by_text("Customer")).to_be_visible()

