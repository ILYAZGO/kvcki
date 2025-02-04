from playwright.sync_api import Page, expect, BrowserContext, sync_playwright, Playwright
from utils.variables import *
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
@allure.description("Check dates buttons")
def test_check_dates(base_url, page: Page) -> None:
    communications = Communications(page)

    with allure.step("Go to url"):
        communications.navigate(base_url)

    with allure.step("Auth with Ecotelecom"):
        communications.auth(ECOTELECOM, ECOPASS)

    with allure.step("Check first and last dates in view. Today by default"):
        communications.assert_check_period_dates(today.strftime("%d/%m/%Y"), today.strftime("%d/%m/%Y"))

    with allure.step("Switch to yesterday"):
        communications.yesterday.click()

    with allure.step("Check first and last dates in view."):
        communications.assert_check_period_dates(yesterday.strftime("%d/%m/%Y"), yesterday.strftime("%d/%m/%Y"))

    with allure.step("Click to week"):
        communications.week.click()

    with allure.step("Choose this week"):
        communications.select_period_value("this_week")

    with allure.step("Check first and last dates in view."):
        communications.assert_check_period_dates(first_day_this_week.strftime("%d/%m/%Y"), last_day_this_week.strftime("%d/%m/%Y"))

    with allure.step("Click to week"):
        communications.week.click()

    with allure.step("Choose last week"):
        communications.select_period_value("last_week")

    with allure.step("Check first and last dates in view."):
        communications.assert_check_period_dates(first_day_last_week.strftime("%d/%m/%Y"), last_day_last_week.strftime("%d/%m/%Y"))

    with allure.step("Click to month"):
        communications.month.click()

    with allure.step("Choose this month"):
        communications.select_period_value("this_month")

    with allure.step("Check first and last dates in view."):
        communications.assert_check_period_dates(first_day_this_month.strftime("%d/%m/%Y"), last_day_this_month.strftime("%d/%m/%Y"))

    with allure.step("Click to month"):
        communications.month.click()

    with allure.step("Choose last month"):
        communications.select_period_value("last_month")

    with allure.step("Check first and last dates in view."):
        communications.assert_check_period_dates(first_day_last_month.strftime("%d/%m/%Y"), last_day_last_month.strftime("%d/%m/%Y"))

    with allure.step("Click to quarter"):
        communications.quarter.click()

    with allure.step("Choose this quarter"):
        communications.select_period_value("this_quarter")

    with allure.step("Check first and last dates in view."):
        communications.assert_check_period_dates(first_day_this_quarter.strftime("%d/%m/%Y"), last_day_this_quarter.strftime("%d/%m/%Y"))

    with allure.step("Click to quarter"):
        communications.quarter.click()

    with allure.step("Choose last quarter"):
        communications.select_period_value("last_quarter")

    # with allure.step("Check first and last dates in view."):
    #     communications.assert_check_period_dates(first_day_last_quarter.strftime("%d/%m/%Y"), last_day_last_quarter.strftime("%d/%m/%Y"))

    with allure.step("Click to year"):
        communications.year.click()

    with allure.step("Choose this year"):
        communications.select_period_value("this_year")

    with allure.step("Check first and last dates in view."):
        communications.assert_check_period_dates(first_day_this_year.strftime("%d/%m/%Y"), last_day_this_year.strftime("%d/%m/%Y"))

    with allure.step("Click to year"):
        communications.year.click()

    with allure.step("Choose last year"):
        communications.select_period_value("last_year")

    with allure.step("Check first and last dates in view."):
        communications.assert_check_period_dates(first_day_last_year.strftime("%d/%m/%Y"), last_day_last_year.strftime("%d/%m/%Y"))

    with allure.step("Switch to all time"):
        communications.all_time.click()

    with allure.step("Check begin and end dates is disabled"):
        communications.assert_check_period_dates_disabled()


@pytest.mark.calls
@pytest.mark.independent
@allure.title("test_communications_check_calendar_localization")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("test_communications_check_calendar_localization")
def test_communications_check_calendar_localization(base_url, page: Page) -> None:
    communications = Communications(page)

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        communications.navigate(base_url)

    with allure.step("Auth with user"):
        communications.auth(LOGIN, PASSWORD)

    with allure.step("Click to calendar"):
        page.locator('[placeholder="Начальная дата"]').click()

    with allure.step("Check localization"):
        expect(page.locator('[class="ant-picker-content"]').nth(0)).to_contain_text("пнвтсрчтптсбвс")
        expect(page.locator('[class="ant-picker-content"]').nth(1)).to_contain_text("пнвтсрчтптсбвс")

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.calls
@pytest.mark.test
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

    with allure.step("Check that 50 calls in one page"):
        expect(page.locator(BUTTON_SHARE_CALL)).to_have_count(50)


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
@pytest.mark.test
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
@pytest.mark.test
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
        communications.fill_by_tag(0, "Другой отдел")

    with allure.step("Press button (Find communications)"):
        communications.press_find_communications_less_than_50()

    with allure.step("Check"):
        communications.assert_communications_found("Найдено коммуникаций 128 из 3130")

    with allure.step("Add extra tag"):
        communications.fill_by_tag(0, "Обсуждение тарифа")

    with allure.step("Press button (Find communications)"):
        communications.press_find_communications_less_than_50()

    with allure.step("Check"):
        communications.assert_communications_found("Найдено коммуникаций 46 из 3130")

    with allure.step("Click to (Add condition)"):
        page.locator(BUTTON_ADD_CONDITION).first.click()

    with allure.step("Change logic operator"):
        page.locator('[data-testid="filters_search_by_tags"]').nth(1).get_by_text("ИЛИ").click()
        page.wait_for_selector(MENU)
        page.get_by_text("НЕТ ВСЕХ").click()

    with allure.step("Add new tag"):
        communications.fill_by_tag(1, "Новое подключение")

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
        communications.fill_client_number("79251579005")
        communications.fill_employee_number("4995055555")
        communications.fill_client_dict_or_text("минутку", "минутку")
        communications.fill_employee_dict_or_text("Зо", "Словарь: Зомбоящик")
        communications.fill_search_length(">10")
        communications.fill_time("11:42")
        communications.fill_id("1644474236.14425")
        communications.fill_by_tag(0, "Другой отдел")

    with allure.step("Check all fields to have value"):
        expect(page.locator('[aria-label="Remove 79251579005"]')).to_be_visible()
        expect(page.locator('[aria-label="Remove 4995055555"]')).to_be_visible()
        expect(page.locator('[aria-label="Remove минутку"]')).to_be_visible()
        expect(page.locator('[aria-label="Remove Словарь: Зомбоящик"]')).to_be_visible()
        expect(page.locator('[aria-label="Remove >10"]')).to_be_visible()
        expect(page.locator('[aria-label="Remove 11:42"]')).to_be_visible()
        expect(page.locator('[aria-label="Remove 1644474236.14425"]')).to_be_visible()
        expect(page.locator('[aria-label="Remove Другой отдел"]')).to_be_visible()
        expect(page.locator(CURRENT_TEMPLATE_NAME)).to_be_visible()

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
        expect(page.locator(CURRENT_TEMPLATE_NAME)).to_be_visible()


