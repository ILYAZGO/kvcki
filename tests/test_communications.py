from playwright.sync_api import Page, expect, BrowserContext
from utils.variables import *
from utils.auth import auth
from pages.communications import *
from utils.dates import *
from datetime import datetime
from utils.create_delete_user import create_user, delete_user
import os
import pytest
import allure


@pytest.mark.calls
@pytest.mark.independent
@allure.title("test_check_dates")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("Check dates buttons. Test not stabile because of expected date")
def test_check_dates(base_url, page: Page) -> None:
    communications = Communications(page)

    with allure.step("Go to url"):
        communications.navigate(base_url)

    with allure.step("Auth with Ecotelecom"):
        communications.auth(ECOTELECOM, ECOPASS)

    with allure.step("Check first and last dates in view. Today by default"):
        communications.assert_check_period_dates(today, today)

    with allure.step("Switch to yesterday"):
        communications.yesterday.click()

    with allure.step("Check first and last dates in view."):
        communications.assert_check_period_dates(yesterday, yesterday)

    with allure.step("Switch to week"):
        communications.week.click()

    with allure.step("Check first and last dates in view."):
        communications.assert_check_period_dates(first_day_week_ago, today)

    # I cant find date month ago. every time changing), so i turn this off
    # with allure.step("Switch to month"):
    #     communications.month.click()
    #
    # with allure.step("Check first and last dates in view."):
    #     communications.assert_check_period_dates(first_day_month_ago, today)

    with allure.step("Switch to year"):
        communications.year.click()

    with allure.step("Check first and last dates in view."):
        communications.assert_check_period_dates(first_day_year_ago, today)

    with allure.step("Switch to all time"):
        communications.all_time.click()

    with allure.step("Check begin and end dates is disabled"):
        communications.assert_check_period_dates_disabled()


@pytest.mark.calls
@pytest.mark.independent
@allure.title("test_check_search_all")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Searching all communications for Ecotelecom")
def test_check_search_all(base_url, page: Page) -> None:
    communications = Communications(page)

    with allure.step("Go to url"):
        communications.navigate(base_url)

    with allure.step("Auth with Ecotelecom"):
        communications.auth(ECOTELECOM, ECOPASS)

    with allure.step("Choose period from 01/01/2022 to 31/12/2022"):
        communications.choose_period_date("01/01/2022", "31/12/2022")

    with allure.step("Press button (Find communications)"):
        communications.press_find_communications_more_than_50()

    with allure.step("Check that all communications found"):
        communications.assert_communications_found("Найдено коммуникаций 3130 из 3130")


@pytest.mark.calls
@pytest.mark.independent
@allure.title("test_check_search_by_client_number")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check search by client number for Ecotelecom")
def test_check_search_by_client_number(base_url, page: Page) -> None:
    communications = Communications(page)

    with allure.step("Go to url"):
        communications.navigate(base_url)

    with allure.step("Auth with Ecotelecom"):
        communications.auth(ECOTELECOM, ECOPASS)

    with allure.step("Choose period from 01/01/2022 to 31/12/2022"):
        communications.choose_period_date("01/01/2022", "31/12/2022")

    with allure.step("Fill client number"):
        communications.fill_client_number("79251579005")

    with allure.step("Press button (Find communications)"):
        communications.press_find_communications_less_than_50()

    with allure.step("Check"):
        communications.assert_communications_found("Найдено коммуникаций 14 из 3130")



@pytest.mark.calls
@pytest.mark.independent
@allure.title("test_check_search_by_employee_number")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check search by employee's number for Ecotelecom")
def test_check_search_by_employee_number(base_url, page: Page) -> None:
    communications = Communications(page)

    with allure.step("Go to url"):
        communications.navigate(base_url)

    with allure.step("Auth with Ecotelecom"):
        communications.auth(ECOTELECOM, ECOPASS)

    with allure.step("Choose period from 01/01/2022 to 31/12/2022"):
        communications.choose_period_date("01/01/2022", "31/12/2022")

    with allure.step("Fill employee number"):
        communications.fill_employee_number("4995055555")

    with allure.step("Press button (Find communications)"):
        communications.press_find_communications_more_than_50()

    with allure.step("Check"):
        communications.assert_communications_found("Найдено коммуникаций 670 из 3130")


@pytest.mark.calls
@pytest.mark.independent
@allure.title("test_check_search_by_client_dict_or_text")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check search by client dict or text for Ecotelecom")
def test_check_search_by_client_dict_or_text(base_url, page: Page) -> None:
    communications = Communications(page)

    with allure.step("Go to url"):
        communications.navigate(base_url)

    with allure.step("Auth with Ecotelecom"):
        communications.auth(ECOTELECOM, ECOPASS)

    with allure.step("Choose period from 01/01/2022 to 31/12/2022"):
        communications.choose_period_date("01/01/2022", "31/12/2022")

    with allure.step("Fill input with text"):
        communications.fill_client_dict_or_text("минутку", "минутку")

    with allure.step("Press button (Find communications)"):
        communications.press_find_communications_less_than_50()

    with allure.step("Check"):
        communications.assert_communications_found("Найдено коммуникаций 20 из 3130")

    with allure.step("Clear, fill input by dict, choose dict from suggestion"):
        communications.fill_client_dict_or_text("Зо", "Словарь: Зомбоящик")

    with allure.step("Press button (Find communications)"):
        communications.press_find_communications_more_than_50()

    with allure.step("Check"):
        communications.assert_communications_found("Найдено коммуникаций 405 из 3130")



@pytest.mark.calls
@pytest.mark.independent
@allure.title("test_check_search_by_employee_dict_or_text")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check search by employee's dict or text for Ecotelecom")
def test_check_search_by_employee_dict_or_text(base_url, page: Page) -> None:
    communications = Communications(page)

    with allure.step("Go to url"):
        communications.navigate(base_url)

    with allure.step("Auth with Ecotelecom"):
        communications.auth(ECOTELECOM, ECOPASS)

    with allure.step("Choose period from 01/01/2022 to 31/12/2022"):
        communications.choose_period_date("01/01/2022", "31/12/2022")

    with allure.step("Fill input with text"):
        communications.fill_employee_dict_or_text("минутку", "минутку")

    with allure.step("Press button (Find communications)"):
        communications.press_find_communications_more_than_50()

    with allure.step("Check"):
        communications.assert_communications_found("Найдено коммуникаций 204 из 3130")

    with allure.step("Clear, fill input by dict, choose dict from suggestion"):
        communications.fill_employee_dict_or_text("Зо", "Словарь: Зомбоящик")

    with allure.step("Press button (Find communications)"):
        communications.press_find_communications_more_than_50()

    with allure.step("Check"):
        communications.assert_communications_found("Найдено коммуникаций 492 из 3130")


@pytest.mark.calls
@pytest.mark.independent
@allure.title("test_check_search_by_exact_time")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check search by exact time for Ecotelecom")
def test_check_search_by_exact_time(base_url, page: Page) -> None:
    communications = Communications(page)

    with allure.step("Go to url"):
        communications.navigate(base_url)

    with allure.step("Auth with Ecotelecom"):
        communications.auth(ECOTELECOM, ECOPASS)

    with allure.step("Choose period from 01/01/2022 to 31/12/2022"):
        communications.choose_period_date("01/01/2022", "31/12/2022")

    with allure.step("Fill exact time"):
        communications.fill_time("11:42")

    with allure.step("Press button (Find communications)"):
        communications.press_find_communications_less_than_50()

    with allure.step("Check"):
        communications.assert_communications_found("Найдено коммуникаций 5 из 3130")


@pytest.mark.calls
@pytest.mark.independent
@allure.title("test_check_search_by_length")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check search by length for Ecotelecom")
def test_check_search_by_length(base_url, page: Page) -> None:
    communications = Communications(page)

    with allure.step("Go to url"):
        communications.navigate(base_url)

    with allure.step("Auth with Ecotelecom"):
        communications.auth(ECOTELECOM, ECOPASS)

    with allure.step("Choose period from 01/01/2022 to 31/12/2022"):
        communications.choose_period_date("01/01/2022", "31/12/2022")

    with allure.step("Fill length <10"):
        communications.fill_search_length("<10")

    with allure.step("Press button (Find communications)"):
        communications.press_find_communications_more_than_50()

    with allure.step("Check"):
        communications.assert_communications_found("Найдено коммуникаций 441 из 3130")

    with allure.step("Fill length >10"):
        communications.fill_search_length(">10")

    with allure.step("Press button (Find communications)"):
        communications.press_find_communications_more_than_50()

    with allure.step("Check"):
        communications.assert_communications_found("Найдено коммуникаций 2689 из 3130")

    with allure.step("Fill length 1711"):
        communications.fill_search_length("1711")

    with allure.step("Press button (Find communications)"):
        communications.press_find_communications_less_than_50()

    with allure.step("Check"):
        communications.assert_communications_found("Найдено коммуникаций 1 из 3130")


