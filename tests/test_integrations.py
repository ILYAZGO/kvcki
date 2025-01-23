from playwright.sync_api import Page, expect
from utils.variables import *
from utils.dates import first_day_week_ago
from pages.integration import *
from utils.create_delete_user import create_user, delete_user
import pytest
import allure
import re


@pytest.mark.independent
@pytest.mark.integration
@allure.title("test_usedesk")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("User making integration with usedesk")
def test_usedesk(base_url, page: Page) -> None:
    integrations = Integrations(page)

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        integrations.navigate(base_url)

    with allure.step("Auth"):
        integrations.auth(LOGIN, PASSWORD)

    with allure.step("Go to settings"):
        integrations.click_settings()

    with allure.step("Go to integrations"):
        integrations.press_integrations_in_menu()

    with allure.step("Press (Connect)"):
        integrations.press_connect()

    with allure.step("Choose Usedesk"):
        integrations.choose_integration("usedesk")

    with allure.step("Input API token"):
        integrations.input_api_token()

    with allure.step("Press (Save)"):
        integrations.press_save()

    with allure.step("Check alert"):
        integrations.check_alert("Данные сохранены")

    with allure.step("Check integration status"):
        expect(page.locator('[class*="styles_statusTitleDisconnected_"]')).to_have_count(1)

    with allure.step("Make integration Active"):
        page.locator('[type="checkbox"]').click()

    with allure.step("Check alert"):
        integrations.check_alert("Данные сохранены")

    with allure.step("Check integration status"):
        expect(page.locator('[class*="styles_statusTitleConnected"]')).to_have_count(1)

    with allure.step("Reload page"):
        integrations.reload_page()

    with allure.step("Check integration status"):
        expect(page.locator('[class*="styles_statusTitleConnected"]')).to_have_count(1)

    with allure.step("Go to integrations"):
        page.locator(BUTTON_INTEGRACII).click()

    with allure.step("Press to (Play) button"):
        integrations.press_play()

    with allure.step("Set period (first_day_week_ago)"):
        integrations.set_date(first_day_week_ago)

    with allure.step("Set calls limit (2)"):
        integrations.set_calls_limit("2")

    with allure.step("Press button create"):
        integrations.press_create()

    with allure.step("Check alert"):
        integrations.check_alert("Задача создана")

    with allure.step("Wait 35 seconds"):
        page.wait_for_timeout(35000)

    with allure.step("Reload page"):
        integrations.reload_page()

    with allure.step("Check that 2 communications downloaded"):
        page.wait_for_selector('[class*=headerRow]')
        expect(page.locator('[role="rowgroup"]').locator('[role="cell"]').nth(4)).to_have_text('2')

    with allure.step("Go to integration history"):
        page.locator('[aria-label="История"]').locator('[type="button"]').click()

    with allure.step("Check that integration have logs"):
        expect(page.locator('[aria-label="Логи интеграции"]')).to_have_count(1)

    with allure.step("Go to logs"):
        page.locator('[aria-label="Логи интеграции"]').locator('[type="button"]').click()

    with allure.step("Check that logs present"):
        page.wait_for_selector('[data-testid="TaskHistoryLogTable_dataTextarea"]', timeout=wait_until_visible)
        textarea = page.locator('[data-testid="TaskHistoryLogTable_dataTextarea"]')
        count = textarea.count()

        assert count > 1

    with allure.step("Go back to integrations list"):
        page.locator('[class*="styles_category"]').nth(0).click()

    with allure.step("Delete integration"):
        integrations.delete_integration()

    with allure.step("Check that integration deleted"):
        expect(page.locator(BUTTON_CONNECT)).to_be_visible()

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.integration
@allure.title("test_search_string")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_search_string")
def test_search_string(base_url, page: Page) -> None:
    integrations = Integrations(page)

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        integrations.navigate(base_url)

    with allure.step("Auth"):
        integrations.auth(LOGIN, PASSWORD)

    with allure.step("Go to settings"):
        integrations.click_settings()

    with allure.step("Go to integrations"):
        integrations.press_integrations_in_menu()

    with allure.step("Press (Connect)"):
        integrations.press_connect()

    with allure.step("Fill search string"):
        page.get_by_role("textbox", name="Поиск").type("za", delay=30)
        page.wait_for_timeout(500)

    with allure.step("Check that search string found something"):
        expect(page.locator('[class*="styles_listItem_"]')).to_have_count(1)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.integration
@allure.title("test_integration_parameters")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_integration_parameters. with ecotelecom")
def test_integration_parameters(base_url, page: Page) -> None:
    integrations = Integrations(page)

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        integrations.navigate(base_url)

    with allure.step("Auth"):
        integrations.auth(ECOTELECOM, ECOPASS)

    with allure.step("Go to settings"):
        integrations.click_settings()

    with allure.step("Go to integrations"):
        integrations.press_integrations_in_menu()

    with allure.step("Go to settings"):
        page.locator('[aria-label="Настройки"]').click()
        page.wait_for_selector('[href*="/parameters"]')

    with allure.step("Go to parameters"):
        page.locator('[href*="/parameters"]').click()

    with allure.step("Check duration limit and skip empty calls are present"):
        expect(page.locator('[data-testid="duration_limit"]').locator('[type="text"]')).to_have_value("50")
        expect(page.locator('[data-testid="skip_empty_calls"]')).to_have_class(re.compile(r"Mui-checked"))