@pytest.mark.calls
@pytest.mark.independent
@allure.title("test_check_open_call_in_new_tab_by_user")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("test_check_open_call_in_new_tab_by_user")
def test_check_open_call_in_new_tab_by_user(base_url, page: Page, context: BrowserContext) -> None:
    communications = Communications(page)

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        communications.navigate(base_url)

    with allure.step("Auth with user"):
        communications.auth(LOGIN, PASSWORD)
        page.wait_for_timeout(5000)

    with allure.step("Open new tab"):
        with context.expect_page() as new_tab_event:
            page.locator(BUTTON_SHARE_CALL).locator('[type="button"]').click()
            new_tab=new_tab_event.value

    with allure.step("Check"):
        page.wait_for_timeout(2500)
        expect(new_tab.locator(AUDIO_PLAYER)).to_have_count(1)
        expect(new_tab.locator('[class*="MuiAccordionSummary-content"]')).to_have_count(1)
        expect(new_tab.locator('[class*="ClientBlock_employeePhone"]')).to_have_text("0987654321")
        expect(new_tab.locator('[class*="ClientBlock_employeeDuration"]')).to_have_text("00:00:38")
        expect(new_tab.locator('[aria-label="Применение GPT правила"]')).to_have_count(1)
        expect(new_tab.locator('[aria-label="Перетегировать"]')).to_have_count(1)
        expect(new_tab.locator('[aria-label="Скачать"]')).to_have_count(1)
        expect(new_tab.locator('[aria-label="Excel экспорт"]')).to_have_count(1)
        expect(new_tab.locator('[aria-label="Скопировать публичную ссылку"]')).to_have_count(1)
        expect(new_tab.locator('[class*="styles_withAllComments_"]')).to_have_count(1)
        expect(new_tab.get_by_text("Добавить комментарий")).to_have_count(1)
        expect(new_tab.locator('[class*="_manualGroup_"]')).to_have_count(1)

    with allure.step("Close context"):
        new_tab.close()

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


# 00000000000
@pytest.mark.calls
@pytest.mark.independent
@allure.title("test_check_open_call_in_new_tab_by_admin")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("test_check_open_call_in_new_tab_by_admin")
def test_check_open_call_in_new_tab_by_admin(base_url, page: Page, context: BrowserContext) -> None:
    communications = Communications(page)

    with allure.step("Create admin"):
        USER_ID_ADMIN, TOKEN_ADMIN, LOGIN_ADMIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        communications.navigate(base_url)

    with allure.step("Auth with user"):
        communications.auth(LOGIN_ADMIN, PASSWORD)
        page.wait_for_timeout(5000)

    with allure.step("Go to user"):
        communications.go_to_user(LOGIN_USER)
        page.wait_for_load_state(state="load", timeout=wait_until_visible)
        page.wait_for_timeout(5000)

    with allure.step("Open new tab"):
        with context.expect_page() as new_tab_event:
            page.locator(BUTTON_SHARE_CALL).locator('[type="button"]').click()
            new_tab=new_tab_event.value

    with allure.step("Check"):
        page.wait_for_timeout(2500)
        expect(new_tab.locator(AUDIO_PLAYER)).to_have_count(1)
        expect(new_tab.locator('[class*="MuiAccordionSummary-content"]')).to_have_count(1)
        expect(new_tab.locator('[class*="ClientBlock_employeePhone"]')).to_have_text("0987654321")
        expect(new_tab.locator('[class*="ClientBlock_employeeDuration"]')).to_have_text("00:00:38")
        expect(new_tab.locator('[aria-label="Применение GPT правила"]')).to_have_count(1)
        expect(new_tab.locator('[aria-label="Перетегировать"]')).to_have_count(1)
        expect(new_tab.locator('[aria-label="Скачать"]')).to_have_count(1)
        expect(new_tab.locator('[aria-label="Excel экспорт"]')).to_have_count(1)
        expect(new_tab.locator('[aria-label="Скопировать публичную ссылку"]')).to_have_count(1)
        expect(new_tab.locator('[class*="styles_withAllComments_"]')).to_have_count(1)
        expect(new_tab.get_by_text("Добавить комментарий")).to_have_count(1)
        expect(new_tab.locator('[class*="_manualGroup_"]')).to_have_count(1)

    with allure.step("Change user in new tab. https://task.imot.io/browse/DEV-3239"):
        # page.wait_for_timeout(3000)
        # communications.go_to_user("Экотелеком")
        # page.wait_for_timeout(5000)
        # page.wait_for_load_state(state="load", timeout=wait_until_visible)
        #
        # page.wait_for_selector('[value="6204e7cb599aff4f43f5d3a0"]', state="hidden")
        # page.wait_for_timeout(10000)

        new_tab.locator("#react-select-2-input").type("Экотелеком", delay=30)
        new_tab.get_by_text("Экотелеком", exact=True).click()
        new_tab.wait_for_load_state(state="load", timeout=wait_until_visible)
        new_tab.wait_for_timeout(2000)


    with allure.step("Check"):
        new_tab.wait_for_timeout(2500)
        expect(new_tab.locator(AUDIO_PLAYER)).to_have_count(1)
        expect(new_tab.locator('[class*="MuiAccordionSummary-content"]')).to_have_count(1)
        expect(new_tab.locator('[class*="ClientBlock_employeePhone"]')).to_have_text("0987654321")
        expect(new_tab.locator('[class*="ClientBlock_employeeDuration"]')).to_have_text("00:00:38")
        expect(new_tab.locator('[aria-label="Применение GPT правила"]')).to_have_count(1)
        expect(new_tab.locator('[aria-label="Перетегировать"]')).to_have_count(1)
        expect(new_tab.locator('[aria-label="Скачать"]')).to_have_count(1)
        expect(new_tab.locator('[aria-label="Excel экспорт"]')).to_have_count(1)
        expect(new_tab.locator('[aria-label="Скопировать публичную ссылку"]')).to_have_count(1)
        expect(new_tab.locator('[class*="styles_withAllComments_"]')).to_have_count(1)
        expect(new_tab.get_by_text("Добавить комментарий")).to_have_count(1)
        expect(new_tab.locator('[class*="_manualGroup_"]')).to_have_count(1)

    with allure.step("Close context"):
        new_tab.close()

    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN_ADMIN, USER_ID_ADMIN)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)