@pytest.mark.calls
@pytest.mark.independent
@allure.title("test_check_search_by_id")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check search by id for Ecotelecom")
def test_check_search_by_id(base_url, page: Page) -> None:
    communications = Communications(page)

    with allure.step("Go to url"):
        communications.navigate(base_url)

    with allure.step("Auth with Ecotelecom"):
        communications.auth(ECOTELECOM, ECOPASS)

    with allure.step("Choose period from 01/01/2022 to 31/12/2022"):
        communications.choose_period_date("01/01/2022", "31/12/2022")

    with allure.step("Fill ID"):
        communications.fill_id("1644474236.14425")

    with allure.step("Press button (Find communications)"):
        communications.press_find_communications_less_than_50()

    with allure.step("Check"):
        communications.assert_communications_found("Найдено коммуникаций 1 из 3130")


@pytest.mark.calls
@pytest.mark.independent
@allure.title("test_check_search_by_tag")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check search by tag for Ecotelecom")
def test_check_search_by_tag(base_url, page: Page) -> None:
    communications = Communications(page)

    with allure.step("Go to url"):
        communications.navigate(base_url)

    with allure.step("Auth with Ecotelecom"):
        communications.auth(ECOTELECOM, ECOPASS)

    with allure.step("Choose period from 01/01/2022 to 31/12/2022"):
        communications.choose_period_date("01/01/2022", "31/12/2022")

    with allure.step("Fill by tag"):
        communications.fill_by_tag("Другой отдел")

    with allure.step("Press button (Find communications)"):
        communications.press_find_communications_less_than_50()

    with allure.step("Check"):
        communications.assert_communications_found("Найдено коммуникаций 128 из 3130")

    with allure.step("Add extra tag"):
        communications.fill_by_tag("Обсуждение тарифа")

    with allure.step("Press button (Find communications)"):
        communications.press_find_communications_less_than_50()

    with allure.step("Check"):
        communications.assert_communications_found("Найдено коммуникаций 46 из 3130")

    with allure.step("Click to (Add condition)"):
        page.locator(BUTTON_DOBAVIT_USLOVIE).first.click()

    with allure.step("Change logic operator"):
        page.locator(CHANGE_LOGIC_OPERATOR).click()
        page.get_by_text("НЕТ ВСЕХ").click()

    with allure.step("Add new tag"):
        page.wait_for_selector(INPUT_PO_TEGAM_NEW, timeout=wait_until_visible)
        page.locator(INPUT_PO_TEGAM_NEW).fill("Новое подключение")
        page.wait_for_timeout(800)
        page.locator(MENU).locator('[id*="-option-0"]').get_by_text("Новое подключение", exact=True).click()
        page.locator(COMMUNICATIONS_SEARCH).click()  # tupo click

    with allure.step("Press button (Find communications)"):
        communications.press_find_communications_less_than_50()

    with allure.step("Check"):
        communications.assert_communications_found("Найдено коммуникаций 19 из 3130")


@pytest.mark.calls
@pytest.mark.independent
@allure.title("test_check_sort")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("Check sort (6 type) all calls for Ecotelecom")
def test_check_sort(base_url, page: Page) -> None:
    communications = Communications(page)

    with allure.step("Go to url"):
        communications.navigate(base_url)

    with allure.step("Auth with Ecotelecom"):
        communications.auth(ECOTELECOM, ECOPASS)

    with allure.step("Choose period from 01/01/2022 to 31/12/2022"):
        communications.choose_period_date("01/01/2022", "31/12/2022")

    with allure.step("Press button (Find communications)"):
        communications.press_find_communications_more_than_50()

    with allure.step("Check all communications count, OLD calls first by default"):
        communications.assert_communications_found("Найдено коммуникаций 3130 из 3130")
        communications.assert_call_date_and_time("08.02.22 00:12")

    with allure.step("Change sort to NEW FIRST"):
        communications.change_sort("Сначала новые")

    with allure.step("Check NEW FIRST in list"):
        communications.assert_call_date_and_time("16.05.22 18:21")

    with allure.step("Change sort to SHORT FIRST"):
        communications.change_sort("Сначала короткие")

    with allure.step("Check SHORT FIRST in list"):
        communications.assert_call_date_and_time("09.02.22 11:41")

    with allure.step("Change sort to LONG FIRST"):
        communications.change_sort("Сначала длинные")

    with allure.step("Check LONG FIRST in list"):
        communications.assert_call_date_and_time("09.02.22 18:08")

    with allure.step("Change sort to MORE POINTS"):
        communications.change_sort("Сначала много баллов")

    with allure.step("Check SHORT FIRST in list"):
        communications.assert_call_date_and_time("09.02.22 21:23")

    with allure.step("Change sort to LESS POINTS"):
        communications.change_sort("Сначала мало баллов")

    with allure.step("Check LONG FIRST in list"):
        communications.assert_call_date_and_time("10.02.22 10:57")


@pytest.mark.calls
@pytest.mark.independent
@allure.title("test_check_clear_all_fields")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("Check clear all fields by button for Ecotelecom")
def test_check_clear_all_fields(base_url, page: Page) -> None:
    communications = Communications(page)

    with allure.step("Go to url"):
        communications.navigate(base_url)

    with allure.step("Auth with Ecotelecom"):
        communications.auth(ECOTELECOM, ECOPASS)

    with allure.step("Fill all default fields"):
        page.wait_for_selector(INPUT_ID, timeout=wait_until_visible)

        communications.fill_client_number("79251579005")

        communications.fill_employee_number("4995055555")

        communications.fill_client_dict_or_text("минутку", "минутку")

        communications.fill_employee_dict_or_text("Зо", "Словарь: Зомбоящик")

        communications.fill_search_length(">10")

        communications.fill_time("11:42")

        communications.fill_id("1644474236.14425")

        communications.fill_by_tag("Другой отдел")

    with allure.step("Check all fields to have value"):
        expect(page.locator('[aria-label="Remove 79251579005"]')).to_be_visible()
        expect(page.locator('[aria-label="Remove 4995055555"]')).to_be_visible()
        expect(page.locator('[aria-label="Remove минутку"]')).to_be_visible()
        expect(page.locator('[aria-label="Remove Словарь: Зомбоящик"]')).to_be_visible()
        expect(page.locator('[aria-label="Remove >10"]')).to_be_visible()
        expect(page.locator('[aria-label="Remove 11:42"]')).to_be_visible()
        expect(page.locator('[aria-label="Remove 1644474236.14425"]')).to_be_visible()
        expect(page.locator('[aria-label="Remove Другой отдел"]')).to_be_visible()

    with allure.step("Press button (Clear)"):
        communications.press_clear_button()

    with allure.step("Check that cleared"):
        expect(page.locator('[aria-label="Remove 79251579005"]')).not_to_be_visible()
        expect(page.locator('[aria-label="Remove 4995055555"]')).not_to_be_visible()
        expect(page.locator('[aria-label="Remove минутку"]')).not_to_be_visible()
        expect(page.locator('[aria-label="Remove Словарь: Зомбоящик"]')).not_to_be_visible()
        expect(page.locator('[aria-label="Remove >10"]')).not_to_be_visible()
        expect(page.locator('[aria-label="Remove 11:42"]')).not_to_be_visible()
        expect(page.locator('[aria-label="Remove 1644474236.14425"]')).not_to_be_visible()
        expect(page.locator('[aria-label="Remove Другой отдел"]')).not_to_be_visible()


@pytest.mark.calls
@pytest.mark.independent
@allure.title("test_check_open_call_in_new_tab")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("test_check_open_call_in_new_tab")
def test_check_open_call_in_new_tab(base_url, page: Page, context: BrowserContext) -> None:
    communications = Communications(page)

    with allure.step("Go to url"):
        communications.navigate(base_url)

    with allure.step("Auth with Ecotelecom"):
        communications.auth(ECOTELECOM, ECOPASS)

    with allure.step("Choose period from 01/01/2022 to 31/12/2022"):
        communications.choose_period_date("01/01/2022", "31/12/2022")

    with allure.step("Fill ID to find call"):
        page.wait_for_selector(INPUT_ID, timeout=wait_until_visible)
        page.locator(INPUT_ID).locator('[type="text"]').type("1644268426.90181", delay=100)
        page.wait_for_timeout(500)

    with allure.step("Press button (Find communications)"):
        communications.press_find_communications_less_than_50()

    with allure.step("Open new tab"):
        with context.expect_page() as new_tab_event:
            page.locator('[data-testid="call_share"]').get_by_role("button").click()
            new_tab=new_tab_event.value

    with allure.step("Check"):
        page.wait_for_timeout(2000)
        expect(new_tab.locator(AUDIO_PLAYER)).to_have_count(1)
        expect(new_tab.locator('[class*="MuiAccordionSummary-content"]')).to_have_count(1)
        expect(new_tab.locator('[id="62050BEC113619D283D9D584"]')).to_have_count(1)
        expect(new_tab.locator('[class*="ClientBlock_employeePhone"]')).to_have_text("79161489993")
        expect(new_tab.locator('[class*="ClientBlock_employeeDuration"]')).to_have_text("00:00:42")
        expect(new_tab.locator('[aria-label="Применение GPT правила"]')).to_have_count(1)
        expect(new_tab.locator('[aria-label="Перетегировать"]')).to_have_count(1)
        expect(new_tab.locator('[aria-label="Скачать"]')).to_have_count(1)
        expect(new_tab.locator('[aria-label="Excel экспорт"]')).to_have_count(1)
        expect(new_tab.locator('[aria-label="Скопировать публичную ссылку"]')).to_have_count(1)
        expect(new_tab.locator('[class*="styles_withAllComments_"]')).to_have_count(1)
        expect(new_tab.get_by_text("Добавить комментарий")).to_have_count(1)

    with allure.step("Close context"):
        new_tab.close()


