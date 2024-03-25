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

    page.locator(BUTTON_CHANGE_FILTERS).click()
    page.locator('[id="Фильтровать по числовым тегам"]').click()
    page.mouse.wheel(delta_x=0, delta_y=10000)
    page.get_by_text("По чеклистам").nth(1).click()
    page.locator(TUPO_CLICK).click()
    page.locator('[autocorrect=off]').nth(0).fill("автотест")
    page.get_by_text("Чек лист звонка (не трогать, автотест повзязан на баллы которые получаются в результате применения этого чек листа)", exact=True).click()
    page.locator('[class*="subtitle1 styles_searchTitleLeftText"]').click()

    # 0
    fill_row_by_tag_and_value("0", "Тегу и значениям", "direction", "incoming", page)

    # add column
    press_add_row(page)

    # 1

    fill_row_by_tag_and_value("1", "Тегу и значениям", "hangup", "operator", page)

    # add column
    press_add_row(page)

    # 2
    fill_row_by_tag_and_value("2", "Тегу и значениям", "CALLID", "Выбрать все", page)

    click_checkbox_row_in_tag_and_value("2",page)

    expect(page.locator('[data-testid="report_rows_row_2_tagCheckbox"]')).not_to_be_checked()

    # add column
    press_add_row(page)

    # 3
    fill_row_by_tag_and_value("3", "Тегу и значениям", "queue", "Выбрать все", page)

    click_checkbox_row_in_tag_and_value("3",page)

    expect(page.locator('[data-testid="report_rows_row_3_tagCheckbox"]')).not_to_be_checked()

    fill_column_by_communication("0", page)

    press_generate_report(page)

    expect(page.locator('[aria-label="incoming + operator + CALLID + queue"]')).to_be_visible()

    expect(page.locator('[data-id="0"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("193")
    expect(page.locator('[data-id="1"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("193")

    collapse_expand_report(page)
    page.wait_for_selector(BUTTON_ADD_ROW)

    expect(page.locator('[aria-label="Remove Чек лист звонка (не трогать, автотест повзязан на баллы которые получаются в результате применения этого чек листа)"]')).to_be_visible()

    # check column
    expect(page.locator('[data-testid="report_rows_row_0_select"]')).to_have_text("Тегу и значениям")
    expect(page.locator('[data-testid="report_rows_row_1_select"]')).to_have_text("Тегу и значениям")
    expect(page.locator('[data-testid="report_rows_row_2_select"]')).to_have_text("Тегу и значениям")
    expect(page.locator('[data-testid="report_rows_row_3_select"]')).to_have_text("Тегу и значениям")
    # check tagSelect
    expect(page.locator('[data-testid="report_rows_row_0_tagSelect"]')).to_have_text("direction")
    expect(page.locator('[data-testid="report_rows_row_1_tagSelect"]')).to_have_text("hangup")
    expect(page.locator('[data-testid="report_rows_row_2_tagSelect"]')).to_have_text("CALLID")
    expect(page.locator('[data-testid="report_rows_row_3_tagSelect"]')).to_have_text("queue")
    # check tagValues
    expect(page.locator('[data-testid="report_rows_row_0_tagValues"]')).to_have_text("incoming")
    expect(page.locator('[data-testid="report_rows_row_1_tagValues"]')).to_have_text("operator")
    expect(page.locator('[data-testid="report_rows_row_2_tagValues"]')).to_have_text("Выбрать все")
    expect(page.locator('[data-testid="report_rows_row_3_tagValues"]')).to_have_text("Выбрать все")
    # check checkboxes
    expect(page.locator('[data-testid="report_rows_row_0_tagCheckbox"]')).to_be_checked()
    expect(page.locator('[data-testid="report_rows_row_1_tagCheckbox"]')).to_be_checked()
    expect(page.locator('[data-testid="report_rows_row_2_tagCheckbox"]')).not_to_be_checked()
    expect(page.locator('[data-testid="report_rows_row_3_tagCheckbox"]')).not_to_be_checked()