#----------

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
        communications.press_calls_list_download_button(0)

    with allure.step("Check content of button download"):
        expect(page.locator(MENU)).to_have_text("Экспорт аудиоЭкспорт расшифровкиЭкспорт коммуникаций")

    with allure.step("Choose (Export audio) option from opened menu"):
        # Start waiting for the download
        with page.expect_download(timeout=60000) as download_info:
            # Perform the action that initiates download
            page.locator(MENU).get_by_text("Экспорт аудио", exact=True).click()
        download = download_info.value
        path = f'{os.getcwd()}/'

        # Wait for the download process to complete and save the downloaded file somewhere
        download.save_as(path + download.suggested_filename)

    with allure.step("Check that export (zip) downloaded"):
        assert os.path.isfile(path + download.suggested_filename) == True
        assert 120000 < os.path.getsize(path + download.suggested_filename) < 160000

    with allure.step("Remove downloaded export (zip)"):
        os.remove(path + download.suggested_filename)

    with allure.step("Check that downloaded export (zip) removed"):
        assert os.path.isfile(path + download.suggested_filename) == False


    with allure.step("Press button (Download)"):
        communications.press_calls_list_download_button(0)

    with allure.step("Press (Export)"):
        page.locator(MENU).get_by_text("Экспорт расшифровки", exact=True).click()
        page.wait_for_selector(MODAL_WINDOW)

    with allure.step("Choose (Export transcribe) option from opened menu"):
        # Start waiting for the download
        with page.expect_download(timeout=60000) as download_info:
            # Perform the action that initiates download
            page.locator(MODAL_WINDOW).get_by_text("Экспортировать", exact=True).click()
        download = download_info.value
        path = f'{os.getcwd()}/'
        # Wait for the download process to complete and save the downloaded file somewhere
        download.save_as(path + download.suggested_filename)

    with allure.step("Check that export (zip) downloaded"):
        assert os.path.isfile(path + download.suggested_filename) == True
        assert 7000 < os.path.getsize(path + download.suggested_filename) < 9000

    with allure.step("Remove downloaded export (zip)"):
        os.remove(path + download.suggested_filename)

    with allure.step("Check that downloaded export (zip) removed"):
        assert os.path.isfile(path + download.suggested_filename) == False

    with allure.step("Close modal with export"):
        page.wait_for_selector(BUTTON_CROSS, timeout=wait_until_visible)
        page.locator(BUTTON_CROSS).click()
        page.wait_for_selector(MODAL_WINDOW, state="hidden")

    #@
    with allure.step("Press button (Download)"):
        communications.press_calls_list_download_button(0)

    with allure.step("Press (Export)"):
        page.locator(MENU).get_by_text("Экспорт коммуникаций", exact=True).click()
        page.wait_for_selector(MODAL_WINDOW)

    with allure.step("Choose (Export transcribe) option from opened menu"):
        # Start waiting for the download
        with page.expect_download(timeout=60000) as download_info:
            # Perform the action that initiates download
            page.locator(MODAL_WINDOW).get_by_text("Экспортировать", exact=True).click()
        download = download_info.value
        path = f'{os.getcwd()}/'

        # Wait for the download process to complete and save the downloaded file somewhere
        download.save_as(path + download.suggested_filename)

    with allure.step("Check that export (zip) downloaded"):
        assert os.path.isfile(path + download.suggested_filename) == True
        assert 6000 < os.path.getsize(path + download.suggested_filename) < 7000

    with allure.step("Remove downloaded export (zip)"):
        os.remove(path + download.suggested_filename)

    with allure.step("Check that downloaded export (zip) removed"):
        assert os.path.isfile(path + download.suggested_filename) == False

    with allure.step("Close modal with export"):
        page.wait_for_selector(BUTTON_CROSS, timeout=wait_until_visible)
        page.locator(BUTTON_CROSS).click()
        page.wait_for_selector(MODAL_WINDOW, state="hidden")



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
        communications.expand_call()

    with allure.step("Check that all 6 buttons in expanded call visible"):
        expect(page.locator(OPEN_CALL_AREA).locator('[aria-label="Переход в источник коммуникации"]')).to_be_visible()
        expect(page.locator(OPEN_CALL_AREA).locator('[aria-label="Применение GPT правила"]')).to_be_visible()
        expect(page.locator(OPEN_CALL_AREA).locator('[aria-label="Перетегировать"]')).to_be_visible()
        expect(page.locator(OPEN_CALL_AREA).locator('[aria-label="Скачать"]')).to_be_visible()
        expect(page.locator(OPEN_CALL_AREA).locator('[aria-label="Excel экспорт"]')).to_be_visible()
        expect(page.locator(OPEN_CALL_AREA).locator('[aria-label="Скопировать публичную ссылку"]')).to_be_visible()
        expect(page.locator(OPEN_CALL_AREA).locator(BUTTON_CALLS_ACTION)).to_be_visible()

    with allure.step("Click button (calls action)"):
        page.locator(OPEN_CALL_AREA).locator(BUTTON_CALLS_ACTION).locator('[type="button"]').click()

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

    with allure.step("Expand call"):
        communications.expand_call()

    with allure.step("Press (Download) button and download file"):
        # Start waiting for the download
        with page.expect_download(timeout=60000) as download_info:
            # Perform the action that initiates download
            page.wait_for_timeout(1000)
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

    with allure.step("Fill first ID to find call"):
        page.wait_for_selector(INPUT_ID, timeout=wait_until_visible)
        page.locator(INPUT_ID).locator('[type="text"]').type("1644268426.90181", delay=20)
        page.wait_for_timeout(500)

    with allure.step("Press button (Find communications)"):
        communications.press_find_communications_less_than_50()

    with allure.step("Expand call"):
        communications.expand_call()

    with allure.step("Press (EX) button"):
        communications.press_ex_button_in_expanded_call()

    with allure.step("Check content of modal window"):
        expect(page.locator(MODAL_WINDOW).get_by_text("Теги без значений")).to_have_count(1)
        expect(page.locator(MODAL_WINDOW).get_by_text("Теги со значениями")).to_have_count(1)
        expect(page.locator(MODAL_WINDOW).get_by_text("Параметры коммуникаций")).to_have_count(1)

    with allure.step(" and download excel"):
        # Start waiting for the download
        with page.expect_download(timeout=60000) as download_info:
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

    with allure.step("Close export modal"):
        page.wait_for_selector(BUTTON_CROSS, timeout=wait_until_visible)
        page.locator(BUTTON_CROSS).click()
        page.wait_for_selector(MODAL_WINDOW, state="hidden")

    with allure.step("Fill second ID to find call"):
        page.wait_for_selector(INPUT_ID, timeout=wait_until_visible)
        page.locator(INPUT_ID).locator('[type="text"]').clear()
        page.locator(INPUT_ID).locator('[type="text"]').type("1644268692.90190", delay=20)
        page.wait_for_timeout(500)

    with allure.step("Press button (Find communications)"):
        communications.press_find_communications_less_than_50()

    with allure.step("Expand call"):
        communications.expand_call()

    with allure.step("Press (EX) button"):
        communications.press_ex_button_in_expanded_call()

    with allure.step("Check content of modal window"):
        expect(page.locator(MODAL_WINDOW).get_by_text("Теги без значений")).to_have_count(1)
        expect(page.locator(MODAL_WINDOW).get_by_text("Теги со значениями")).to_have_count(1)
        expect(page.locator(MODAL_WINDOW).get_by_text("Параметры коммуникаций")).to_have_count(1)

    with allure.step(" and download excel"):
        # Start waiting for the download
        with page.expect_download(timeout=60000) as download_info:
            # Perform the action that initiates download
            page.locator(MODAL_WINDOW).locator('[class*="buttonsBlock_"]').get_by_role("button", name="Экспортировать").click()
        download = download_info.value
        path = f'{os.getcwd()}/'

        # Wait for the download process to complete and save the downloaded file somewhere
        download.save_as(path + download.suggested_filename)

    with allure.step("Check that excel export downloaded"):
        assert os.path.isfile(path + download.suggested_filename) == True
        assert os.path.getsize(path + download.suggested_filename) > 7100

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

    with allure.step("Check that no any templates"):
        communications.assert_template_name("Сохраненные шаблоны поиска(0)")

    with allure.step("Save template"):
        communications.press_save_template()

    with allure.step("Check that (add) button disabled"):
        expect(page.locator(MODAL_WINDOW).locator(BUTTON_SUBMIT)).to_be_disabled()

    with allure.step("Fill template name"):
        page.locator(INPUT_NAME).type("firstTemplate", delay=30)

    with allure.step("Check that (add) button enabled"):
        expect(page.locator(MODAL_WINDOW).locator(BUTTON_SUBMIT)).to_be_enabled()

    with allure.step("Press (add)"):
        page.locator(MODAL_WINDOW).locator(BUTTON_SUBMIT).click()

    with allure.step("Check that template saved"):
        communications.assert_template_name("firstTemplate(1)")

    with allure.step("Rename template"):
        communications.press_rename_template()

    with allure.step("Check that (add) button disabled"):
        expect(page.locator(MODAL_WINDOW).locator(BUTTON_SUBMIT)).to_be_disabled()

    with allure.step("Fill template name"):
        page.locator(INPUT_NAME).type("renameTemplate", delay=30)

    with allure.step("Check that (add) button enabled"):
        expect(page.locator(MODAL_WINDOW).locator(BUTTON_SUBMIT)).to_be_enabled()

    with allure.step("Press (add)"):
        page.locator(MODAL_WINDOW).locator(BUTTON_SUBMIT).click()

    with allure.step("Check that template saved"):
        communications.assert_template_name("renameTemplate(1)")

    with allure.step("Delete template"):
        communications.press_delete_template()

    with allure.step("Press (cancel)"):
        page.get_by_role("button", name="Отмена").click()

    with allure.step("Delete template"):
        communications.press_delete_template()

    with allure.step("Confirm delete"):
        page.locator(MODAL_WINDOW).locator(BUTTON_SUBMIT).click()
        page.wait_for_timeout(2000)

    with allure.step("Check that template saved"):
        communications.assert_template_name("Сохраненные шаблоны поиска(0)")

    # with allure.step("Check stupid text"):
    #     expect(page.locator('[style="font-size: 13px; margin-top: 15px;"]').get_by_text("Поиск пуст. Добавить фильтры можно с помощь 'Изменить фильтры'")).to_be_visible()

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

    with allure.step("Expand call"):
        communications.expand_call()

    with allure.step("Press (add comment)"):
        communications.press_add_comment()

    with allure.step("Check that comment form openned"):
        page.wait_for_timeout(1000)
        expect(page.locator(ALL_COMMENTS_AREA).locator('[type="button"]').nth(1)).to_be_disabled()
        expect(page.locator(ALL_COMMENTS_AREA).locator('[type="checkbox"]')).not_to_be_checked()

    with allure.step("Check that we can close comment form with X"):
        page.locator(BUTTON_CROSS).click()

    with allure.step("Press (add comment)"):
        communications.press_add_comment()

    with allure.step("Check checkbox (hidden)"):
        page.locator(ALL_COMMENTS_AREA).locator('[type="checkbox"]').check()

    with allure.step("Add title"):
        page.locator(BUTTON_ADD_COMMENT_TITLE).click()

    with allure.step("Fill title"):
        page.locator('[id*="post_comment_"]').locator('[class*="styles_title_"]').type("CommentTitle", delay=20)

    with allure.step("Check that button (add comment) still disabled"):
        expect(page.locator(ALL_COMMENTS_AREA).locator('[type="button"]').nth(1)).to_be_disabled()

    with allure.step("Fill comment"):
        page.locator('[class*="styles_textareaWrapper"]').locator('[class*="styles_textarea_"]').type("CommentText", delay=20)

    with allure.step("Press (add comment)"):
        page.locator(ALL_COMMENTS_AREA).locator('[type="button"]').nth(1).click()
        page.wait_for_timeout(1000)

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
        page.wait_for_selector(MENU)

    with allure.step("Choose and click (delete)"):
        page.locator(MENU).get_by_text("Удалить комментарий", exact=True).click()
        page.wait_for_timeout(500)
        page.wait_for_selector(MODAL_WINDOW)

    with allure.step("Confirm deleting"):
        page.locator(MODAL_WINDOW).get_by_role("button", name="Удалить").click()
        page.wait_for_selector(MODAL_WINDOW, state="hidden")
        page.wait_for_timeout(500)

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
    communications = Communications(page)

    expected_languages = ("Английский (Великобритания)Английский (США)Испанский (Латинская Америка, Карибский регион, "
                          "код региона UN M49)Испанский (Испания)Французский (Франция)Португальский "
                          "(Бразилия)Португальский (Португалия)РусскийТурецкий (Турция)УкраинскийУзбекскийАвто")

    expected_engines = "DeepgramHappyscribeNLab SpeechIMOT.IOwhisperЯндексyandex_v3"
    #expected_engines = "DeepgramgigaamHappyscribenexaraNLab SpeechIMOT.IOwhisperЯндексyandex_v3"


    alert_merge = "Опция 'Объединить дорожки в один файл' не может быть выбрана одновременно с любой из диаризаций"

    alert_diarization = "Выберите только одну диаризацию среди опций"

    action_started = "Действие начато"

    with allure.step("Create admin"):
        USER_ID, TOKEN, LOGIN= create_user(API_URL, ROLE_ADMIN, PASSWORD)

    with allure.step("Go to url"):
        communications.navigate(base_url)

    with allure.step("Auth with admin"):
        communications.auth(LOGIN, PASSWORD)

    with allure.step("Go to user"):
        communications.go_to_user("Экотелеком")

    with allure.step("Choose period from 01/01/2022 to 31/12/2022"):
        communications.choose_period_date("01/01/2022", "31/12/2022")

    with allure.step("Fill ID"):
        page.locator(INPUT_ID).locator('[type="text"]').type("1644396067.1832", delay=30)
        page.wait_for_timeout(500)

    with allure.step("Press button (Find communications)"):
        communications.press_find_communications_less_than_50()

    with allure.step("Check"):
        communications.assert_communications_found("Найдено коммуникаций 1 из 3130")

    with allure.step("Click calls list actions button (...)"):
        communications.press_calls_action_button_in_list(0)

    with allure.step("Choose re-recognize in menu"):
        page.locator(MENU).get_by_text("Перераспознать", exact=True).click()
        page.wait_for_timeout(1000)
        page.wait_for_selector(MODAL_WINDOW)

    with allure.step("Check modal window content"):
        expect(page.locator('[class*="styles_sttAllFoudCalls_"]')).to_contain_text(" (количество коммуникаций:  1)")
        expect(page.locator(SELECT_LANGUAGE)).to_contain_text("Русский")
        expect(page.locator(MODAL_WINDOW).locator(BUTTON_CROSS)).to_have_count(1)
        expect(page.locator(MODAL_WINDOW).locator(BUTTON_SUBMIT)).to_contain_text("Перераспознать")

