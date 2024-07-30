import os
from playwright.sync_api import Page, expect
from utils.variables import *
from utils.dates import *
from utils.auth import auth
from pages.reports import *
import pytest
import allure


@pytest.mark.independent
@pytest.mark.reports
@allure.title("test_reports_check_dates")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_reports_check_dates")
def test_reports_check_dates(base_url, page: Page) -> None:

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with ecotelecom"):
        auth(ECOTELECOM, ECOPASS, page)

    with allure.step("Go to reports"):
        go_to_reports(page)

    with allure.step("Press (Create report)"):
        press_create_report(page)

    with allure.step("Check begin and end dates in view. today by default"):
        expect(page.locator(FIRST_DATE)).to_have_value(today)
        expect(page.locator(LAST_DATE)).to_have_value(today)

    with allure.step("Switch to yesterday"):
        page.locator(YESTERDAY).click()

    with allure.step("Check begin and end dates in view"):
        expect(page.locator(FIRST_DATE)).to_have_value(yesterday)
        expect(page.locator(LAST_DATE)).to_have_value(yesterday)

    with allure.step("Switch to week"):
        page.locator(WEEK).click()

    with allure.step("Check begin and end dates in view"):
        expect(page.locator(FIRST_DATE)).to_have_value(first_day_week_ago)
        expect(page.locator(LAST_DATE)).to_have_value(today)

    with allure.step("Switch to month"):
        page.locator(MONTH).click()

    with allure.step("Check begin and end dates in view"):
        expect(page.locator(FIRST_DATE)).to_have_value(first_day_month_ago)
        expect(page.locator(LAST_DATE)).to_have_value(today)

    with allure.step("Switch to year"):
        page.locator(YEAR).click()

    with allure.step("Check begin and end dates in view"):
        expect(page.locator(FIRST_DATE)).to_have_value(first_day_year_ago)
        expect(page.locator(LAST_DATE)).to_have_value(today)

    with allure.step("Switch to all time"):
        page.locator(ALL_TIME).click()

    with allure.step("Check begin and end dates is disabled"):
        expect(page.locator(FIRST_DATE)).to_be_disabled()
        expect(page.locator(LAST_DATE)).to_be_disabled()