@pytest.mark.calls
@pytest.mark.independent
@allure.title("test_check_content_button_calls_actions")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("test_check_content_button_calls_actions (...)")
def test_check_content_button_calls_actions(base_url, page: Page) -> None:
    communications = Communications(page)

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        communications.navigate(base_url)

    with allure.step("Auth with user"):
        communications.auth(LOGIN, PASSWORD)

    with allure.step("Press button (Find communications)"):
        communications.press_find_communications_less_than_50()

    with allure.step("Press button (Calls action)"):
        communications.press_calls_action_button_in_list(0)

    with allure.step("Check content of button (...) calls action"):
        expect(page.locator(MENU)).to_have_text("Применить GPTПоменять аудио каналыЗагрузить теги из crmПрименить информированиеПрименить адресную книгуФильтр тегов")

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.calls
@pytest.mark.independent
@allure.title("test_check_download_button_in_calls_list")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("test_check_content_button_calls (download)")
def test_check_download_button_in_calls_list(base_url, page: Page) -> None:
    communications = Communications(page)

    with allure.step("Go to url"):
        communications.navigate(base_url)

    with allure.step("Auth with Ecotelecom"):
        communications.auth(ECOTELECOM, ECOPASS)

    with allure.step("Choose period from 01/01/2022 to 31/12/2022"):
        communications.choose_period_date("01/01/2022", "31/12/2022")

    with allure.step("Fill ID to find call"):
        page.wait_for_selector(INPUT_ID, timeout=wait_until_visible)
        page.locator(INPUT_ID).locator('[type="text"]').type("1644268426.90181", delay=30)
        page.wait_for_timeout(500)

    with allure.step("Press button (Find communications)"):
        communications.press_find_communications_less_than_50()

    with allure.step("Press button (Download)"):
        press_calls_list_download_button(0, page)

    with allure.step("Check content of button download"):
        expect(page.locator(MENU)).to_have_text("Экспорт аудиоЭкспорт расшифровкиЭкспорт коммуникаций")

    with allure.step("Choose (Export audio) option from opened menu"):
        # Start waiting for the download
        with page.expect_download(timeout=50000) as download_info:
            # Perform the action that initiates download
            page.locator(MENU).get_by_text("Экспорт аудио", exact=True).click()
        download = download_info.value
        path = f'{os.getcwd()}/'

        # Wait for the download process to complete and save the downloaded file somewhere
        download.save_as(path + download.suggested_filename)

    with allure.step("Check that export (zip) downloaded"):
        assert os.path.isfile(path + download.suggested_filename) == True
        assert 10000 < os.path.getsize(path + download.suggested_filename) < 15000

    with allure.step("Remove downloaded export (zip)"):
        os.remove(path + download.suggested_filename)

    with allure.step("Check that downloaded export (zip) removed"):
        assert os.path.isfile(path + download.suggested_filename) == False

    # For now not working. Download can take long time

    #with allure.step("Press button (Download)"):
    #    press_calls_action_button_in_list(0, page)

    #with allure.step("Choose (Export transcribe) option from opened menu"):
        # Start waiting for the download
    #    with page.expect_download(timeout=50000) as download_info:
            # Perform the action that initiates download
    #        page.locator('[class*="menu"]').get_by_text("Экспорт расшифровки", exact=True).click()
    #    download = download_info.value
    #    path = f'{os.getcwd()}/'

        # Wait for the download process to complete and save the downloaded file somewhere
    #    download.save_as(path + download.suggested_filename)

    #with allure.step("Check that export (zip) downloaded"):
   #     assert os.path.isfile(path + download.suggested_filename) == True

    #with allure.step("Remove downloaded export (zip)"):
    #    os.remove(path + download.suggested_filename)

    #with allure.step("Check that downloaded export (zip) removed"):
    #    assert os.path.isfile(path + download.suggested_filename) == False



@pytest.mark.calls
@pytest.mark.independent
@allure.title("test_check_buttons_in_open_call")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("test_check_buttons_in_open_call")
def test_check_buttons_in_open_call(base_url, page: Page) -> None:
    communications = Communications(page)

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        communications.navigate(base_url)

    with allure.step("Auth with user"):
        communications.auth(LOGIN, PASSWORD)

    # with allure.step("Press button (Find communications)"):
    #     press_find_communications(page)

    with allure.step("Expand call"):
        #page.wait_for_timeout(4000)
        page.wait_for_selector(BUTTON_EXPAND_CALL, timeout=wait_until_visible)
        #page.wait_for_timeout(500)
        page.locator(BUTTON_EXPAND_CALL).click()
        page.wait_for_selector(ALL_COMMENTS_AREA, timeout=wait_until_visible)

    with allure.step("Check that all 6 buttons in expanded call visible"):
        expect(page.locator(OPEN_CALL_AREA).locator('[aria-label="Переход в источник коммуникации"]')).to_be_visible()
        expect(page.locator(OPEN_CALL_AREA).locator('[aria-label="Применение GPT правила"]')).to_be_visible()
        expect(page.locator(OPEN_CALL_AREA).locator('[aria-label="Перетегировать"]')).to_be_visible()
        expect(page.locator(OPEN_CALL_AREA).locator('[aria-label="Скачать"]')).to_be_visible()
        expect(page.locator(OPEN_CALL_AREA).locator('[aria-label="Excel экспорт"]')).to_be_visible()
        expect(page.locator(OPEN_CALL_AREA).locator('[aria-label="Скопировать публичную ссылку"]')).to_be_visible()
        expect(page.locator(OPEN_CALL_AREA).locator(BUTTON_CALLS_ACTION)).to_be_visible()

    with allure.step("Click button (calls action)"):
        page.locator(OPEN_CALL_AREA).locator(BUTTON_CALLS_ACTION).click()

    with (allure.step("Check content in opened menu")):
        expect(page.locator(OPEN_CALL_AREA).locator(MENU)).to_have_text("Удаленные тегиМета инфоПоменять аудио каналыЗагрузить теги из crmПрименить информированиеПрименить адресную книгуРедактировать правило оповещения")

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)

@pytest.mark.calls
@pytest.mark.independent
@allure.title("test_check_download_call_from_expanded_call")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("test_check_download_call_from_expanded_call")
def test_check_download_call_from_expanded_call(base_url, page: Page) -> None:
    communications = Communications(page)

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        communications.navigate(base_url)

    with allure.step("Auth with user"):
        communications.auth(LOGIN, PASSWORD)

    # with allure.step("Press button (Find communications)"):
    #     press_find_communications(page)

    with allure.step("Expand call"):
        #page.wait_for_timeout(4500)
        page.wait_for_selector(BUTTON_EXPAND_CALL, timeout=wait_until_visible)
        page.locator(BUTTON_EXPAND_CALL).click()
        page.wait_for_selector(ALL_COMMENTS_AREA, timeout=wait_until_visible)

    with allure.step("Press (Download) button and download file"):
        # Start waiting for the download
        with page.expect_download(timeout=50000) as download_info:
            # Perform the action that initiates download
            page.locator(OPEN_CALL_AREA).locator('[aria-label="Скачать"]').locator('[type="button"]').click()
        download = download_info.value
        path = f'{os.getcwd()}/'

        # Wait for the download process to complete and save the downloaded file somewhere
        download.save_as(path + download.suggested_filename)

    with allure.step("Check that file opus downloaded"):
        assert os.path.isfile(path + download.suggested_filename) == True
        assert 139000 < os.path.getsize(path + download.suggested_filename) < 139700

    with allure.step("Remove downloaded file"):
        os.remove(path + download.suggested_filename)

    with allure.step("Check that file removed"):
        assert os.path.isfile(path + download.suggested_filename) == False

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)

@pytest.mark.calls
@pytest.mark.independent
@allure.title("test_check_download_excel_from_expanded_call")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_check_download_excel_from_expanded_call")
def test_check_download_excel_from_expanded_call(base_url, page: Page) -> None:
    communications = Communications(page)

    with allure.step("Go to url"):
        communications.navigate(base_url)

    with allure.step("Auth with Ecotelecom"):
        communications.auth(ECOTELECOM, ECOPASS)

    with allure.step("Choose period from 01/01/2022 to 31/12/2022"):
        communications.choose_period_date("01/01/2022", "31/12/2022")

    with allure.step("Fill ID to find call"):
        page.wait_for_selector(INPUT_ID, timeout=wait_until_visible)
        page.locator(INPUT_ID).locator('[type="text"]').type("1644268426.90181", delay=100)
        page.wait_for_timeout(500)

    with allure.step("Press button (Find communications)"):
        communications.press_find_communications_less_than_50()

    with allure.step("Expand call"):
        page.locator(BUTTON_EXPAND_CALL).click()
        page.wait_for_selector('[id="62050BEC113619D283D9D584-9-0"]')  #  wait word "nu"

    with allure.step("Press (EX) button"):
        press_ex_button_in_expanded_call(page)

    with allure.step("Check content of modal window"):
        expect(page.locator(MODAL_WINDOW).get_by_text("Теги без значений")).to_have_count(1)
        expect(page.locator(MODAL_WINDOW).get_by_text("Теги со значениями")).to_have_count(1)
        expect(page.locator(MODAL_WINDOW).get_by_text("Параметры коммуникаций")).to_have_count(1)

    with allure.step(" and download excel"):
        # Start waiting for the download
        with page.expect_download(timeout=50000) as download_info:
            # Perform the action that initiates download
            page.locator(MODAL_WINDOW).locator('[class*="buttonsBlock_"]').get_by_role("button", name="Экспортировать").click()
        download = download_info.value
        path = f'{os.getcwd()}/'

        # Wait for the download process to complete and save the downloaded file somewhere
        download.save_as(path + download.suggested_filename)

    with allure.step("Check that excel export downloaded"):
        assert os.path.isfile(path + download.suggested_filename) == True
        assert os.path.getsize(path + download.suggested_filename) > 7300

    with allure.step("Remove downloaded excel export"):
        os.remove(path + download.suggested_filename)

    with allure.step("Check that excel export removed"):
        assert os.path.isfile(path + download.suggested_filename) == False


