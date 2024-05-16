import os

from playwright.sync_api import Page, expect, BrowserContext
from utils.variables import *
from utils.auth import auth
from pages.calls import *
from utils.dates import *
import pytest
import allure


@pytest.mark.calls
@pytest.mark.independent
@allure.title("test_check_dates")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("Check dates buttons")
def test_check_dates(page: Page) -> None:

    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)

    with allure.step("Auth"):
        auth(ECOTELECOM, ECOPASS, page)
        page.wait_for_selector(FIRST_DATE)

    with allure.step("Check first and last dates in view. Today by default"):
        expect(page.locator(FIRST_DATE)).to_have_value(today)
        expect(page.locator(LAST_DATE)).to_have_value(today)

    with allure.step("Switch to yesterday"):
        page.locator(YESTERDAY).click()

    with allure.step("Check first and last dates in view."):
        expect(page.locator(FIRST_DATE)).to_have_value(yesterday)
        expect(page.locator(LAST_DATE)).to_have_value(yesterday)

    with allure.step("Switch to week"):
        page.locator(WEEK).click()

    with allure.step("Check first and last dates in view."):
        expect(page.locator(FIRST_DATE)).to_have_value(first_day_week_ago)
        expect(page.locator(LAST_DATE)).to_have_value(today)

    with allure.step("Switch to month"):
        page.locator(MONTH).click()

    with allure.step("Check first and last dates in view."):
        expect(page.locator(FIRST_DATE)).to_have_value(first_day_month_ago)
        expect(page.locator(LAST_DATE)).to_have_value(today)

    with allure.step("Switch to year"):
        page.locator(YEAR).click()

    with allure.step("Check first and last dates in view."):
        expect(page.locator(FIRST_DATE)).to_have_value(first_day_year_ago)
        expect(page.locator(LAST_DATE)).to_have_value(today)

    with allure.step("Switch to all time"):
        page.locator(ALL_TIME).click()

    with allure.step("Check begin and end dates is disabled"):
        expect(page.locator(FIRST_DATE)).to_be_disabled()
        expect(page.locator(LAST_DATE)).to_be_disabled()


@pytest.mark.calls
@pytest.mark.independent
@allure.title("test_check_search_all")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Searching all communications for Ecotelecom")
def test_check_search_all(page: Page) -> None:

    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)

    with allure.step("Auth"):
        auth(ECOTELECOM, ECOPASS, page)

    with allure.step("Choose period from 01/01/2022 to 31/12/2022"):
        choose_preiod_date("01/01/2022", "31/12/2022", page)

    with allure.step("Press button (Find communications)"):
        press_find_communications(page)
        page.wait_for_selector(FIRST_PAGE_PAGINATION, timeout=wait_until_visible)

    with allure.step("Check"):
        expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено коммуникаций 3130 из 3130")


@pytest.mark.calls
@pytest.mark.independent
@allure.title("test_check_search_by_client_number")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check search by client number for Ecotelecom")
def test_check_search_by_client_number(page: Page) -> None:

    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)

    with allure.step("Auth"):
        auth(ECOTELECOM, ECOPASS, page)

    with allure.step("Choose period from 01/01/2022 to 31/12/2022"):
        choose_preiod_date("01/01/2022", "31/12/2022", page)

    with allure.step("Fill client number"):
        page.locator(INPUT_NOMER_CLIENTA).locator('[type="text"]').fill("79251579005")

    with allure.step("Press button (Find communications)"):
        press_find_communications(page)

    with allure.step("Check"):
        expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено коммуникаций 14 из 3130", timeout=wait_until_visible)


