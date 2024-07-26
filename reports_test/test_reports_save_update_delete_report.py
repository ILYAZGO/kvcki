from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.reports import *
import pytest

'''create report , save , change, save current, delete'''


@pytest.mark.independent
@pytest.mark.reports
def test_example(base_url, page: Page) -> None:
    page.goto(base_url, timeout=timeout)

    auth(ECOTELECOM, ECOPASS, page)

    page.locator(BUTTON_OT4ETI).click()

    page.locator(BUTTON_CREATE_REPORT_IN_MENU).click()

    choose_preiod_date("01/01/2022", "31/12/2022", page)

    add_checklist_to_report("Второй чеклист (тоже нужен для автотестов, не трогать)", page)

    #fill_column_by_communication("0",page)

    #press_generate_report(page)

    press_save_as_new(page)

    expect(page.locator(INPUT_REPORT_NAME)).to_be_empty()
    expect(page.locator('[class="modal-btns"]').locator('[type="submit"]')).to_be_disabled(timeout=wait_until_visible)

    page.locator(INPUT_REPORT_NAME).fill("auto_test_report")

    expect(page.locator('[class="modal-btns"]').locator('[type="submit"]')).to_be_enabled(timeout=wait_until_visible)

    page.locator('[class="modal-btns"]').locator('[type="submit"]').click()

    press_generate_report(page)

    page.wait_for_selector('[data-id="0"]')


    expect(page.locator('[aria-label="08-02-2022"]')).to_be_visible()
    expect(page.locator('[aria-label="09-02-2022"]')).to_be_visible()
    expect(page.locator('[aria-label="10-02-2022"]')).to_be_visible()
    expect(page.locator('[data-id="0"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("10")
    expect(page.locator('[data-id="1"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("38")
    expect(page.locator('[data-id="2"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("15")
    expect(page.locator('[data-id="3"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("63")

    expect(page.locator('[data-testid="templatesReports"]').locator('[class*="body1"]')).to_have_text("auto_test_report")



    #collapse_expand_report(page)
    #page.wait_for_selector(BUTTON_ADD_COLUMN)

    #expect(page.locator('[aria-label="Remove Второй чеклист (тоже нужен для автотестов, не трогать)"]')).to_be_visible()

    # check column
    #expect(page.locator('[data-testid="report_columns_column_0_select"]')).to_have_text("По количеству коммуникаций")

    press_save_current(page)

    expect(page.locator(INPUT_REPORT_NAME)).to_have_value("auto_test_report")
    expect(page.locator('[class="modal-btns"]').locator('[type="submit"]')).to_be_enabled()
    expect(page.locator('[class="modal-btns"]').locator('[type="submit"]')).to_have_text("Обновить")

    page.locator('[class="modal-btns"]').locator('[type="submit"]').click()

    press_generate_report(page)

    page.wait_for_selector('[data-id="0"]')

    expect(page.locator('[data-testid="templatesReports"]').locator('[class*="body1"]')).to_have_text("auto_test_report")

    #delete report
    page.locator('[class=" css-izdlur"]').click()
    page.get_by_text("Удалить шаблон", exact=True).click()

    page.wait_for_selector('[class="modal-btns"]')

    page.get_by_text("Удалить", exact=True).click()
    page.wait_for_timeout(1000)
    expect(page.locator('[data-testid="templatesReports"]').locator('[class*="body1"]')).to_have_text("Сохраненные отчеты")