#  check all combinations of engines and models

    with allure.step("Click to language"):
        communications.click_language_select()

    with allure.step("Check language list"):
        communications.assert_menu_values(expected_languages)

    with allure.step("Close language menu"):
        page.locator('[class*="STT_order_"]').click()

    # for ecotelecom engine and model already selected
    # with allure.step("Check that engine not selected"):
    #     expect(page.locator(SELECT_ENGINE)).to_contain_text("Выберите движок")

    # with allure.step("Check that model not selected"):
    #     expect(page.locator(SELECT_MODEL)).to_contain_text("Выберите модель")

    with allure.step("Click to engine"):
        communications.click_engine_select()

    with allure.step("Check engine list"):
        communications.assert_menu_values(expected_engines)

    with allure.step("Click to engine"):
        communications.click_engine_select()

    with allure.step("Choose Deepgram"):
        communications.choose_option(0)

    with allure.step("Click to model"):
        communications.click_model_select()

    with allure.step("Check model list"):
        communications.assert_menu_values("Обобщённаяwhisper")

    with allure.step("Select model Обобщённая"):
        communications.choose_option(0)

    with allure.step("Click to model"):
        communications.click_model_select()

    with allure.step("Select model whisper"):
        communications.choose_option(1)

    with allure.step("Check engine parameters"):
        expect(page.locator(SELECT_ENGINE)).to_contain_text("Deepgram")
        expect(page.locator(SELECT_MODEL)).to_contain_text("whisper")
        expect(page.locator(CHECKBOX_MERGE_ALL_TO_ONE)).not_to_be_checked()
        expect(page.locator(RECOGNITION_PRIORITY).locator('[type="number"]')).to_have_value("1")
        expect(page.locator(CHECKBOX_DIARIZATION)).not_to_be_checked()
        expect(page.locator(CHECKBOX_ECONOMIZE)).to_be_checked()
        expect(page.locator('[type="checkbox"]')).to_have_count(3)

    with allure.step("Click to engine"):
        communications.click_engine_select()

    with allure.step("Choose Happyscribe"):
        communications.choose_option(1)

    with allure.step("Click to model"):
        communications.click_model_select()

    with allure.step("Check model list"):
        communications.assert_menu_values("Стандарт")

    with allure.step("Select model Стандарт"):
        communications.choose_option(0)

    with allure.step("Check engine parameters"):
        expect(page.locator(SELECT_ENGINE)).to_contain_text("Happyscribe")
        expect(page.locator(SELECT_MODEL)).to_contain_text("Стандарт")
        expect(page.locator(CHECKBOX_MERGE_ALL_TO_ONE)).not_to_be_checked()
        expect(page.locator(RECOGNITION_PRIORITY).locator('[type="number"]')).to_have_value("1")
        expect(page.locator(CHECKBOX_DIARIZATION)).not_to_be_checked()
        expect(page.locator(CHECKBOX_ECONOMIZE)).to_be_checked()
        expect(page.locator('[type="checkbox"]')).to_have_count(3)

    with allure.step("Click to engine"):
        communications.click_engine_select()

    with allure.step("Choose NLab Speech"):
        communications.choose_option(2)

    with allure.step("Click to model"):
        communications.click_model_select()

    with allure.step("Check model list"):
        communications.assert_menu_values("ОбобщённаяЖадный")

    with allure.step("Select model Обобщённая"):
        communications.choose_option(0)

    with allure.step("Click to model"):
        communications.click_model_select()

    with allure.step("Select model Жадный"):
        communications.choose_option(1)

    with allure.step("Check engine parameters"):
        expect(page.locator(SELECT_ENGINE)).to_contain_text("NLab Speech")
        expect(page.locator(SELECT_MODEL)).to_contain_text("Жадный")
        expect(page.locator(CHECKBOX_MERGE_ALL_TO_ONE)).not_to_be_checked()
        expect(page.locator(RECOGNITION_PRIORITY).locator('[type="number"]')).to_have_value("1")
        expect(page.locator(CHECKBOX_DIARIZATION)).not_to_be_checked()
        expect(page.locator(CHECKBOX_ECONOMIZE)).to_be_checked()
        expect(page.locator('[type="checkbox"]')).to_have_count(3)


    with allure.step("Click to engine"):
        communications.click_engine_select()

    with allure.step("Choose IMOT.IO"):
        communications.choose_option(3)

    with allure.step("Click to model"):
        communications.click_model_select()

    with allure.step("Check model list"):
        communications.assert_menu_values("Стандарт")

    with allure.step("Select model Стандарт"):
        communications.choose_option(0)

    with allure.step("Check engine parameters"):
        expect(page.locator(SELECT_ENGINE)).to_contain_text("IMOT.IO")
        expect(page.locator(SELECT_MODEL)).to_contain_text("Стандарт")
        expect(page.locator(CHECKBOX_MERGE_ALL_TO_ONE)).not_to_be_checked()
        expect(page.locator(RECOGNITION_PRIORITY).locator('[type="number"]')).to_have_value("1")
        expect(page.locator(CHECKBOX_DIARIZATION)).not_to_be_checked()
        expect(page.locator(CHECKBOX_ECONOMIZE)).to_be_checked()
        expect(page.locator('[type="checkbox"]')).to_have_count(3)

    with allure.step("Click to engine"):
        communications.click_engine_select()

    with allure.step("Choose whisper"):
        communications.choose_option(4)

    with allure.step("Click to model"):
        communications.click_model_select()

    with allure.step("Check model list"):
        communications.assert_menu_values("Стандарт")

    with allure.step("Select model Стандарт"):
        communications.choose_option(0)

    with allure.step("Check engine parameters"):
        expect(page.locator(SELECT_ENGINE)).to_contain_text("whisper")
        expect(page.locator(SELECT_MODEL)).to_contain_text("Стандарт")
        expect(page.locator(CHECKBOX_MERGE_ALL_TO_ONE)).not_to_be_checked()
        expect(page.locator(RECOGNITION_PRIORITY).locator('[type="number"]')).to_have_value("1")
        expect(page.locator(CHECKBOX_DIARIZATION)).not_to_be_checked()
        expect(page.locator(CHECKBOX_ECONOMIZE)).to_be_checked()
        expect(page.locator('[type="checkbox"]')).to_have_count(5)

    with allure.step("Click to engine"):
        communications.click_engine_select()

    with allure.step("Choose Яндекс"):
        communications.choose_option(5)

    with allure.step("Click to model"):
        communications.click_model_select()

    with allure.step("Check model list"):
        communications.assert_menu_values("Отложенная обобщённаяОбобщённая")

    with allure.step("Select model Отложенная обобщённая"):
        communications.choose_option(0)

    with allure.step("Click to model"):
        communications.click_model_select()

    with allure.step("Select model Обобщённая"):
        communications.choose_option(1)

    with allure.step("Check engine parameters"):
        expect(page.locator(SELECT_ENGINE)).to_contain_text("Яндекс")
        expect(page.locator(SELECT_MODEL)).to_contain_text("Обобщённая")
        expect(page.locator(CHECKBOX_MERGE_ALL_TO_ONE)).to_be_checked()
        expect(page.locator(RECOGNITION_PRIORITY).locator('[type="number"]')).to_have_value("1")
        expect(page.locator(CHECKBOX_DIARIZATION)).not_to_be_checked()
        expect(page.locator(CHECKBOX_ECONOMIZE)).to_be_checked()
        expect(page.locator('[type="checkbox"]')).to_have_count(3)

    with allure.step("Click to engine"):
        communications.click_engine_select()

    with allure.step("Choose yandex_v3"):
        communications.choose_option(6)

    with allure.step("Click to model"):
        communications.click_model_select()

    with allure.step("Check model list"):
        communications.assert_menu_values("Отложенная обобщённаяОбобщённая")

    with allure.step("Select model Отложенная обобщённая"):
        communications.choose_option(0)

    with allure.step("Click to model"):
        communications.click_model_select()

    with allure.step("Select model Обобщённая"):
        communications.choose_option(1)

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
        communications.click_engine_select()

    with allure.step("Choose yandex_v3"):
        communications.choose_option(6)

    with allure.step("Check (Save) button is disabled"):
        expect(page.locator(BLOCK_WITH_BUTTON).locator(BUTTON_SUBMIT)).to_be_enabled()

    with allure.step("Click to model"):
        communications.click_model_select()

    with allure.step("Select model best"):
        communications.choose_option(0)

    with allure.step("Check (Save) button is enabled"):
        expect(page.locator(BLOCK_WITH_BUTTON).locator(BUTTON_SUBMIT)).to_be_enabled()

    with allure.step("Check merge all to one checkbox"):
        page.locator(CHECKBOX_MERGE_ALL_TO_ONE).set_checked(checked=True)

    with allure.step("Try to save"):
        communications.click_submit_in_word_processing()

    with allure.step("Wait for alert and check alert message"):
        communications.check_alert(alert_merge)

    with allure.step("Uncheck merge all to one checkbox"):
        page.locator(CHECKBOX_MERGE_ALL_TO_ONE).uncheck()

    with allure.step("Check diarization checkbox"):
        page.locator(CHECKBOX_DIARIZATION).set_checked(checked=True)

    with allure.step("Try to save"):
        communications.click_submit_in_word_processing()

    with allure.step("Wait for alert and check alert message"):
        communications.check_alert(alert_diarization)

    with allure.step("Uncheck diarization checkbox"):
        page.locator(CHECKBOX_DIARIZATION).uncheck()

    with allure.step("Change parameters"):
        page.locator(RECOGNITION_PRIORITY).locator('[type="number"]').fill("10")
        page.locator(CHECKBOX_ECONOMIZE).set_checked(checked=True)
        #page.locator(CHECKBOX_USE_WEBHOOK).set_checked(checked=True)

    with allure.step("Press (Save)"):
        communications.click_submit_in_word_processing()

    with allure.step("Wait for alert and check alert message"):
        page.wait_for_selector('[class*="SnackbarItem"]', timeout=wait_until_visible)
        # expect(page.locator('[class*="SnackbarItem"]')).to_contain_text(action_started)
        # page.wait_for_selector('[class*="SnackbarItem"]', state="hidden", timeout=wait_until_visible)

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
    # expected_engines = "DeepgramgigaamHappyscribenexaraNLab SpeechIMOT.IOwhisperЯндексyandex_v3"

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
        communications.go_to_user("Экотелеком")

    with allure.step("Choose period from 01/01/2022 to 31/12/2022"):
        communications.choose_period_date("01/01/2022", "31/12/2022")

    with allure.step("Fill ID"):
        page.locator(INPUT_ID).locator('[type="text"]').type("1644396067.1832", delay=50)
        page.wait_for_timeout(500)

    with allure.step("Press button (Find communications)"):
        communications.press_find_communications_less_than_50()

    with allure.step("Check"):
        communications.assert_communications_found("Найдено коммуникаций 1 из 3130")

    with allure.step("Expand call"):
        communications.expand_call()

    with allure.step("Click calls list actions button (...)"):
        communications.press_calls_action_button_in_list(1)

    with allure.step("Choose re-recognize in menu"):
        page.locator(MENU).get_by_text("Перераспознать", exact=True).click()
        page.wait_for_selector(MODAL_WINDOW)

    with allure.step("Check modal window content"):
        expect(page.locator(SELECT_LANGUAGE)).to_contain_text("Русский")
        expect(page.locator(MODAL_WINDOW).locator(BUTTON_CROSS)).to_have_count(1)
        expect(page.locator(MODAL_WINDOW).locator(BUTTON_SUBMIT)).to_contain_text("Перераспознать")