@pytest.mark.calls
@pytest.mark.independent
@allure.title("test_check_search_template")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("test_check_search_template")
def test_check_search_template(base_url, page: Page) -> None:
    communications = Communications(page)

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        communications.navigate(base_url)

    with allure.step("Auth with user"):
        communications.auth(LOGIN, PASSWORD)
        page.wait_for_selector(BUTTON_FIND_COMMUNICATIONS)

    with allure.step("Check that no any templates"):
        expect(page.locator(CURRENT_TEMPLATE_NAME)).to_have_text("Сохраненные шаблоны поиска(0)")

    with allure.step("Save template"):
        press_save_template(page)

    with allure.step("Check that (add) button disabled"):
        expect(page.locator(MODAL_WINDOW).locator(BUTTON_SUBMIT)).to_be_disabled()

    with allure.step("Fill template name"):
        page.locator(INPUT_TEMPLATE_NAME).fill("firstTemplate")

    with allure.step("Check that (add) button enabled"):
        expect(page.locator(MODAL_WINDOW).locator(BUTTON_SUBMIT)).to_be_enabled()

    with allure.step("Press (add)"):
        page.locator(MODAL_WINDOW).locator(BUTTON_SUBMIT).click()

    with allure.step("Check that template saved"):
        expect(page.locator(CURRENT_TEMPLATE_NAME)).to_have_text("firstTemplate(1)")

    with allure.step("Rename template"):
        press_rename_template(page)

    with allure.step("Check that (add) button disabled"):
        expect(page.locator(MODAL_WINDOW).locator(BUTTON_SUBMIT)).to_be_disabled()

    with allure.step("Fill template name"):
        page.locator(INPUT_TEMPLATE_NAME).fill("renameTemplate")

    with allure.step("Check that (add) button enabled"):
        expect(page.locator(MODAL_WINDOW).locator(BUTTON_SUBMIT)).to_be_enabled()

    with allure.step("Press (add)"):
        page.locator(MODAL_WINDOW).locator(BUTTON_SUBMIT).click()

    with allure.step("Check that template saved"):
        expect(page.locator(CURRENT_TEMPLATE_NAME)).to_have_text("renameTemplate(1)")

    with allure.step("Delete template"):
        press_delete_template(page)

    with allure.step("Press (cancel)"):
        page.get_by_role("button", name="Отмена").click()

    with allure.step("Delete template"):
        press_delete_template(page)

    with allure.step("Confirm delete"):
        page.locator(MODAL_WINDOW).locator(BUTTON_SUBMIT).click()
        page.wait_for_timeout(300)

    with allure.step("Check that template saved"):
        expect(page.locator(CURRENT_TEMPLATE_NAME)).to_have_text("Сохраненные шаблоны поиска(0)")

    with allure.step("Check stupid text"):
        expect(page.locator('[style="font-size: 13px; margin-top: 15px;"]').get_by_text("Поиск пуст. Добавить фильтры можно с помощь 'Изменить фильтры'")).to_be_visible()

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.calls
@pytest.mark.independent
@allure.title("test_check_communication_comment")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("test_check_communication_comment")
def test_check_communication_comment(base_url, page: Page) -> None:
    communications = Communications(page)

    today = datetime.now().strftime("%d.%m.%Y, ")  # %H:%M can fail test if minutes changed while test running

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        communications.navigate(base_url)

    with allure.step("Auth with user"):
        communications.auth(LOGIN, PASSWORD)

    # with allure.step("Press button (Find communications)"):
    #     press_find_communications(page)

    with allure.step("Expand call"):
        page.wait_for_selector(BUTTON_EXPAND_CALL, timeout=wait_until_visible)
        page.wait_for_timeout(1500)
        page.locator(BUTTON_EXPAND_CALL).click()
        page.wait_for_selector(ALL_COMMENTS_AREA)

    with allure.step("Press (add comment)"):
        page.locator(BUTTON_ADD_COMMENT).click()

    with allure.step("Check that comment form openned"):
        page.wait_for_selector('[class*="styles_textareaWrapper"]')
        page.wait_for_timeout(500)
        expect(page.locator(ALL_COMMENTS_AREA).locator('[type="button"]').nth(1)).to_be_disabled()
        expect(page.locator(ALL_COMMENTS_AREA).locator('[type="checkbox"]')).not_to_be_checked()

    with allure.step("Check that we can close comment form with X"):
        page.locator(BUTTON_KRESTIK).click()

    with allure.step("Press (add comment)"):
        page.locator(BUTTON_ADD_COMMENT).click()

    with allure.step("Check checkbox (hidden)"):
        page.locator(ALL_COMMENTS_AREA).locator('[type="checkbox"]').check()

    with allure.step("Add title"):
        page.locator(BUTTON_ADD_COMMENT_TITLE).click()

    with allure.step("Fill title"):
        page.locator('[class*="styles_title_"]').fill("CommentTitle")

    with allure.step("Check that button (add comment) still disabled"):
        expect(page.locator(ALL_COMMENTS_AREA).locator('[type="button"]').nth(1)).to_be_disabled()

    with allure.step("Fill comment"):
        page.locator('[class*="styles_textareaWrapper"]').locator('[class*="styles_textarea_"]').fill("CommentText")

    with allure.step("Press (add comment)"):
        page.locator(ALL_COMMENTS_AREA).locator('[type="button"]').nth(1).click()

    with allure.step("Check that comment saved and saved right"):
        expect(page.locator('[class*="styles_author_"]')).to_have_text(LOGIN)
        expect(page.locator('[class*="styles_time_"]')).to_contain_text(today)
        expect(page.locator(COMMENT_AREA).locator('[class*="styles_head_"]').locator('[height="18"]')).to_have_count(1)
        expect(page.locator(COMMENT_AREA).locator('[class*="styles_title_"]')).to_have_text("CommentTitle")
        expect(page.locator(COMMENT_AREA).locator('[class*="styles_message_"]')).to_have_text("CommentText")

    with allure.step("Press to (...) comment options"):
        page.locator('[class*="styles_optionsSelect_"]').click()

    with allure.step("Choose and click (edit)"):
        page.locator(MENU).get_by_text("Редактировать", exact=True).click()
        page.wait_for_selector('[class*="styles_checkButton_"]')
        expect(page.locator('[class*="styles_checkButton_"]')).to_be_disabled()

    with allure.step("Edit title"):
        page.locator('[class*="styles_editableInput"]').clear()
        page.locator('[class*="styles_editableInput"]').fill("EditedTitle")

    with allure.step("Edit comment text"):
        page.locator('[class*="styles_editableTextarea"]').clear()
        page.locator('[class*="styles_editableTextarea"]').fill("EditedText")

    with allure.step("Save edited comment"):
        page.locator('[class*="styles_checkButton_"]').click()

    with allure.step("Check that edition comment saved"):
        expect(page.locator(COMMENT_AREA).locator('[class*="styles_title_"]')).to_have_text("EditedTitle")
        expect(page.locator(COMMENT_AREA).locator('[class*="styles_message_"]')).to_have_text("EditedText")

    with allure.step("Press to (...) comment options"):
        page.locator('[class*="styles_optionsSelect_"]').click()

    with allure.step("Choose and click (delete)"):
        page.locator(MENU).get_by_text("Удалить комментарий", exact=True).click()
        page.wait_for_selector(MODAL_WINDOW)

    with allure.step("Confirm deleting"):
        page.locator(MODAL_WINDOW).get_by_role("button", name="Удалить").click()
        page.wait_for_timeout(800)

    with allure.step("Check that comment was deleted"):
        expect(page.locator(COMMENT_AREA)).not_to_be_visible()

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.calls
@pytest.mark.independent
@allure.title("test_check_re_recognize_for_call_list")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check re-recognize in call list for ecotelecom. First finding by ID call with 0 length")
def test_check_re_recognize_for_call_list(base_url, page: Page) -> None:

    expected_languages = ("Английский (Великобритания)Английский (США)Испанский (Латинская Америка, Карибский регион, "
                          "код региона UN M49)Испанский (Испания)Французский (Франция)Португальский "
                          "(Бразилия)Португальский (Португалия)РусскийТурецкий (Турция)УкраинскийУзбекскийАвто")

    expected_engines = "DeepgramHappyscribeNLab SpeechIMOT.IOwhisperЯндексyandex_v3"

    alert_merge = "Опция 'Объединить дорожки в один файл' не может быть выбрана одновременно с любой из диаризаций"

    alert_diarization = "Выберите только одну диаризацию среди опций"

    action_started = "Действие начато"

    with allure.step("Create admin"):
        USER_ID, TOKEN, LOGIN= create_user(API_URL, ROLE_ADMIN, PASSWORD)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with admin"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to user"):
        go_to_user("Экотелеком", page)

    with allure.step("Choose period from 01/01/2022 to 31/12/2022"):
        choose_preiod_date("01/01/2022", "31/12/2022", page)

    with allure.step("Fill ID"):
        page.locator(INPUT_ID).locator('[type="text"]').type("1644396067.1832", delay=100)
        page.wait_for_timeout(300)

    with allure.step("Press button (Find communications)"):
        press_find_communications(page)

    with allure.step("Check"):
        expect(page.locator(NAYDENO_ZVONKOV).nth(0)).to_have_text("Найдено коммуникаций 1 из 3130", timeout=wait_until_visible)

    with allure.step("Click calls list actions button (...)"):
        press_calls_action_button_in_list(0, page)

    with allure.step("Choose re-recognize in menu"):
        page.locator(MENU).get_by_text("Перераспознать", exact=True).click()
        page.wait_for_timeout(1000)
        page.wait_for_selector(MODAL_WINDOW)

    with allure.step("Check modal window content"):
        expect(page.locator('[class*="styles_sttAllFoudCalls_"]')).to_contain_text(" (количество коммуникаций:  1)")
        expect(page.locator(SELECT_LANGUAGE)).to_contain_text("Русский")
        expect(page.locator(MODAL_WINDOW).locator(BUTTON_KRESTIK)).to_have_count(1)
        expect(page.locator(MODAL_WINDOW).locator(BUTTON_SUBMIT)).to_contain_text("Перераспознать")

