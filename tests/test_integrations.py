from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from utils.dates import first_day_week_ago
from pages.communications import *
from pages.integration import *
from utils.create_delete_user import create_user, delete_user
import pytest
import allure


@pytest.mark.dependent
@pytest.mark.integration
@allure.title("test_usedesk")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("User making integration with usedesk")
def test_usedesk(base_url, page: Page) -> None:

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=timeout)

    with allure.step("Auth"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to settings"):
        go_to_settings(page)

    with allure.step("Go to integrations"):
        page.locator(BUTTON_INTEGRACII_IN_MENU).click(timeout=wait_until_visible)

    with allure.step("Press (Connect)"):
        page.locator(BUTTON_PODKLU4IT).click()
        page.wait_for_selector('[alt="AmoCRM"]')

    with allure.step("Choose Usedesk"):
        page.locator(".styles_body__L76ER", has_text="usedesk").get_by_role("button").click()

    with allure.step("Input and save API token"):
        input_save_api_token(page)

    with allure.step("Go to integrations"):
        page.locator(BUTTON_INTEGRACII).click()

    with allure.step("Press to (Play) button"):
        page.wait_for_selector(BUTTON_PLAY)
        page.locator(BUTTON_PLAY).click()

    with allure.step("Set period (first_day_week_ago)"):
        set_date(first_day_week_ago, page)

    with allure.step("Set calls limit (3)"):
        set_calls_limit("3", page)

    with allure.step("Press button create"):
        page.locator(BUTTON_SOZDAT).click()

    with allure.step("Wait 240 seconds"):
        page.wait_for_timeout(240000)

    with allure.step("Reload page"):
        page.reload()

    with allure.step("Check that 3 communications downloaded"):
        page.wait_for_selector('[class*=headerRow]')
        expect(page.locator('[role="rowgroup"]').locator('[role="cell"]').nth(4)).to_have_text('3')

    with allure.step("Delete integration"):
        delete_integration(page)

    with allure.step("Check that integration deleted"):
        expect(page.locator(BUTTON_PODKLU4IT)).to_be_visible()

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.integration
@allure.title("test_search_string")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_search_string")
def test_search_string(base_url, page: Page) -> None:

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=timeout)

    with allure.step("Auth"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to settings"):
        go_to_settings(page)

    with allure.step("Go to integrations"):
        page.locator(BUTTON_INTEGRACII_IN_MENU).click(timeout=wait_until_visible)

    with allure.step("Press (Connect)"):
        page.locator(BUTTON_PODKLU4IT).click()
        page.wait_for_selector('[alt="AmoCRM"]')

    with allure.step("Fill search string"):
        page.get_by_role("textbox", name="Поиск").fill("za")
        page.wait_for_timeout(500)

    with allure.step("Check that search string found something"):
        expect(page.locator('[class*="styles_listItem_"]')).to_have_count(1)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)