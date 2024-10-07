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
@allure.title("test_mistic_mayorov")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_mistic_mayorov Пн 09 сен 2024 16∶05∶49")
def test_mistic_mayorov(base_url, page: Page) -> None:
    BUTTON_VOITI = "[type='submit']"

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with 0AleberOper"):
        auth("0AleberOper", PASSWORD, page)
        page.wait_for_selector(FIRST_DATE, timeout=wait_until_visible)

    with allure.step("Choose period"):
        page.wait_for_selector(INPUT_PO_TEGAM, timeout=wait_until_visible)
        page.locator(FIRST_DATE).click()
        page.wait_for_timeout(100)
        page.locator(FIRST_DATE).fill("03/09/2024")
        page.wait_for_timeout(300)
        page.locator(LAST_DATE).click()
        page.wait_for_timeout(100)
        page.locator(LAST_DATE).fill("09/09/2024")
        page.wait_for_timeout(300)
        page.keyboard.press("Enter")
        page.wait_for_timeout(300)

    with allure.step("Search coomunications"):
        press_find_communications(page)

    with allure.step("Check"):
        expect(page.locator(NAYDENO_ZVONKOV).nth(0)).to_have_text("Найдено коммуникаций 1212 из 1212", timeout=wait_until_visible)

    with allure.step("Quit from account"):
        page.locator('[aria-label="Профиль"]').get_by_role("button").click()
        page.get_by_text("Выйти", exact=True).click()

    with allure.step("Check that quit was successful"):
        expect(page.locator(BUTTON_VOITI)).to_be_visible()

    with allure.step("Auth with 1AleberOper"):
        auth("1AleberOper", PASSWORD, page)
        page.wait_for_selector(FIRST_DATE)

    with allure.step("Choose period"):
        page.wait_for_selector(INPUT_PO_TEGAM, timeout=wait_until_visible)
        page.locator(FIRST_DATE).click()
        page.wait_for_timeout(100)
        page.locator(FIRST_DATE).fill("03/09/2024")
        page.wait_for_timeout(300)
        page.locator(LAST_DATE).click()
        page.wait_for_timeout(100)
        page.locator(LAST_DATE).fill("09/09/2024")
        page.wait_for_timeout(300)
        page.keyboard.press("Enter")
        page.wait_for_timeout(300)

    with allure.step("Search coomunications"):
        press_find_communications(page)

    with allure.step("Check"):
        expect(page.locator(NAYDENO_ZVONKOV).nth(0)).to_have_text("Найдено коммуникаций 899 из 899",
                                                                  timeout=wait_until_visible)

    with allure.step("Quit from account"):
        page.locator('[aria-label="Профиль"]').get_by_role("button").click()
        page.get_by_text("Выйти", exact=True).click()

    with allure.step("Check that quit was successful"):
        expect(page.locator(BUTTON_VOITI)).to_be_visible()

    with allure.step("Auth with 2AleberOper"):
        auth("2AleberOper", PASSWORD, page)
        page.wait_for_selector(FIRST_DATE)

    with allure.step("Choose period"):
        page.wait_for_selector(INPUT_PO_TEGAM, timeout=wait_until_visible)
        page.locator(FIRST_DATE).click()
        page.wait_for_timeout(100)
        page.locator(FIRST_DATE).fill("03/09/2024")
        page.wait_for_timeout(300)
        page.locator(LAST_DATE).click()
        page.wait_for_timeout(100)
        page.locator(LAST_DATE).fill("09/09/2024")
        page.wait_for_timeout(300)
        page.keyboard.press("Enter")
        page.wait_for_timeout(300)

    with allure.step("Search coomunications"):
        press_find_communications(page)

    with allure.step("Check"):
        expect(page.locator(NAYDENO_ZVONKOV).nth(0)).to_have_text("Найдено коммуникаций 229 из 229",
                                                                  timeout=wait_until_visible)

    with allure.step("Quit from account"):
        page.locator('[aria-label="Профиль"]').get_by_role("button").click()
        page.get_by_text("Выйти", exact=True).click()

    with allure.step("Check that quit was successful"):
        expect(page.locator(BUTTON_VOITI)).to_be_visible()


    with allure.step("Auth with 3AleberOper"):
        auth("3AleberOper", PASSWORD, page)
        page.wait_for_selector(FIRST_DATE)

    with allure.step("Choose period"):
        page.wait_for_selector(INPUT_PO_TEGAM, timeout=wait_until_visible)
        page.locator(FIRST_DATE).click()
        page.wait_for_timeout(100)
        page.locator(FIRST_DATE).fill("03/09/2024")
        page.wait_for_timeout(300)
        page.locator(LAST_DATE).click()
        page.wait_for_timeout(100)
        page.locator(LAST_DATE).fill("09/09/2024")
        page.wait_for_timeout(300)
        page.keyboard.press("Enter")
        page.wait_for_timeout(300)

    with allure.step("Search coomunications"):
        press_find_communications(page)

    with allure.step("Check"):
        expect(page.locator(NAYDENO_ZVONKOV).nth(0)).to_have_text("Найдено коммуникаций 562 из 562",
                                                                  timeout=wait_until_visible)

    with allure.step("Quit from account"):
        page.locator('[aria-label="Профиль"]').get_by_role("button").click()
        page.get_by_text("Выйти", exact=True).click()

    with allure.step("Check that quit was successful"):
        expect(page.locator(BUTTON_VOITI)).to_be_visible()