@pytest.mark.calls
@pytest.mark.independent
@allure.title("test_check_search_by_employee_number")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check search by employee number for Ecotelecom")
def test_check_search_by_employee_number(page: Page) -> None:

    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)

    with allure.step("Auth"):
        auth(ECOTELECOM, ECOPASS, page)

    with allure.step("Choose period from 01/01/2022 to 31/12/2022"):
        choose_preiod_date("01/01/2022", "31/12/2022", page)

    with allure.step("Fill employee number"):
        page.locator(INPUT_NOMER_SOTRUDNIKA).locator('[type="text"]').fill("4995055555")

    with allure.step("Press button (Find communications)"):
        press_find_communications(page)
        page.wait_for_selector(FIRST_PAGE_PAGINATION, timeout=wait_until_visible)

    with allure.step("Check"):
        expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено коммуникаций 670 из 3130", timeout=wait_until_visible)


@pytest.mark.calls
@pytest.mark.independent
@allure.title("test_check_search_by_client_dict_or_text")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check search by client dict or text for Ecotelecom")
def test_check_search_by_client_dict_or_text(page: Page) -> None:

    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)

    with allure.step("Auth"):
        auth(ECOTELECOM, ECOPASS, page)

    with allure.step("Choose period from 01/01/2022 to 31/12/2022"):
        choose_preiod_date("01/01/2022", "31/12/2022", page)

    with allure.step("Fill input with text"):
        page.locator(INPUT_SLOVAR_ILI_TEXT_CLIENT).locator('[type="text"]').fill("адрес")
        page.wait_for_timeout(2400)

    with allure.step("Press button (Find communications)"):
        press_find_communications(page)
        page.wait_for_selector(FIRST_PAGE_PAGINATION, timeout=wait_until_visible)

    with allure.step("Check"):
        expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено коммуникаций 184 из 3130", timeout=wait_until_visible) #152

    with allure.step("Clear, fill input by dict, choose dict from suggestion"):
        page.locator(INPUT_SLOVAR_ILI_TEXT_CLIENT).locator('[type="text"]').clear()
        page.locator(INPUT_SLOVAR_ILI_TEXT_CLIENT).locator('[type="text"]').fill("Зо")
        page.get_by_text("Зомбоящик").click()

    with allure.step("Press button (Find communications)"):
        press_find_communications(page)
        page.wait_for_selector(FIRST_PAGE_PAGINATION, timeout=wait_until_visible)

    with allure.step("Check"):
        expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено коммуникаций 407 из 3130", timeout=wait_until_visible) #410


@pytest.mark.calls
@pytest.mark.independent
@allure.title("test_check_search_by_employee_dict_or_text")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check search by employee dict or text for Ecotelecom")
def test_check_search_by_employee_dict_or_text(page: Page) -> None:

    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)

    with allure.step("Auth"):
        auth(ECOTELECOM, ECOPASS, page)

    with allure.step("Choose period from 01/01/2022 to 31/12/2022"):
        choose_preiod_date("01/01/2022", "31/12/2022", page)

    with allure.step("Fill input with text"):
        page.locator(INPUT_SLOVAR_ILI_TEXT_SOTRUDNIK).locator('[type="text"]').fill("адрес")
        page.wait_for_timeout(2000)

    with allure.step("Press button (Find communications)"):
        press_find_communications(page)
        page.wait_for_selector(FIRST_PAGE_PAGINATION, timeout=wait_until_visible)

    with allure.step("Check"):
        expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено коммуникаций 398 из 3130", timeout=wait_until_visible) #430

    with allure.step("Clear, fill input by dict, choose dict from suggestion"):
        page.locator(INPUT_SLOVAR_ILI_TEXT_SOTRUDNIK).locator('[type="text"]').clear()
        page.locator(INPUT_SLOVAR_ILI_TEXT_SOTRUDNIK).locator('[type="text"]').fill("Зо")
        page.get_by_text("Зомбоящик").click()

    with allure.step("Press button (Find communications)"):
        press_find_communications(page)
        page.wait_for_selector(FIRST_PAGE_PAGINATION, timeout=wait_until_visible)

    with allure.step("Check"):
        expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено коммуникаций 491 из 3130", timeout=wait_until_visible)  #488