#  check all combinations of engines and models

    with allure.step("Click to language"):
        communications.click_language_select()

    with allure.step("Check language list"):
        communications.assert_menu_values(expected_languages)

    with allure.step("Close language menu"):
        page.locator('[class*="STT_order_"]').click()

    # for ecotelecom engine and model already selected
    # with allure.step("Check that engine not selected"):
    #     expect(page.locator(SELECT_ENGINE)).to_contain_text("Выберите движок")

    # with allure.step("Check that model not selected"):
    #     expect(page.locator(SELECT_MODEL)).to_contain_text("Выберите модель")

    with allure.step("Click to engine"):
        communications.click_engine_select()

    with allure.step("Check engine list"):
        communications.assert_menu_values(expected_engines)

    with allure.step("Click to engine"):
        communications.click_engine_select()

    with allure.step("Choose Deepgram"):
        communications.choose_option(0)

    with allure.step("Click to model"):
        communications.click_model_select()

    with allure.step("Check model list"):
        communications.assert_menu_values("Обобщённаяwhisper")

    with allure.step("Select model Обобщённая"):
        communications.choose_option(0)

    with allure.step("Click to model"):
        communications.click_model_select()

    with allure.step("Select model whisper"):
        communications.choose_option(1)

    with allure.step("Check engine parameters"):
        expect(page.locator(SELECT_ENGINE)).to_contain_text("Deepgram")
        expect(page.locator(SELECT_MODEL)).to_contain_text("whisper")
        expect(page.locator(CHECKBOX_MERGE_ALL_TO_ONE)).not_to_be_checked()
        expect(page.locator(RECOGNITION_PRIORITY).locator('[type="number"]')).to_have_value("1")
        expect(page.locator(CHECKBOX_DIARIZATION)).not_to_be_checked()
        expect(page.locator(CHECKBOX_ECONOMIZE)).to_be_checked()
        expect(page.locator('[type="checkbox"]')).to_have_count(3)

    with allure.step("Click to engine"):
        communications.click_engine_select()

    with allure.step("Choose Happyscribe"):
        communications.choose_option(1)

    with allure.step("Click to model"):
        communications.click_model_select()

    with allure.step("Check model list"):
        communications.assert_menu_values("Стандарт")

    with allure.step("Select model Стандарт"):
        communications.choose_option(0)

    with allure.step("Check engine parameters"):
        expect(page.locator(SELECT_ENGINE)).to_contain_text("Happyscribe")
        expect(page.locator(SELECT_MODEL)).to_contain_text("Стандарт")
        expect(page.locator(CHECKBOX_MERGE_ALL_TO_ONE)).not_to_be_checked()
        expect(page.locator(RECOGNITION_PRIORITY).locator('[type="number"]')).to_have_value("1")
        expect(page.locator(CHECKBOX_DIARIZATION)).not_to_be_checked()
        expect(page.locator(CHECKBOX_ECONOMIZE)).to_be_checked()
        expect(page.locator('[type="checkbox"]')).to_have_count(3)

    with allure.step("Click to engine"):
        communications.click_engine_select()

    with allure.step("Choose NLab Speech"):
        communications.choose_option(2)

    with allure.step("Click to model"):
        communications.click_model_select()

    with allure.step("Check model list"):
        communications.assert_menu_values("ОбобщённаяЖадный")

    with allure.step("Select model Обобщённая"):
        communications.choose_option(0)

    with allure.step("Click to model"):
        communications.click_model_select()

    with allure.step("Select model Жадный"):
        communications.choose_option(1)

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
        communications.click_engine_select()

    with allure.step("Choose IMOT.IO"):
        communications.choose_option(3)

    with allure.step("Click to model"):
        communications.click_model_select()

    with allure.step("Check model list"):
        communications.assert_menu_values("Стандарт")

    with allure.step("Select model Стандарт"):
        communications.choose_option(0)

    with allure.step("Check engine parameters"):
        expect(page.locator(SELECT_ENGINE)).to_contain_text("IMOT.IO")
        expect(page.locator(SELECT_MODEL)).to_contain_text("Стандарт")
        expect(page.locator(CHECKBOX_MERGE_ALL_TO_ONE)).not_to_be_checked()
        expect(page.locator(RECOGNITION_PRIORITY).locator('[type="number"]')).to_have_value("1")
        expect(page.locator(CHECKBOX_DIARIZATION)).not_to_be_checked()
        expect(page.locator(CHECKBOX_ECONOMIZE)).to_be_checked()
        expect(page.locator('[type="checkbox"]')).to_have_count(3)

    with allure.step("Click to engine"):
        communications.click_engine_select()

    with allure.step("Choose whisper"):
        communications.choose_option(4)

    with allure.step("Click to model"):
        communications.click_model_select()

    with allure.step("Check model list"):
        communications.assert_menu_values("Стандарт")

    with allure.step("Select model Стандарт"):
        communications.choose_option(0)

    with allure.step("Check engine parameters"):
        expect(page.locator(SELECT_ENGINE)).to_contain_text("whisper")
        expect(page.locator(SELECT_MODEL)).to_contain_text("Стандарт")
        expect(page.locator(CHECKBOX_MERGE_ALL_TO_ONE)).not_to_be_checked()
        expect(page.locator(RECOGNITION_PRIORITY).locator('[type="number"]')).to_have_value("1")
        expect(page.locator(CHECKBOX_DIARIZATION)).not_to_be_checked()
        expect(page.locator(CHECKBOX_ECONOMIZE)).to_be_checked()
        expect(page.locator('[type="checkbox"]')).to_have_count(5)

    with allure.step("Click to engine"):
        communications.click_engine_select()

    with allure.step("Choose Яндекс"):
        communications.choose_option(5)

    with allure.step("Click to model"):
        communications.click_model_select()

    with allure.step("Check model list"):
        communications.assert_menu_values("Отложенная обобщённаяОбобщённая")

    with allure.step("Select model Отложенная обобщённая"):
        communications.choose_option(0)

    with allure.step("Click to model"):
        communications.click_model_select()

    with allure.step("Select model Обобщённая"):
        communications.choose_option(1)

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
        communications.click_engine_select()

    with allure.step("Choose yandex_v3"):
        communications.choose_option(6)

    with allure.step("Click to model"):
        communications.click_model_select()

    with allure.step("Check model list"):
        communications.assert_menu_values("Отложенная обобщённаяОбобщённая")

    with allure.step("Select model Отложенная обобщённая"):
        communications.choose_option(0)

    with allure.step("Click to model"):
        communications.click_model_select()

    with allure.step("Select model Обобщённая"):
        communications.choose_option(1)

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
        communications.click_engine_select()

    with allure.step("Choose assembly_ai"):
        communications.choose_option(6)

    with allure.step("Check (Save) button is disabled"):
        expect(page.locator(BLOCK_WITH_BUTTON).locator(BUTTON_SUBMIT)).to_be_enabled()

    with allure.step("Click to model"):
        communications.click_model_select()

    with allure.step("Select model best"):
        communications.choose_option(0)

    with allure.step("Check (Save) button is enabled"):
        expect(page.locator(BLOCK_WITH_BUTTON).locator(BUTTON_SUBMIT)).to_be_enabled()

    with allure.step("Check merge all to one checkbox"):
        page.locator(CHECKBOX_MERGE_ALL_TO_ONE).set_checked(checked=True)

    with allure.step("Try to save"):
        communications.click_submit_in_word_processing()

    with allure.step("Wait for alert and check alert message"):
        communications.check_alert(alert_merge)

    with allure.step("Uncheck merge all to one checkbox"):
        page.locator(CHECKBOX_MERGE_ALL_TO_ONE).uncheck()

    with allure.step("Check diarization checkbox"):
        page.locator(CHECKBOX_DIARIZATION).set_checked(checked=True)

    with allure.step("Try to save"):
        communications.click_submit_in_word_processing()

    with allure.step("Wait for alert and check alert message"):
        communications.check_alert(alert_diarization)

    with allure.step("Uncheck diarization checkbox"):
        page.locator(CHECKBOX_DIARIZATION).uncheck()

    with allure.step("Change parameters"):
        page.locator(RECOGNITION_PRIORITY).locator('[type="number"]').fill("10")
        page.locator(CHECKBOX_ECONOMIZE).set_checked(checked=True)
        #page.locator(CHECKBOX_USE_WEBHOOK).set_checked(checked=True)

    with allure.step("Press (Save)"):
        communications.click_submit_in_word_processing()

    with allure.step("Wait for alert and check alert message"):
        communications.check_alert(action_started)

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

    with allure.step("Expand call"):
        communications.expand_call()

    with allure.step("Press (add manual tag)"):
        communications.press_cross_in_manual_tags()

    with allure.step("Press (Enter) with empty input"):
        communications.press_key("Enter")

    with allure.step("Wait for alert and check alert message"):
        communications.check_alert("Укажите название тега")

    # with allure.step("Press (add manual tag)"):
    #     communications.press_cross_in_manual_tags()

    with allure.step("Press (New tag)"):
        page.wait_for_timeout(600)
        page.locator(SELECT_WITH_SEARCH_MANUAL_TAGS).locator('[class*="_tagGhost_"]').click()
        page.wait_for_timeout(500)
        page.wait_for_selector(SELECT_WITH_SEARCH_MANUAL_TAGS)

    with allure.step("Add manual tag name"):
        communications.add_manual_tag_name("manual_tag")

    with allure.step("Press (add comment)"):
        communications.press_key("Enter")

    with allure.step("Wait for alert and check alert message"):
        communications.check_alert("Тег успешно добавлен")

    with allure.step("Check that we can see 2 manual tags"):
        communications.assert_tags_have_count(2)

    with allure.step("Delete manual call from call header"):
        communications.delete_manual_tag_from_call_header(0)

    with allure.step("Wait for alert and check alert message"):
        communications.check_alert("Тег удален")

    with allure.step("Check that we can see 2 manual tags"):
        communications.assert_tags_have_count(0)
    #

    with allure.step("Kostyl for https://task.imot.io/browse/DEV-3083"):
        page.locator('[class*="_manualGroup_"]').locator('[type="button"]').click()
        page.wait_for_timeout(500)

    with allure.step("Press (add manual tag)"):
        communications.press_cross_in_manual_tags()

    with allure.step("Add manual tag name"):
        communications.add_manual_tag_name("manual_tag")

    with allure.step("Press (add comment)"):
        communications.press_key("Enter")

    with allure.step("Wait for alert and check alert message"):
        communications.check_alert("Тег успешно добавлен")

    with allure.step("Check that we can see 2 manual tags"):
        communications.assert_tags_have_count(2)

    with allure.step("Delete manual tag from manual tags"):
        communications.delete_manual_tag_from_manual_tags(0)

    with allure.step("Wait for alert and check alert message"):
        communications.check_alert("Тег удален")

    with allure.step("Check that we can see 2 manual tags"):
        communications.assert_tags_have_count(0)

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

    with allure.step("Auth with admin"):
        communications.auth(LOGIN_ADMIN, PASSWORD)

    with allure.step("Change user to auto_test_user"):
        communications.go_to_user(LOGIN_USER)

    with allure.step("Press button (Find communications)"):
        communications.press_find_communications_less_than_50()

    with allure.step("Check that 1 communications found. Should be 1 and date today"):
        communications.assert_communications_found("Найдено коммуникаций 1 из 1")

    with allure.step("Go to settings"):
        communications.click_settings()

    with allure.step("Change user to ecotelecom"):
        communications.go_to_user("Экотелеком")

    with allure.step("Go to communications"):
        communications.click_communications()

    with allure.step("Check that all communications found"):
        communications.assert_communications_found("Найдено коммуникаций 0 из 0")

    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN_ADMIN, USER_ID_ADMIN)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)