@pytest.mark.independent
@pytest.mark.reports
@allure.title("test_reports_save_update_delete_report")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("create report , save , change, save current, delete")
def test_reports_save_update_delete_report(base_url, page: Page) -> None:

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with ecotelecom"):
        auth(ECOTELECOM, ECOPASS, page)

    with allure.step("Go to reports"):
        go_to_reports(page)

    with allure.step("Press (Create report)"):
        press_create_report(page)

    with allure.step("Choose period 01/01/2022-31/12/2022"):
        choose_preiod_date("01/01/2022", "31/12/2022", page)

    with allure.step("Add filter check-list : Второй чеклист (тоже нужен для автотестов, не трогать)"):
        add_checklist_to_report("Второй чеклист (тоже нужен для автотестов, не трогать)", page)

    with allure.step("Press (Save as new)"):
        press_save_as_new(page)

    with allure.step("Check that opened modal window with empty report name and button (add) disabled"):
        expect(page.locator(INPUT_REPORT_NAME)).to_be_empty()
        expect(page.locator('[class="modal-btns"]').locator('[type="submit"]')).to_be_disabled(timeout=wait_until_visible)

    with allure.step("Input report name - auto_test_report"):
        page.locator(INPUT_REPORT_NAME).fill("auto_test_report")

    with allure.step("Check that button (add) enabled"):
        expect(page.locator('[class="modal-btns"]').locator('[type="submit"]')).to_be_enabled(timeout=wait_until_visible)

    with allure.step("Press (save) button"):
        page.locator('[class="modal-btns"]').locator('[type="submit"]').click()

    with allure.step("Press generate report"):
        press_generate_report(page)

    with allure.step("Check that report generated"):
        expect(page.locator('[aria-label="08-02-2022"]')).to_be_visible()
        expect(page.locator('[aria-label="09-02-2022"]')).to_be_visible()
        expect(page.locator('[aria-label="10-02-2022"]')).to_be_visible()
        expect(page.locator('[data-id="0"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("10")
        expect(page.locator('[data-id="1"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("38")
        expect(page.locator('[data-id="2"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("15")
        expect(page.locator('[data-id="3"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("63")

        expect(page.locator('[data-testid="templatesReports"]').locator('[class*="body1"]')).to_have_text("auto_test_report")

    with allure.step("Press (save current)"):
        press_save_current(page)

    with allure.step("Check that modal window have report name and (add) button enabled"):
        expect(page.locator(INPUT_REPORT_NAME)).to_have_value("auto_test_report")
        expect(page.locator('[class="modal-btns"]').locator('[type="submit"]')).to_be_enabled()
        expect(page.locator('[class="modal-btns"]').locator('[type="submit"]')).to_have_text("Обновить")

    with allure.step("Press (save) button"):
        page.locator('[class="modal-btns"]').locator('[type="submit"]').click()

    with allure.step("Press generate report"):
        press_generate_report(page)

    with allure.step("Check that report name not changed"):
        expect(page.locator('[data-testid="templatesReports"]').locator('[class*="body1"]')).to_have_text("auto_test_report")

    with allure.step("Delete report"):
        page.locator('[class=" css-izdlur"]').click()
        page.get_by_text("Удалить шаблон", exact=True).click()

        page.wait_for_selector('[class="modal-btns"]')

        page.get_by_text("Удалить", exact=True).click()
        page.wait_for_timeout(900)

    with allure.step("Check that report deleted"):
        expect(page.locator('[data-testid="templatesReports"]').locator('[class*="body1"]')).to_have_text("Сохраненные отчеты")


@pytest.mark.independent
@pytest.mark.reports
@allure.title("test_reports_download_report")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_reports_download_report")
def test_reports_download_report(base_url, page: Page) -> None:

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with ecotelecom"):
        auth(ECOTELECOM, ECOPASS, page)

    with allure.step("Go to reports"):
        go_to_reports(page)

    with allure.step("Press (Create report)"):
        press_create_report(page)

    with allure.step("Choose period 01/01/2022-31/12/2022"):
        choose_preiod_date("01/01/2022", "31/12/2022", page)

    with allure.step("Add filter check-list : Второй чеклист (тоже нужен для автотестов, не трогать)"):
        add_checklist_to_report("Второй чеклист (тоже нужен для автотестов, не трогать)", page)

    with allure.step("Press generate report"):
        press_generate_report(page)

    with allure.step("Check that report created"):
        expect(page.locator('[aria-label="08-02-2022"]')).to_be_visible()
        expect(page.locator('[aria-label="09-02-2022"]')).to_be_visible()
        expect(page.locator('[aria-label="10-02-2022"]')).to_be_visible()
        expect(page.locator('[data-id="0"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("10")
        expect(page.locator('[data-id="1"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("38")
        expect(page.locator('[data-id="2"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("15")
        expect(page.locator('[data-id="3"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("63")

    with allure.step("Press (Export to Excel) and wait until file will be saved"):
        # Start waiting for the download
        with page.expect_download(timeout=wait_until_visible) as download_info:
            # Perform the action that initiates download
            page.get_by_text("Экспорт в Excel").click()
        download = download_info.value
        path = f'{os.getcwd()}/'

        # Wait for the download process to complete and save the downloaded file somewhere
        download.save_as(path + download.suggested_filename)

    with allure.step("Check that file was downloaded"):
        assert os.path.isfile(path + download.suggested_filename) == True
        page.wait_for_timeout(500)

    with allure.step("Remove downloaded file"):
        os.remove(path + download.suggested_filename)
        page.wait_for_timeout(500)

    with allure.step("Check that file was removed"):
        assert os.path.isfile(path + download.suggested_filename) == False


@pytest.mark.independent
@pytest.mark.reports
@allure.title("test_reports_management_check_search")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_reports_management_check_search")
def test_reports_management_check_search(base_url, page: Page) -> None:

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with ecotelecom"):
        auth(ECOTELECOM, ECOPASS, page)

    with allure.step("Go to reports"):
        go_to_reports(page)

    with allure.step("Type Ntcn in searchstring in menu an press magnifier"):
        page.locator(INPUT_SEARCH).fill("Ntcn")
        page.locator(BUTTON_LUPA).click()

    with allure.step("Check that search was successful"):
        expect(page.locator(INPUT_SEARCH)).to_have_value("Ntcn")
        expect(page.get_by_text("Ntcn")).to_have_count(1)


@pytest.mark.independent
@pytest.mark.reports
@allure.title("test_reports_row_1_without_grouping")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_reports_row_1_without_grouping")
def test_reports_row_1_without_grouping(base_url, page: Page) -> None:

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with ecotelecom"):
        auth(ECOTELECOM, ECOPASS, page)

    with allure.step("Go to reports"):
        go_to_reports(page)

    with allure.step("Press (Create report)"):
        press_create_report(page)

    with allure.step("Choose period 01/01/2022-31/12/2022"):
        choose_preiod_date("01/01/2022", "31/12/2022", page)

    with allure.step("Add filter check-list : Второй чеклист (тоже нужен для автотестов, не трогать)"):
        add_checklist_to_report("Второй чеклист (тоже нужен для автотестов, не трогать)", page)

    with allure.step("Make row without grouping"):
        fill_row_without_grouping("1", "Без группировки", page)

    #fill_column_by_communication("0", page)

    with allure.step("Press generate report"):
        press_generate_report(page)

    with allure.step("Check that report generated"):
        expect(page.locator('[aria-label="Без группировки"]')).to_have_count(2)

        expect(page.locator('[data-id="0"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("63")
        expect(page.locator('[data-id="1"]').locator('[data-field="row_sum_calls_count"]')).to_have_text("63")

    with allure.step("Expand report parameters"):
        collapse_expand_report(page)
        page.wait_for_selector(BUTTON_ADD_COLUMN)

    with allure.step("Check checklist exists"):
        expect(page.locator('[aria-label="Remove Второй чеклист (тоже нужен для автотестов, не трогать)"]')).to_be_visible()

    with allure.step("Check row is without grouping"):
        expect(page.locator('[data-testid="report_rows_row_1_select"]')).to_have_text("Без группировки")

    with allure.step("Check column is by communications"):
        expect(page.locator('[data-testid="report_columns_column_0_select"]')).to_have_text("По количеству коммуникаций")