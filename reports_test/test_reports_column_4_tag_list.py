from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.reports import *
import pytest

'''generate report with filter, 4 columns with tag list, few checkboxes and check all that possible.'''


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
    fill_column_by_tag_list("0", "11", "asterisk_context", page=page)

    # add column
    press_add_column(page)

    # 1
    fill_column_by_tag_list("1", "CALLID", "direction", page=page)

    # add column
    press_add_column(page)

    # 2
    fill_column_by_tag_list("2", "hangup", "k", page=page)

    click_checkbox_in_tag_list("2",page)

    expect(page.locator('[data-testid="report_columns_column_2_tagListCheckbox"]')).not_to_be_checked()

    # add column
    press_add_column(page)

    # 3
    fill_column_by_tag_list("3", "multi value", "multi value number", page=page)

    click_checkbox_in_tag_list("3",page)

    expect(page.locator('[data-testid="report_columns_column_3_tagListCheckbox"]')).not_to_be_checked()

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

    # check column
    expect(page.locator('[data-testid="report_columns_column_0_select"]')).to_have_text("По списку тегов")
    expect(page.locator('[data-testid="report_columns_column_1_select"]')).to_have_text("По списку тегов")
    expect(page.locator('[data-testid="report_columns_column_2_select"]')).to_have_text("По списку тегов")
    expect(page.locator('[data-testid="report_columns_column_3_select"]')).to_have_text("По списку тегов")
    # check tagSelect
    expect(page.locator('[data-testid="report_columns_column_0__tagListValues"]')).to_have_text("11asterisk_context")
    expect(page.locator('[data-testid="report_columns_column_1__tagListValues"]')).to_have_text("CALLIDdirection")
    expect(page.locator('[data-testid="report_columns_column_2__tagListValues"]')).to_have_text("hangupk")
    expect(page.locator('[data-testid="report_columns_column_3__tagListValues"]')).to_have_text("multi valuemulti value number")

    # check checkboxes
    expect(page.locator('[data-testid="report_columns_column_0_tagListCheckbox"]')).to_be_checked()
    expect(page.locator('[data-testid="report_columns_column_1_tagListCheckbox"]')).to_be_checked()
    expect(page.locator('[data-testid="report_columns_column_2_tagListCheckbox"]')).not_to_be_checked()
    expect(page.locator('[data-testid="report_columns_column_3_tagListCheckbox"]')).not_to_be_checked()

    expect(page.locator('[data-testid="report_columns_column_2_tagListInput"]').locator('[type="text"]')).to_have_value("hangup, k")
    expect(page.locator('[data-testid="report_columns_column_3_tagListInput"]').locator('[type="text"]')).to_have_value("multi value, multi value number")