@pytest.mark.calls
@pytest.mark.independent
@allure.title("test_check_search_by_exact_time")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check search by exact time for Ecotelecom")
def test_check_search_by_exact_time(page: Page) -> None:

    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)

    with allure.step("Auth"):
        auth(ECOTELECOM, ECOPASS, page)

    with allure.step("Choose period from 01/01/2022 to 31/12/2022"):
        choose_preiod_date("01/01/2022", "31/12/2022", page)

    with allure.step("Fill exact time"):
        page.locator(INPUT_VREMYA_ZVONKA).locator('[type="text"]').fill("11:42")

    with allure.step("Press button (Find communications)"):
        press_find_communications(page)

    with allure.step("Check"):
        expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено коммуникаций 5 из 3130", timeout=wait_until_visible)


@pytest.mark.calls
@pytest.mark.independent
@allure.title("test_check_search_by_length")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check search by length for Ecotelecom")
def test_check_search_by_length(page: Page) -> None:

    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)

    with allure.step("Auth"):
        auth(ECOTELECOM, ECOPASS, page)

    with allure.step("Choose period from 01/01/2022 to 31/12/2022"):
        choose_preiod_date("01/01/2022", "31/12/2022", page)

    with allure.step("Fill length <10"):
        fill_search_length("<10", page)

    with allure.step("Press button (Find communications)"):
        press_find_communications(page)
        page.wait_for_selector(FIRST_PAGE_PAGINATION, timeout=wait_until_visible)

    with allure.step("Check"):
        expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено коммуникаций 443 из 3130", timeout=wait_until_visible)

    with allure.step("Fill length >10"):
        fill_search_length(">10", page)

    with allure.step("Press button (Find communications)"):
        press_find_communications(page)
        page.wait_for_selector(FIRST_PAGE_PAGINATION, timeout=wait_until_visible)

    with allure.step("Check"):
        expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено коммуникаций 2687 из 3130", timeout=wait_until_visible)

    with allure.step("Fill length 1711"):
        fill_search_length("1711", page)

    with allure.step("Press button (Find communications)"):
        press_find_communications(page)

    with allure.step("Check"):
        expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено коммуникаций 1 из 3130", timeout=wait_until_visible)


@pytest.mark.calls
@pytest.mark.independent
@allure.title("test_check_search_by_ID")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check search by ID for Ecotelecom")
def test_check_search_by_ID(page: Page) -> None:

    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)

    with allure.step("Auth"):
        auth(ECOTELECOM, ECOPASS, page)

    with allure.step("Choose period from 01/01/2022 to 31/12/2022"):
        choose_preiod_date("01/01/2022", "31/12/2022", page)

    with allure.step("Fill ID"):
        page.locator(INPUT_ID).locator('[type="text"]').fill("1644474236.14425")

    with allure.step("Press button (Find communications)"):
        press_find_communications(page)

    with allure.step("Check"):
        expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено коммуникаций 1 из 3130", timeout=wait_until_visible)



