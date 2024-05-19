from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.reports import *
import pytest

'''generate report with filter, 4 columns with tag and value, few checkboxes and check all that possible'''

@pytest.mark.reports
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    auth(ECOTELECOM, ECOPASS, page)
    '''go to reports'''
    page.locator(BUTTON_OT4ETI).click()
    '''click create report'''
    page.locator(BUTTON_CREATE_REPORT_IN_MENU).click()

    choose_preiod_date("01/01/2022", "31/12/2022", page=page)

    add_checklist_to_report("Второй чеклист (тоже нужен для автотестов, не трогать)", page)

    # 0

    fill_row_by_tag_list("1", "По списку тегов", "direction", page)

    # add row
    press_add_row(page)

    # 1

    fill_row_by_tag_list("2", "По списку тегов", "hangup", page)
    #page.wait_for_timeout(1000)
    #fill_row_by_tag_list("2", "По списку тегов", "CALLID", page)

    click_checkbox_row_in_tag_list("2",page)

    expect(page.locator('[data-testid="report_rows_row_2_tagListCheckbox"]')).not_to_be_checked()

    fill_column_by_communication("0", page)

    press_generate_report(page)

    #expect(page.locator('[aria-label="direction + hangup, CALLID"]')).to_be_visible()
    expect(page.locator('[aria-label="direction + hangup"]')).to_be_visible()
    expect(page.locator('[data-id="0"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("63")
    expect(page.locator('[data-id="1"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("63")

    collapse_expand_report(page)
    page.wait_for_selector(BUTTON_ADD_ROW)

    expect(page.locator('[aria-label="Remove Второй чеклист (тоже нужен для автотестов, не трогать)"]')).to_be_visible()

    # check column
    expect(page.locator('[data-testid="report_rows_row_1_select"]')).to_have_text("По списку тегов")
    expect(page.locator('[data-testid="report_rows_row_2_select"]')).to_have_text("По списку тегов")

    # check tagSelect
    expect(page.locator('[data-testid="report_rows_row_1__tagListValues"]')).to_have_text("direction")
    #expect(page.locator('[data-testid="report_rows_row_2__tagListValues"]')).to_have_text("hangupCALLID")
    expect(page.locator('[data-testid="report_rows_row_2__tagListValues"]')).to_have_text("hangup")
    # check checkboxes
    expect(page.locator('[data-testid="report_rows_row_1_tagListCheckbox"]')).to_be_checked()
    expect(page.locator('[data-testid="report_rows_row_2_tagListCheckbox"]')).not_to_be_checked()
