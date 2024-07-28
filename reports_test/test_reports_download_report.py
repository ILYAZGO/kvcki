from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.reports import *
import pytest

'''download report'''


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

    fill_column_by_communication("0",page)

    press_generate_report(page)

    expect(page.locator('[aria-label="08-02-2022"]')).to_be_visible()
    expect(page.locator('[aria-label="09-02-2022"]')).to_be_visible()
    expect(page.locator('[aria-label="10-02-2022"]')).to_be_visible()
    expect(page.locator('[data-id="0"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("10")
    expect(page.locator('[data-id="1"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("38")
    expect(page.locator('[data-id="2"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("15")
    expect(page.locator('[data-id="3"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("63")


        # Start waiting for the download
    with page.expect_download(timeout=50000) as download_info:
            # Perform the action that initiates download
        page.get_by_text("Экспорт в Excel").click()
    download = download_info.value
    path = f'{os.getcwd()}/'

        # Wait for the download process to complete and save the downloaded file somewhere
    download.save_as(path + download.suggested_filename)

    assert os.path.isfile(path + download.suggested_filename) == True
    page.wait_for_timeout(500)
    os.remove(path + download.suggested_filename)
    page.wait_for_timeout(500)
    assert os.path.isfile(path + download.suggested_filename) == False