@pytest.mark.calls
@pytest.mark.independent
@allure.title("test_check_search_by_tag")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check search by tag for Ecotelecom")
def test_check_search_by_tag(page: Page) -> None:

    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)

    with allure.step("Auth"):
        auth(ECOTELECOM, ECOPASS, page)

    with allure.step("Choose period from 01/01/2022 to 31/12/2022"):
        choose_preiod_date("01/01/2022", "31/12/2022", page)

    with allure.step("Fill by tag"):
        page.wait_for_selector(INPUT_PO_TEGAM)
        page.locator(INPUT_PO_TEGAM).locator('[type="text"]').fill("Другой отдел")
        page.wait_for_timeout(2600)
        page.get_by_text("Другой отдел", exact=True).first.click()
        page.locator(POISK_PO_FRAGMENTAM).click()  # tupo click

    with allure.step("Press button (Find communications)"):
        press_find_communications(page)

    with allure.step("Check"):
        expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено коммуникаций 131 из 3130", timeout=wait_until_visible)  #131

    with allure.step("Add extra tag"):
        page.locator(INPUT_PO_TEGAM).locator('[type="text"]').fill("Обсуждение тарифа")
        page.wait_for_timeout(2900)
        page.get_by_text("Обсуждение тарифа", exact=True).first.click()
        page.locator(POISK_PO_FRAGMENTAM).click()  # tupo click

    with allure.step("Press button (Find communications)"):
        press_find_communications(page)

    with allure.step("Check"):
        expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено коммуникаций 46 из 3130", timeout=wait_until_visible) #46

    with allure.step("Click to (Add condition)"):
        page.locator(BUTTON_DOBAVIT_USLOVIE).first.click()

    with allure.step("Change logic operator"):
        page.locator(CHANGE_LOGIC_OPERATOR).click()
        page.get_by_text("НЕТ ВСЕХ").click()

    with allure.step("Add new tag"):
        page.wait_for_selector(INPUT_PO_TEGAM_NEW)
        page.locator(INPUT_PO_TEGAM_NEW).fill("Новое подключение")
        page.wait_for_timeout(2800)
        page.get_by_text("Новое подключение", exact=True).first.click()
        page.locator(POISK_PO_FRAGMENTAM).click()  # tupo click

    with allure.step("Press button (Find communications)"):
        press_find_communications(page)

    with allure.step("Check"):
        expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено коммуникаций 19 из 3130", timeout=wait_until_visible) #19






@pytest.mark.calls
@pytest.mark.independent
@allure.title("test_check_sort")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("Check sort(4 type) all calls for Ecotelecom")
def test_check_sort(page: Page) -> None:

    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)

    with allure.step("Auth"):
        auth(ECOTELECOM, ECOPASS, page)

    with allure.step("Choose period from 01/01/2022 to 31/12/2022"):
        choose_preiod_date("01/01/2022", "31/12/2022", page)

    with allure.step("Press button (Find communications)"):
        press_find_communications(page)
        page.wait_for_selector(FIRST_PAGE_PAGINATION, timeout=wait_until_visible)

    with allure.step("Check all communications count, OLD calls first by default"):
        expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено коммуникаций 3130 из 3130", timeout=wait_until_visible)
        expect(page.locator(CALL_DATE_AND_TIME)).to_have_text("08.02.22 00:12", timeout=wait_until_visible)

    with allure.step("Change sort to NEW FIRST"):
        change_sort("Сначала новые", page)

    with allure.step("Check NEW first in list"):
        expect(page.locator(CALL_DATE_AND_TIME)).to_have_text("16.05.22 18:21", timeout=wait_until_visible)

    with allure.step("Change sort to SHORT FIRST"):
        change_sort("Сначала короткие", page)

    with allure.step("Check SHORT first in list"):
        expect(page.locator(CALL_DATE_AND_TIME)).to_have_text("09.02.22 11:41", timeout=wait_until_visible)

    with allure.step("Change sort to LONG FIRST"):
        change_sort("Сначала длинные", page)

    with allure.step("Check LONG first in list"):
        expect(page.locator(CALL_DATE_AND_TIME)).to_have_text("09.02.22 18:08", timeout=wait_until_visible)