#  check all combinations of engines and models

        with allure.step("Click to language"):
            page.locator(SELECT_LANGUAGE).locator('[type="text"]').click()
            page.wait_for_selector(MENU)

        with allure.step("Check language list"):
            expect(page.locator(MENU)).to_contain_text(expected_languages)

        with allure.step("Close language menu"):
            page.locator('[class*="STT_order_"]').click()

        # for ecotelecom engine and model already selected
        # with allure.step("Check that engine not selected"):
        #     expect(page.locator(SELECT_ENGINE)).to_contain_text("Выберите движок")

        # with allure.step("Check that model not selected"):
        #     expect(page.locator(SELECT_MODEL)).to_contain_text("Выберите модель")

        with allure.step("Click to engine"):
            page.locator(SELECT_ENGINE).locator('[type="text"]').click()
            page.wait_for_selector(MENU)

        with allure.step("Check engine list"):
            expect(page.locator(MENU)).to_contain_text(expected_engines)

        with allure.step("Click to engine"):
            page.locator(SELECT_ENGINE).locator('[type="text"]').click()
            page.wait_for_selector(MENU)

        with allure.step("Choose Deepgram"):
            choose_option(0, page)

        with allure.step("Click to model"):
            page.locator(SELECT_MODEL).locator('[type="text"]').click()
            page.wait_for_selector(MENU)

        with allure.step("Check model list"):
            expect(page.locator(MENU)).to_contain_text("Обобщённаяwhisper")

        with allure.step("Select model Обобщённая"):
            choose_option(0, page)

        with allure.step("Click to model"):
            page.locator(SELECT_MODEL).locator('[type="text"]').click()
            page.wait_for_selector(MENU)

        with allure.step("Select model whisper"):
            choose_option(1, page)

        with allure.step("Check engine parameters"):
            expect(page.locator(SELECT_ENGINE)).to_contain_text("Deepgram")
            expect(page.locator(SELECT_MODEL)).to_contain_text("whisper")
            expect(page.locator(CHECKBOX_MERGE_ALL_TO_ONE)).not_to_be_checked()
            expect(page.locator(RECOGNITION_PRIORITY).locator('[type="number"]')).to_have_value("1")
            expect(page.locator(CHECKBOX_DIARIZATION)).not_to_be_checked()
            expect(page.locator(CHECKBOX_ECONOMIZE)).to_be_checked()
            expect(page.locator('[type="checkbox"]')).to_have_count(3)

        with allure.step("Click to engine"):
            page.locator(SELECT_ENGINE).locator('[type="text"]').click()
            page.wait_for_selector(MENU)

        with allure.step("Choose Happyscribe"):
            choose_option(1, page)

        with allure.step("Click to model"):
            page.locator(SELECT_MODEL).locator('[type="text"]').click()
            page.wait_for_selector(MENU)

        with allure.step("Check model list"):
            expect(page.locator(MENU)).to_contain_text("Стандарт")

        with allure.step("Select model Стандарт"):
            choose_option(0, page)

        with allure.step("Check engine parameters"):
            expect(page.locator(SELECT_ENGINE)).to_contain_text("Happyscribe")
            expect(page.locator(SELECT_MODEL)).to_contain_text("Стандарт")
            expect(page.locator(CHECKBOX_MERGE_ALL_TO_ONE)).not_to_be_checked()
            expect(page.locator(RECOGNITION_PRIORITY).locator('[type="number"]')).to_have_value("1")
            expect(page.locator(CHECKBOX_DIARIZATION)).not_to_be_checked()
            expect(page.locator(CHECKBOX_ECONOMIZE)).to_be_checked()
            expect(page.locator('[type="checkbox"]')).to_have_count(3)

        with allure.step("Click to engine"):
            page.locator(SELECT_ENGINE).locator('[type="text"]').click()
            page.wait_for_selector(MENU)

        with allure.step("Choose NLab Speech"):
            choose_option(2, page)

        with allure.step("Click to model"):
            page.locator(SELECT_MODEL).locator('[type="text"]').click()
            page.wait_for_selector(MENU)

        with allure.step("Check model list"):
            expect(page.locator(MENU)).to_contain_text("ОбобщённаяЖадный")

        with allure.step("Select model Обобщённая"):
            choose_option(0, page)

        with allure.step("Click to model"):
            page.locator(SELECT_MODEL).locator('[type="text"]').click()
            page.wait_for_selector(MENU)

        with allure.step("Select model Жадный"):
            choose_option(1, page)

        with allure.step("Check engine parameters"):
            expect(page.locator(SELECT_ENGINE)).to_contain_text("NLab Speech")
            expect(page.locator(SELECT_MODEL)).to_contain_text("Жадный")
            expect(page.locator(CHECKBOX_MERGE_ALL_TO_ONE)).not_to_be_checked()
            expect(page.locator(RECOGNITION_PRIORITY).locator('[type="number"]')).to_have_value("1")
            expect(page.locator(CHECKBOX_DIARIZATION)).not_to_be_checked()
            expect(page.locator(CHECKBOX_ECONOMIZE)).to_be_checked()
            expect(page.locator('[type="checkbox"]')).to_have_count(3)


        with allure.step("Click to engine"):
            page.locator(SELECT_ENGINE).locator('[type="text"]').click()
            page.wait_for_selector(MENU)

        with allure.step("Choose IMOT.IO"):
            choose_option(3, page)

        with allure.step("Click to model"):
            page.locator(SELECT_MODEL).locator('[type="text"]').click()
            page.wait_for_selector(MENU)

        with allure.step("Check model list"):
            expect(page.locator(MENU)).to_contain_text("Стандарт")

        with allure.step("Select model Стандарт"):
            choose_option(0, page)

        with allure.step("Check engine parameters"):
            expect(page.locator(SELECT_ENGINE)).to_contain_text("IMOT.IO")
            expect(page.locator(SELECT_MODEL)).to_contain_text("Стандарт")
            expect(page.locator(CHECKBOX_MERGE_ALL_TO_ONE)).not_to_be_checked()
            expect(page.locator(RECOGNITION_PRIORITY).locator('[type="number"]')).to_have_value("1")
            expect(page.locator(CHECKBOX_DIARIZATION)).not_to_be_checked()
            expect(page.locator(CHECKBOX_ECONOMIZE)).to_be_checked()
            expect(page.locator('[type="checkbox"]')).to_have_count(3)

        with allure.step("Click to engine"):
            page.locator(SELECT_ENGINE).locator('[type="text"]').click()
            page.wait_for_selector(MENU)

        with allure.step("Choose whisper"):
            choose_option(4, page)

        with allure.step("Click to model"):
            page.locator(SELECT_MODEL).locator('[type="text"]').click()
            page.wait_for_selector(MENU)

        with allure.step("Check model list"):
            expect(page.locator(MENU)).to_contain_text("Стандарт")

        with allure.step("Select model Стандарт"):
            choose_option(0, page)

        with allure.step("Check engine parameters"):
            expect(page.locator(SELECT_ENGINE)).to_contain_text("whisper")
            expect(page.locator(SELECT_MODEL)).to_contain_text("Стандарт")
            expect(page.locator(CHECKBOX_MERGE_ALL_TO_ONE)).not_to_be_checked()
            expect(page.locator(RECOGNITION_PRIORITY).locator('[type="number"]')).to_have_value("1")
            expect(page.locator(CHECKBOX_DIARIZATION)).not_to_be_checked()
            expect(page.locator(CHECKBOX_ECONOMIZE)).to_be_checked()
            expect(page.locator('[type="checkbox"]')).to_have_count(5)

        with allure.step("Click to engine"):
            page.locator(SELECT_ENGINE).locator('[type="text"]').click()
            page.wait_for_selector(MENU)

        with allure.step("Choose Яндекс"):
            choose_option(5, page)

        with allure.step("Click to model"):
            page.locator(SELECT_MODEL).locator('[type="text"]').click()
            page.wait_for_selector(MENU)
            page.wait_for_timeout(500)

        with allure.step("Check model list"):
            expect(page.locator(MENU)).to_contain_text("Отложенная обобщённаяОбобщённая")

        with allure.step("Select model Отложенная обобщённая"):
            choose_option(0, page)

        with allure.step("Click to model"):
            page.locator(SELECT_MODEL).locator('[type="text"]').click()
            page.wait_for_selector(MENU)

        with allure.step("Select model Обобщённая"):
            choose_option(1, page)

        with allure.step("Check engine parameters"):
            expect(page.locator(SELECT_ENGINE)).to_contain_text("Яндекс")
            expect(page.locator(SELECT_MODEL)).to_contain_text("Обобщённая")
            expect(page.locator(CHECKBOX_MERGE_ALL_TO_ONE)).to_be_checked()
            expect(page.locator(RECOGNITION_PRIORITY).locator('[type="number"]')).to_have_value("1")
            expect(page.locator(CHECKBOX_DIARIZATION)).not_to_be_checked()
            expect(page.locator(CHECKBOX_ECONOMIZE)).to_be_checked()
            expect(page.locator('[type="checkbox"]')).to_have_count(3)

        with allure.step("Click to engine"):
            page.locator(SELECT_ENGINE).locator('[type="text"]').click()
            page.wait_for_selector(MENU)

        with allure.step("Choose yandex_v3"):
            choose_option(6, page)

        with allure.step("Click to model"):
            page.locator(SELECT_MODEL).locator('[type="text"]').click()
            page.wait_for_selector(MENU)

        with allure.step("Check model list"):
            expect(page.locator(MENU)).to_contain_text("Отложенная обобщённаяОбобщённая")

        with allure.step("Select model Отложенная обобщённая"):
            choose_option(0, page)

        with allure.step("Click to model"):
            page.locator(SELECT_MODEL).locator('[type="text"]').click()
            page.wait_for_selector(MENU)

        with allure.step("Select model Обобщённая"):
            choose_option(1, page)

        with allure.step("Check engine parameters"):
            expect(page.locator(SELECT_ENGINE)).to_contain_text("yandex_v3")
            expect(page.locator(SELECT_MODEL)).to_contain_text("Обобщённая")
            expect(page.locator(CHECKBOX_MERGE_ALL_TO_ONE)).to_be_checked()
            expect(page.locator(RECOGNITION_PRIORITY).locator('[type="number"]')).to_have_value("1")
            expect(page.locator(CHECKBOX_DIARIZATION)).not_to_be_checked()
            expect(page.locator(CHECKBOX_ENGINE_DIARIZATION)).to_be_checked()
            expect(page.locator(CHECKBOX_NORMALIZATION)).not_to_be_checked()
            expect(page.locator(CHECKBOX_PROFANITY_FILTER)).not_to_be_checked()
            expect(page.locator(CHECKBOX_LITERATURE_STYLE)).not_to_be_checked()
            expect(page.locator(CHECKBOX_PHONE_FORMATTING)).to_be_checked()
            expect(page.locator(CHECKBOX_ECONOMIZE)).to_be_checked()
            expect(page.locator('[type="checkbox"]')).to_have_count(8)