@pytest.mark.calls
@pytest.mark.independent
@allure.title("test_check_clear_all_fields")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("Check clear all fields by button for Ecotelecom")
def test_check_clear_all_fields(page: Page) -> None:

    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)

    with allure.step("Auth"):
        auth(ECOTELECOM, ECOPASS, page)

    with allure.step("Fill all default fields"):
        page.wait_for_selector(INPUT_ID)

        page.locator(INPUT_NOMER_CLIENTA).locator('[type="text"]').fill("79251579005")
        page.locator(POISK_PO_FRAGMENTAM).click()
        page.locator(INPUT_NOMER_SOTRUDNIKA).locator('[type="text"]').fill("4995055555")
        page.locator(POISK_PO_FRAGMENTAM).click()

        page.locator(INPUT_SLOVAR_ILI_TEXT_CLIENT).locator('[type="text"]').fill("адрес")
        page.wait_for_timeout(2600)
        page.locator(POISK_PO_FRAGMENTAM).click()

        page.locator(INPUT_SLOVAR_ILI_TEXT_SOTRUDNIK).locator('[type="text"]').fill("2223")
        page.wait_for_timeout(2600)
        page.locator(POISK_PO_FRAGMENTAM).click()

        fill_search_length(">10", page)
        page.locator(POISK_PO_FRAGMENTAM).click()
        page.locator(INPUT_VREMYA_ZVONKA).locator('[type="text"]').fill("11:42")
        page.locator(POISK_PO_FRAGMENTAM).click()
        page.locator(INPUT_ID).locator('[type="text"]').fill("1644474236.14425")
        page.locator(POISK_PO_FRAGMENTAM).click()

        page.wait_for_selector(INPUT_PO_TEGAM)
        page.locator(INPUT_PO_TEGAM).locator('[type="text"]').fill("Другой отдел")
        page.wait_for_timeout(2600)
        page.get_by_text("Другой отдел", exact=True).first.click()
        page.locator(POISK_PO_FRAGMENTAM).click()

    with allure.step("Check all fields to have value"):
        expect(page.locator('[aria-label="Remove 79251579005"]')).to_be_visible()
        expect(page.locator('[aria-label="Remove 4995055555"]')).to_be_visible()
        expect(page.locator('[aria-label="Remove адрес"]')).to_be_visible()
        expect(page.locator('[aria-label="Remove 2223"]')).to_be_visible()
        expect(page.locator('[aria-label="Remove >10"]')).to_be_visible()
        expect(page.locator('[aria-label="Remove 11:42"]')).to_be_visible()
        expect(page.locator('[aria-label="Remove 1644474236.14425"]')).to_be_visible()
        expect(page.locator('[aria-label="Remove Другой отдел"]')).to_be_visible()

    with allure.step("Press button (Clear)"):
        page.locator('[data-testid="calls_btns_clear"]').click()

    with allure.step("Check that cleared"):
        expect(page.locator('[aria-label="Remove 79251579005"]')).not_to_be_visible()
        expect(page.locator('[aria-label="Remove 4995055555"]')).not_to_be_visible()
        expect(page.locator('[aria-label="Remove адрес"]')).not_to_be_visible()
        expect(page.locator('[aria-label="Remove 2223"]')).not_to_be_visible()
        expect(page.locator('[aria-label="Remove >10"]')).not_to_be_visible()
        expect(page.locator('[aria-label="Remove 11:42"]')).not_to_be_visible()
        expect(page.locator('[aria-label="Remove 1644474236.14425"]')).not_to_be_visible()
        expect(page.locator('[aria-label="Remove Другой отдел"]')).not_to_be_visible()



@pytest.mark.calls
@pytest.mark.independent
@allure.title("test_check_open_call_in_new_tab")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("test_check_open_call_in_new_tab")
def test_check_open_call_in_new_tab(page: Page, context: BrowserContext) -> None:

    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)

    with allure.step("Auth"):
        auth(ECOTELECOM, ECOPASS, page)

    with allure.step("Choose period from 01/01/2022 to 31/12/2022"):
        choose_preiod_date("01/01/2022", "31/12/2022", page)

    with allure.step("Fill ID to find call"):
        page.wait_for_selector(INPUT_ID)
        page.locator(INPUT_ID).locator('[type="text"]').fill("1644268426.90181")

    with allure.step("Press button (Find communications)"):
        press_find_communications(page)

    with allure.step("Open new tab"):
        with context.expect_page() as new_tab_event:
            page.locator('[data-testid="call_share"]').get_by_role("button").click()
            new_tab=new_tab_event.value

    with allure.step("Check"):
        expect(new_tab.locator(AUDIO_PLAYER)).to_have_count(1)
        expect(new_tab.locator('[id="accordionSummary"]')).to_have_count(1)
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
def test_check_content_button_calls_actions(page: Page) -> None:

    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)

    with allure.step("Auth"):
        auth(ECOTELECOM, ECOPASS, page)

    with allure.step("Choose period from 01/01/2022 to 31/12/2022"):
        choose_preiod_date("01/01/2022", "31/12/2022", page)

    with allure.step("Fill ID to find call"):
        page.wait_for_selector(INPUT_ID)
        page.locator(INPUT_ID).locator('[type="text"]').fill("1644268426.90181")

    with allure.step("Press button (Find communications)"):
        press_find_communications(page)

    with allure.step("Press button (Calls action)"):
        page.locator('[data-testid="calls_actions_actions-btn"]').nth(0).click()

    with allure.step("Check content of button (...) calls action"):
        expect(page.locator('[class*="menu"]')).to_have_text("Применить GPTПоменять аудио каналыЗагрузить теги из crmПрименить информированиеПрименить адресную книгуФильтр тегов")


@pytest.mark.calls
@pytest.mark.independent
@allure.title("test_check_content_button_calls_download")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("test_check_content_button_calls (download)")
def test_check_content_button_calls_download(page: Page) -> None:

    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)

    with allure.step("Auth"):
        auth(ECOTELECOM, ECOPASS, page)

    with allure.step("Choose period from 01/01/2022 to 31/12/2022"):
        choose_preiod_date("01/01/2022", "31/12/2022", page)

    with allure.step("Fill ID to find call"):
        page.wait_for_selector(INPUT_ID)
        page.locator(INPUT_ID).locator('[type="text"]').fill("1644268426.90181")

    with allure.step("Press button (Find communications)"):
        press_find_communications(page)

    with allure.step("Press button (Download)"):
        page.locator('[data-testid="calls_actions_download"]').nth(0).click()

    with allure.step("Check content of button download"):
        expect(page.locator('[class*="menu"]')).to_have_text("Экспорт аудиоЭкспорт расшифровкиЭкспорт коммуникаций")


@pytest.mark.calls
@pytest.mark.independent
@allure.title("test_check_buttons_in_open_call")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("test_check_buttons_in_open_call")
def test_check_buttons_in_open_call(page: Page) -> None:

    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)

    with allure.step("Auth"):
        auth(ECOTELECOM, ECOPASS, page)

    with allure.step("Choose period from 01/01/2022 to 31/12/2022"):
        choose_preiod_date("01/01/2022", "31/12/2022", page)

    with allure.step("Fill ID to find call"):
        page.wait_for_selector(INPUT_ID)
        page.locator(INPUT_ID).locator('[type="text"]').fill("1644268426.90181")

    with allure.step("Press button (Find communications)"):
        press_find_communications(page)

    with allure.step("Expand call"):
        page.locator('[data-testid="call_expand"]').click()
        page.wait_for_selector('[id="62050BEC113619D283D9D584-9-0"]')  #  wait word "nu"

    with allure.step("Check that all 6 buttons in expanded call visible"):
        expect(page.locator('[class="MuiAccordion-region"]').locator('[aria-label="Применение GPT правила"]')).to_be_visible()
        expect(page.locator('[class="MuiAccordion-region"]').locator('[aria-label="Перетегировать"]')).to_be_visible()
        expect(page.locator('[class="MuiAccordion-region"]').locator('[aria-label="Скачать"]')).to_be_visible()
        expect(page.locator('[class="MuiAccordion-region"]').locator('[aria-label="Excel экспорт"]')).to_be_visible()
        expect(page.locator('[class="MuiAccordion-region"]').locator('[aria-label="Скопировать публичную ссылку"]')).to_be_visible()
        expect(page.locator('[class="MuiAccordion-region"]').locator('[data-testid="calls_actions_actions-btn"]')).to_be_visible()

    with allure.step("Click button (calls action)"):
        page.locator('[class="MuiAccordion-region"]').locator('[data-testid="calls_actions_actions-btn"]').click()

    with (allure.step("Check content in opened menu")):
        expect(page.locator('[class="MuiAccordion-region"]').locator('[class*="menu"]')).to_have_text("Мета инфоПоменять аудио каналыЗагрузить теги из crmПрименить информированиеПрименить адресную книгуРедактировать правило оповещения ")