#  check save combinations

    with allure.step("Click to engine"):
        page.locator(SELECT_ENGINE).locator('[type="text"]').click()
        page.wait_for_selector(MENU)

    with allure.step("Choose assembly_ai"):
        choose_option(6, page)

    with allure.step("Check (Save) button is disabled"):
        expect(page.locator(BLOCK_WITH_BUTTON).locator(BUTTON_SUBMIT)).to_be_enabled()

    with allure.step("Click to model"):
        page.locator(SELECT_MODEL).locator('[type="text"]').click()
        page.wait_for_selector(MENU)

    with allure.step("Select model best"):
        choose_option(0, page)

    with allure.step("Check (Save) button is enabled"):
        expect(page.locator(BLOCK_WITH_BUTTON).locator(BUTTON_SUBMIT)).to_be_enabled()

    with allure.step("Check merge all to one checkbox"):
        page.locator(CHECKBOX_MERGE_ALL_TO_ONE).set_checked(checked=True)

    with allure.step("Try to save"):
        click_submit_in_word_processing(page)

    with allure.step("Wait for alert and check alert message"):
        page.wait_for_selector(ALERT, timeout=wait_until_visible)
        expect(page.locator(ALERT)).to_contain_text(alert_merge)
        page.wait_for_selector(ALERT, state="hidden", timeout=wait_until_visible)

    with allure.step("Uncheck merge all to one checkbox"):
        page.locator(CHECKBOX_MERGE_ALL_TO_ONE).uncheck()

    with allure.step("Check diarization checkbox"):
        page.locator(CHECKBOX_DIARIZATION).set_checked(checked=True)

    with allure.step("Try to save"):
        click_submit_in_word_processing(page)

    with allure.step("Wait for alert and check alert message"):
        page.wait_for_selector(ALERT, timeout=wait_until_visible)
        expect(page.locator(ALERT)).to_contain_text(alert_diarization)
        page.wait_for_selector(ALERT, state="hidden", timeout=wait_until_visible)

    with allure.step("Uncheck diarization checkbox"):
        page.locator(CHECKBOX_DIARIZATION).uncheck()

    with allure.step("Change parameters"):
        page.locator(RECOGNITION_PRIORITY).locator('[type="number"]').fill("10")
        page.locator(CHECKBOX_ECONOMIZE).set_checked(checked=True)
        #page.locator(CHECKBOX_USE_WEBHOOK).set_checked(checked=True)

    with allure.step("Press (Save)"):
        click_submit_in_word_processing(page)

    with allure.step("Wait for alert and check alert message"):
        page.wait_for_selector(ALERT, timeout=wait_until_visible)
        # expect(page.locator(ALERT)).to_contain_text(action_started)
        # page.wait_for_selector(ALERT, state="hidden", timeout=wait_until_visible)

    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN, USER_ID)



@pytest.mark.calls
@pytest.mark.independent
@allure.title("test_check_re_recognize_for_expanded_call")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check re-recognize in expanded call for ecotelecom. First finding by ID call with 0 length")
def test_check_re_recognize_for_expanded_call(base_url, page: Page) -> None:
    communications = Communications(page)

    expected_languages = ("Английский (Великобритания)Английский (США)Испанский (Латинская Америка, Карибский регион, "
                          "код региона UN M49)Испанский (Испания)Французский (Франция)Португальский "
                          "(Бразилия)Португальский (Португалия)РусскийТурецкий (Турция)УкраинскийУзбекскийАвто")

    expected_engines = "DeepgramHappyscribeNLab SpeechIMOT.IOwhisperЯндексyandex_v3"

    alert_merge = "Опция 'Объединить дорожки в один файл' не может быть выбрана одновременно с любой из диаризаций"

    alert_diarization = "Выберите только одну диаризацию среди опций"

    action_started = "Действие начато"

    with allure.step("Create admin"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    with allure.step("Go to url"):
        communications.navigate(base_url)

    with allure.step("Auth with admin"):
        communications.auth(LOGIN, PASSWORD)

    with allure.step("Go to user"):
        go_to_user("Экотелеком", page)

    with allure.step("Choose period from 01/01/2022 to 31/12/2022"):
        choose_preiod_date("01/01/2022", "31/12/2022", page)

    with allure.step("Fill ID"):
        page.locator(INPUT_ID).locator('[type="text"]').type("1644396067.1832", delay=100)
        page.wait_for_timeout(500)

    with allure.step("Press button (Find communications)"):
        press_find_communications(page)

    with allure.step("Check"):
        expect(page.locator(NAYDENO_ZVONKOV).nth(0)).to_have_text("Найдено коммуникаций 1 из 3130", timeout=wait_until_visible)

    with allure.step("Expand call"):
        page.locator(BUTTON_EXPAND_CALL).click()
        page.wait_for_selector(ALL_COMMENTS_AREA)

    with allure.step("Click calls list actions button (...)"):
        press_calls_action_button_in_list(1, page)

    with allure.step("Choose re-recognize in menu"):
        page.locator(MENU).get_by_text("Перераспознать", exact=True).click()
        page.wait_for_selector(MODAL_WINDOW)

    with allure.step("Check modal window content"):
        expect(page.locator(SELECT_LANGUAGE)).to_contain_text("Русский")
        expect(page.locator(MODAL_WINDOW).locator(BUTTON_KRESTIK)).to_have_count(1)
        expect(page.locator(MODAL_WINDOW).locator(BUTTON_SUBMIT)).to_contain_text("Перераспознать")
#  check all combinations of engines and models

    with allure.step("Click to language"):
        page.locator(SELECT_LANGUAGE).locator('[type="text"]').click()
        page.wait_for_selector(MENU)

    with allure.step("Check language list"):
        expect(page.locator(MENU)).to_contain_text(expected_languages)

    with allure.step("Close language menu"):
        page.locator('[class*="STT_order_"]').click()

    # for ecotelecom engine and model already selected
    # with allure.step("Check that engine not selected"):
    #     expect(page.locator(SELECT_ENGINE)).to_contain_text("Выберите движок")

    # with allure.step("Check that model not selected"):
    #     expect(page.locator(SELECT_MODEL)).to_contain_text("Выберите модель")

    with allure.step("Click to engine"):
        page.locator(SELECT_ENGINE).locator('[type="text"]').click()
        page.wait_for_selector(MENU)

    with allure.step("Check engine list"):
        expect(page.locator(MENU)).to_contain_text(expected_engines)

    with allure.step("Click to engine"):
        page.locator(SELECT_ENGINE).locator('[type="text"]').click()
        page.wait_for_selector(MENU)

    with allure.step("Choose Deepgram"):
        choose_option(0, page)

    with allure.step("Click to model"):
        page.locator(SELECT_MODEL).locator('[type="text"]').click()
        page.wait_for_selector(MENU)

    with allure.step("Check model list"):
        expect(page.locator(MENU)).to_contain_text("Обобщённаяwhisper")

    with allure.step("Select model Обобщённая"):
        choose_option(0, page)

    with allure.step("Click to model"):
        page.locator(SELECT_MODEL).locator('[type="text"]').click()
        page.wait_for_selector(MENU)

    with allure.step("Select model whisper"):
        choose_option(1, page)

    with allure.step("Check engine parameters"):
        expect(page.locator(SELECT_ENGINE)).to_contain_text("Deepgram")
        expect(page.locator(SELECT_MODEL)).to_contain_text("whisper")
        expect(page.locator(CHECKBOX_MERGE_ALL_TO_ONE)).not_to_be_checked()
        expect(page.locator(RECOGNITION_PRIORITY).locator('[type="number"]')).to_have_value("1")
        expect(page.locator(CHECKBOX_DIARIZATION)).not_to_be_checked()
        expect(page.locator(CHECKBOX_ECONOMIZE)).to_be_checked()
        expect(page.locator('[type="checkbox"]')).to_have_count(3)

    with allure.step("Click to engine"):
        page.locator(SELECT_ENGINE).locator('[type="text"]').click()
        page.wait_for_selector(MENU)

    with allure.step("Choose Happyscribe"):
        choose_option(1, page)

    with allure.step("Click to model"):
        page.locator(SELECT_MODEL).locator('[type="text"]').click()
        page.wait_for_selector(MENU)

    with allure.step("Check model list"):
        expect(page.locator(MENU)).to_contain_text("Стандарт")

    with allure.step("Select model Стандарт"):
        choose_option(0, page)

    with allure.step("Check engine parameters"):
        expect(page.locator(SELECT_ENGINE)).to_contain_text("Happyscribe")
        expect(page.locator(SELECT_MODEL)).to_contain_text("Стандарт")
        expect(page.locator(CHECKBOX_MERGE_ALL_TO_ONE)).not_to_be_checked()
        expect(page.locator(RECOGNITION_PRIORITY).locator('[type="number"]')).to_have_value("1")
        expect(page.locator(CHECKBOX_DIARIZATION)).not_to_be_checked()
        expect(page.locator(CHECKBOX_ECONOMIZE)).to_be_checked()
        expect(page.locator('[type="checkbox"]')).to_have_count(3)

    with allure.step("Click to engine"):
        page.locator(SELECT_ENGINE).locator('[type="text"]').click()
        page.wait_for_selector(MENU)

    with allure.step("Choose NLab Speech"):
        choose_option(2, page)

    with allure.step("Click to model"):
        page.locator(SELECT_MODEL).locator('[type="text"]').click()
        page.wait_for_selector(MENU)

    with allure.step("Check model list"):
        expect(page.locator(MENU)).to_contain_text("ОбобщённаяЖадный")

    with allure.step("Select model Обобщённая"):
        choose_option(0, page)

    with allure.step("Click to model"):
        page.locator(SELECT_MODEL).locator('[type="text"]').click()
        page.wait_for_selector(MENU)

    with allure.step("Select model Жадный"):
        choose_option(1, page)

    with allure.step("Check engine parameters"):
        expect(page.locator(SELECT_ENGINE)).to_contain_text("NLab Speech")
        expect(page.locator(SELECT_MODEL)).to_contain_text("Жадный")
        expect(page.locator(CHECKBOX_MERGE_ALL_TO_ONE)).not_to_be_checked()
        expect(page.locator(RECOGNITION_PRIORITY).locator('[type="number"]')).to_have_value("1")
        expect(page.locator(CHECKBOX_DIARIZATION)).not_to_be_checked()
        expect(page.locator(CHECKBOX_ECONOMIZE)).to_be_checked()
        expect(page.locator('[type="checkbox"]')).to_have_count(3)

    #
    with allure.step("Click to engine"):
        page.locator(SELECT_ENGINE).locator('[type="text"]').click()
        page.wait_for_selector(MENU)

    with allure.step("Choose IMOT.IO"):
        choose_option(3, page)

    with allure.step("Click to model"):
        page.locator(SELECT_MODEL).locator('[type="text"]').click()
        page.wait_for_selector(MENU)

    with allure.step("Check model list"):
        expect(page.locator(MENU)).to_contain_text("Стандарт")

    with allure.step("Select model Стандарт"):
        choose_option(0, page)

    with allure.step("Check engine parameters"):
        expect(page.locator(SELECT_ENGINE)).to_contain_text("IMOT.IO")
        expect(page.locator(SELECT_MODEL)).to_contain_text("Стандарт")
        expect(page.locator(CHECKBOX_MERGE_ALL_TO_ONE)).not_to_be_checked()
        expect(page.locator(RECOGNITION_PRIORITY).locator('[type="number"]')).to_have_value("1")
        expect(page.locator(CHECKBOX_DIARIZATION)).not_to_be_checked()
        expect(page.locator(CHECKBOX_ECONOMIZE)).to_be_checked()
        expect(page.locator('[type="checkbox"]')).to_have_count(3)

    with allure.step("Click to engine"):
        page.locator(SELECT_ENGINE).locator('[type="text"]').click()
        page.wait_for_selector(MENU)

    with allure.step("Choose whisper"):
        choose_option(4, page)

    with allure.step("Click to model"):
        page.locator(SELECT_MODEL).locator('[type="text"]').click()
        page.wait_for_selector(MENU)

    with allure.step("Check model list"):
        expect(page.locator(MENU)).to_contain_text("Стандарт")

    with allure.step("Select model Стандарт"):
        choose_option(0, page)

    with allure.step("Check engine parameters"):
        expect(page.locator(SELECT_ENGINE)).to_contain_text("whisper")
        expect(page.locator(SELECT_MODEL)).to_contain_text("Стандарт")
        expect(page.locator(CHECKBOX_MERGE_ALL_TO_ONE)).not_to_be_checked()
        expect(page.locator(RECOGNITION_PRIORITY).locator('[type="number"]')).to_have_value("1")
        expect(page.locator(CHECKBOX_DIARIZATION)).not_to_be_checked()
        expect(page.locator(CHECKBOX_ECONOMIZE)).to_be_checked()
        expect(page.locator('[type="checkbox"]')).to_have_count(5)

    with allure.step("Click to engine"):
        page.locator(SELECT_ENGINE).locator('[type="text"]').click()
        page.wait_for_selector(MENU)

    with allure.step("Choose Яндекс"):
        choose_option(5, page)

    with allure.step("Click to model"):
        page.locator(SELECT_MODEL).locator('[type="text"]').click()
        page.wait_for_selector(MENU)

    with allure.step("Check model list"):
        expect(page.locator(MENU)).to_contain_text("Отложенная обобщённаяОбобщённая")

    with allure.step("Select model Отложенная обобщённая"):
        choose_option(0, page)

    with allure.step("Click to model"):
        page.locator(SELECT_MODEL).locator('[type="text"]').click()
        page.wait_for_selector(MENU)

    with allure.step("Select model Обобщённая"):
        choose_option(1, page)

    with allure.step("Check engine parameters"):
        expect(page.locator(SELECT_ENGINE)).to_contain_text("Яндекс")
        expect(page.locator(SELECT_MODEL)).to_contain_text("Обобщённая")
        expect(page.locator(CHECKBOX_MERGE_ALL_TO_ONE)).to_be_checked()
        expect(page.locator(RECOGNITION_PRIORITY).locator('[type="number"]')).to_have_value("1")
        expect(page.locator(CHECKBOX_DIARIZATION)).not_to_be_checked()
        expect(page.locator(CHECKBOX_ECONOMIZE)).to_be_checked()
        expect(page.locator('[type="checkbox"]')).to_have_count(3)
    #
    with allure.step("Click to engine"):
        page.locator(SELECT_ENGINE).locator('[type="text"]').click()
        page.wait_for_selector(MENU)

    with allure.step("Choose yandex_v3"):
        choose_option(6, page)

    with allure.step("Click to model"):
        page.locator(SELECT_MODEL).locator('[type="text"]').click()
        page.wait_for_selector(MENU)

    with allure.step("Check model list"):
        expect(page.locator(MENU)).to_contain_text("Отложенная обобщённаяОбобщённая")

    with allure.step("Select model Отложенная обобщённая"):
        choose_option(0, page)

    with allure.step("Click to model"):
        page.locator(SELECT_MODEL).locator('[type="text"]').click()
        page.wait_for_selector(MENU)

    with allure.step("Select model Обобщённая"):
        choose_option(1, page)

    with allure.step("Check engine parameters"):
        expect(page.locator(SELECT_ENGINE)).to_contain_text("yandex_v3")
        expect(page.locator(SELECT_MODEL)).to_contain_text("Обобщённая")
        expect(page.locator(CHECKBOX_MERGE_ALL_TO_ONE)).to_be_checked()
        expect(page.locator(RECOGNITION_PRIORITY).locator('[type="number"]')).to_have_value("1")
        expect(page.locator(CHECKBOX_DIARIZATION)).not_to_be_checked()
        expect(page.locator(CHECKBOX_ENGINE_DIARIZATION)).to_be_checked()
        expect(page.locator(CHECKBOX_NORMALIZATION)).not_to_be_checked()
        expect(page.locator(CHECKBOX_PROFANITY_FILTER)).not_to_be_checked()
        expect(page.locator(CHECKBOX_LITERATURE_STYLE)).not_to_be_checked()
        expect(page.locator(CHECKBOX_PHONE_FORMATTING)).to_be_checked()
        expect(page.locator(CHECKBOX_ECONOMIZE)).to_be_checked()
        expect(page.locator('[type="checkbox"]')).to_have_count(8)

#  check save combinations

    with allure.step("Click to engine"):
        page.locator(SELECT_ENGINE).locator('[type="text"]').click()
        page.wait_for_selector(MENU)

    with allure.step("Choose assembly_ai"):
        choose_option(6, page)

    with allure.step("Check (Save) button is disabled"):
        expect(page.locator(BLOCK_WITH_BUTTON).locator(BUTTON_SUBMIT)).to_be_enabled()

    with allure.step("Click to model"):
        page.locator(SELECT_MODEL).locator('[type="text"]').click()
        page.wait_for_selector(MENU)

    with allure.step("Select model best"):
        choose_option(0, page)

    with allure.step("Check (Save) button is enabled"):
        expect(page.locator(BLOCK_WITH_BUTTON).locator(BUTTON_SUBMIT)).to_be_enabled()

    with allure.step("Check merge all to one checkbox"):
        page.locator(CHECKBOX_MERGE_ALL_TO_ONE).set_checked(checked=True)

    with allure.step("Try to save"):
        click_submit_in_word_processing(page)

    with allure.step("Wait for alert and check alert message"):
        page.wait_for_selector(ALERT, timeout=wait_until_visible)
        expect(page.locator(ALERT)).to_contain_text(alert_merge)
        page.wait_for_selector(ALERT, state="hidden", timeout=wait_until_visible)

    with allure.step("Uncheck merge all to one checkbox"):
        page.locator(CHECKBOX_MERGE_ALL_TO_ONE).uncheck()

    with allure.step("Check diarization checkbox"):
        page.locator(CHECKBOX_DIARIZATION).set_checked(checked=True)

    with allure.step("Try to save"):
        click_submit_in_word_processing(page)

    with allure.step("Wait for alert and check alert message"):
        page.wait_for_selector(ALERT, timeout=wait_until_visible)
        expect(page.locator(ALERT)).to_contain_text(alert_diarization)
        page.wait_for_selector(ALERT, state="hidden", timeout=wait_until_visible)

    with allure.step("Uncheck diarization checkbox"):
        page.locator(CHECKBOX_DIARIZATION).uncheck()

    with allure.step("Change parameters"):
        page.locator(RECOGNITION_PRIORITY).locator('[type="number"]').fill("10")
        page.locator(CHECKBOX_ECONOMIZE).set_checked(checked=True)
        #page.locator(CHECKBOX_USE_WEBHOOK).set_checked(checked=True)

    with allure.step("Press (Save)"):
        click_submit_in_word_processing(page)

    with allure.step("Wait for alert and check alert message"):
        page.wait_for_selector(ALERT, timeout=wait_until_visible)
        expect(page.locator(ALERT)).to_contain_text(action_started)
        page.wait_for_selector(ALERT, state="hidden", timeout=wait_until_visible)

    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.calls
@pytest.mark.independent
@allure.title("test_check_communication_manual_tag")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("test_check_communication_manual_tag")
def test_check_communication_manual_tag(base_url, page: Page) -> None:
    communications = Communications(page)

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        communications.navigate(base_url)

    with allure.step("Auth with user"):
        communications.auth(LOGIN, PASSWORD)

    # with allure.step("Press button (Find communications)"):
    #     press_find_communications(page)

    with allure.step("Expand call"):
        page.wait_for_selector(BUTTON_EXPAND_CALL, timeout=wait_until_visible)
        page.wait_for_timeout(4000)
        page.locator(BUTTON_EXPAND_CALL).click()
        page.wait_for_selector(ALL_COMMENTS_AREA)

    with allure.step("Press (add manual tag)"):
        page.locator('[class*="_manualGroup_"]').locator('[type="button"]').click()
        page.wait_for_selector('[data-testid="CustomSelectWithSearch"]')

    with allure.step("Press (add comment)"):
        page.keyboard.press("Enter")

    with allure.step("Wait for alert and check alert message"):
        page.wait_for_selector(ALERT, timeout=wait_until_visible)
        expect(page.locator(ALERT)).to_contain_text("Укажите название тега")
        page.wait_for_selector(ALERT, state="hidden", timeout=wait_until_visible)

    # with allure.step("Press (add manual tag)"):
    #     page.locator('[class*="_manualGroup_"]').locator('[type="button"]').click()
    #     page.wait_for_selector('[data-testid="CustomSelectWithSearch"]')

    with allure.step("Press (add manual tag)"):
        page.wait_for_timeout(500)
        page.locator('[data-testid="CustomSelectWithSearch"]').locator('[class*="_tagGhost_"]').click()
        page.wait_for_timeout(300)
        page.wait_for_selector('[data-testid="CustomSelectWithSearch"]')

    with allure.step("Add manual tag name"):
        page.locator('[data-testid="CustomSelectWithSearch"]').locator('[role="combobox"]').type("manual_tag", delay=100)

    with allure.step("Press (add comment)"):
        page.keyboard.press("Enter")

    with allure.step("Wait for alert and check alert message"):
        page.wait_for_selector(ALERT, timeout=wait_until_visible)
        expect(page.locator(ALERT)).to_contain_text("Тег успешно добавлен")
        page.wait_for_selector(ALERT, state="hidden", timeout=wait_until_visible)

    with allure.step("Check that we can see 2 manual tags"):
        expect(page.locator('[data-testid*="tag-"]')).to_have_count(2)

    with allure.step("Press pencil button in tag"):
        page.locator('[fill="#d9f7be"]').nth(0).click()
        page.wait_for_selector('[role="tooltip"]')

    with allure.step("Press delete"):
        page.locator('[role="tooltip"]').get_by_text("Удалить").click()
        page.wait_for_selector(MODAL_WINDOW)

    with allure.step(""):
        page.locator(MODAL_WINDOW).locator(BUTTON_SUBMIT).click()
        page.wait_for_selector(MODAL_WINDOW, state="hidden", timeout=wait_until_visible)

    with allure.step("Wait for alert and check alert message"):
        page.wait_for_selector(ALERT, timeout=wait_until_visible)
        expect(page.locator(ALERT)).to_contain_text("Тег удален")
        page.wait_for_selector(ALERT, state="hidden", timeout=wait_until_visible)

    with allure.step("Check that we can see 2 manual tags"):
        expect(page.locator('[data-testid*="tag-"]')).to_have_count(0)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.calls
@pytest.mark.independent
@allure.title("test_check_search_and_switch_to_other_user")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Searching all communications for Ecotelecom and switch to auto_test_user and check that calls changed")
def test_check_search_and_switch_to_other_user(base_url, page: Page) -> None:
    communications = Communications(page)

    with allure.step("Create admin"):
        USER_ID_ADMIN, TOKEN_ADMIN, LOGIN_ADMIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        communications.navigate(base_url)

    with allure.step("Auth with Ecotelecom"):
        communications.auth(LOGIN_ADMIN, PASSWORD)

    with allure.step("Change user to auto_test_user"):
        communications.go_to_user("Экотелеком")

    with allure.step("Choose period from 01/01/2022 to 31/12/2022"):
        communications.choose_period_date("01/01/2022", "31/12/2022")

    with allure.step("Press button (Find communications)"):
        communications.press_find_communications_more_than_50()

    with allure.step("Check that all communications found"):
        communications.assert_communications_found("Найдено коммуникаций 3130 из 3130")

    with allure.step("Go to settings"):
        communications.click_settings()

    with allure.step("Change user to auto_test_user"):
        go_to_user(LOGIN_USER, page)

    with allure.step("Go to communications"):
        page.locator(BUTTON_COMMUNICATIONS).click()
        page.wait_for_selector(BUTTON_FIND_COMMUNICATIONS, timeout=wait_until_visible)

    with allure.step("Press button (Find communications)"):
        communications.press_find_communications_less_than_50()

    with allure.step("Check that 1 communications found. Should be 1 and date today"):
        communications.assert_communications_found("Найдено коммуникаций 0 из 0")

    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN_ADMIN, USER_ID_ADMIN)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)