@pytest.mark.independent
@allure.title("test_check_download_call_from_expanded_call")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("test_check_download_call_from_expanded_call")
def test_check_download_call_from_expanded_call(page: Page) -> None:

    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)

    with allure.step("Auth"):
        auth(ECOTELECOM, ECOPASS, page)

    with allure.step("Choose period from 01/01/2022 to 31/12/2022"):
        choose_preiod_date("01/01/2022", "31/12/2022", page)

    with allure.step("Fill ID to find call"):
        page.wait_for_selector(INPUT_ID)
        page.locator(INPUT_ID).locator('[type="text"]').fill("1644268426.90181")

    with allure.step("Press button (Find communications)"):
        press_find_communications(page)

    with allure.step("Expand call"):
        page.locator('[data-testid="call_expand"]').click()
        page.wait_for_selector('[id="62050BEC113619D283D9D584-9-0"]')  #  wait word "nu"

    with allure.step("Press (Download) button and download file"):
        # Start waiting for the download
        with page.expect_download(timeout=50000) as download_info:
            # Perform the action that initiates download
            page.locator('[class="MuiAccordion-region"]').locator('[aria-label="Скачать"]').locator('[type="button"]').click()
        download = download_info.value
        path = f'{os.getcwd()}/'

        # Wait for the download process to complete and save the downloaded file somewhere
        download.save_as(path + download.suggested_filename)

    with allure.step("Check that file downloaded"):
        assert os.path.isfile(path + download.suggested_filename) == True

    with allure.step("Remove downloaded file"):
        os.remove(path + download.suggested_filename)

    with allure.step("Check that file removed"):
        assert os.path.isfile(path + download.suggested_filename) == False


@pytest.mark.independent
@allure.title("test_check_download_excel_from_expanded_call")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("test_check_download_excel_from_expanded_call")
def test_check_download_excel_from_expanded_call(page: Page) -> None:

    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)

    with allure.step("Auth"):
        auth(ECOTELECOM, ECOPASS, page)

    with allure.step("Choose period from 01/01/2022 to 31/12/2022"):
        choose_preiod_date("01/01/2022", "31/12/2022", page)

    with allure.step("Fill ID to find call"):
        page.wait_for_selector(INPUT_ID)
        page.locator(INPUT_ID).locator('[type="text"]').fill("1644268426.90181")

    with allure.step("Press button (Find communications)"):
        press_find_communications(page)

    with allure.step("Expand call"):
        page.locator('[data-testid="call_expand"]').click()
        page.wait_for_selector('[id="62050BEC113619D283D9D584-9-0"]')  #  wait word "nu"

    with allure.step("Press (EX) button and download excel"):
        # Start waiting for the download
        with page.expect_download(timeout=50000) as download_info:
            # Perform the action that initiates download
            page.locator('[class="MuiAccordion-region"]').locator('[aria-label="Excel экспорт"]').locator('[type="button"]').click()
        download = download_info.value
        path = f'{os.getcwd()}/'

        # Wait for the download process to complete and save the downloaded file somewhere
        download.save_as(path + download.suggested_filename)

    with allure.step("Check that excel export downloaded"):
        assert os.path.isfile(path + download.suggested_filename) == True

    with allure.step("Remove downloaded excel export"):
        os.remove(path + download.suggested_filename)

    with allure.step("Check that excel export removed"):
        assert os.path.isfile(path + download.suggested_filename) == False