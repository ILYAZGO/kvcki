from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.adminbar import *
import pytest
from utils.create_delete_user import create_user, delete_user, give_user_to_manager
import allure


@pytest.mark.independent
@pytest.mark.adminbar
@allure.title("test_admin_bar_with_admin")
@allure.severity(allure.severity_level.NORMAL)
def test_admin_bar_with_admin(base_url, page: Page) -> None:
    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Create admin"):
        USER_ID_ADMIN, TOKEN_ADMIN, LOGIN_ADMIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth"):
        auth(LOGIN_ADMIN, PASSWORD, page)

    with allure.step("Check admin name have count 2"):
        expect(page.get_by_text(LOGIN_ADMIN)).to_have_count(2, timeout=wait_until_visible)

    with allure.step("Go to user"):
        go_to_user(LOGIN_USER, page)

    with allure.step("Check admin name have count 1 and user name have count 1 and users button have count 1"):
        expect(page.get_by_text(LOGIN_ADMIN)).to_have_count(1, timeout=wait_until_visible)
        expect(page.get_by_text(LOGIN_USER, exact=True)).to_have_count(1, timeout=wait_until_visible)
        expect(page.locator(BUTTON_USERS)).to_be_visible()

    with allure.step("Go back in admin"):
        page.locator(BLOCK_ADMIN_BAR).get_by_role("button").click()

    with allure.step("Check admin name have count 2"):
         expect(page.get_by_text(LOGIN_ADMIN)).to_have_count(2, timeout=wait_until_visible)

    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN_ADMIN, USER_ID_ADMIN)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)


@pytest.mark.independent
@pytest.mark.adminbar
@allure.title("test_admin_bar_with_manager")
@allure.severity(allure.severity_level.NORMAL)
def test_admin_bar_with_manager(base_url, page: Page) -> None:

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Create manager"):
        USER_ID_MANAGER, TOKEN_MANAGER, LOGIN_MANAGER = create_user(API_URL, ROLE_MANAGER, PASSWORD)

    with allure.step("Give user to manager"):
        give_user_to_manager(API_URL, USER_ID_MANAGER, USER_ID_USER, TOKEN_MANAGER)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth"):
        auth(LOGIN_MANAGER, PASSWORD, page)

    with allure.step("Check manager name have count 2"):
        expect(page.get_by_text(LOGIN_MANAGER)).to_have_count(2, timeout=wait_until_visible)

    with allure.step("Go to user"):
        go_to_user(LOGIN_USER, page)

    with allure.step("Check manager name have count 1 and user name have count 1 and users button have count 1"):
        expect(page.get_by_text(LOGIN_MANAGER)).to_have_count(1, timeout=wait_until_visible)
        expect(page.get_by_text(LOGIN_USER, exact=True)).to_have_count(1, timeout=wait_until_visible)
        expect(page.locator(BUTTON_USERS)).to_be_visible()

    with allure.step("Go back in manager"):
        page.locator(BLOCK_ADMIN_BAR).get_by_role("button").click()

    with allure.step("Check manager name have count 2"):
        expect(page.get_by_text(LOGIN_MANAGER)).to_have_count(2, timeout=wait_until_visible)

    with allure.step("Delete manager"):
        delete_user(API_URL, TOKEN_MANAGER, USER_ID_MANAGER)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)


@pytest.mark.independent
@pytest.mark.adminbar
@allure.title("test_language_change_by_user")
@allure.severity(allure.severity_level.NORMAL)
def test_language_change_by_user(base_url, page: Page) -> None:

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth"):
        auth(LOGIN_USER, PASSWORD, page)
        page.wait_for_selector('[class*="Hint_question__title"]', timeout=wait_until_visible)

    with allure.step("Change lang from RU to EN"):
        change_lang("RU", "EN", page)

    with allure.step("Check that lang changed"):
        expect(page.get_by_text("Additional filters")).to_be_visible(timeout=wait_until_visible)

    with allure.step("Change lang from EN to ES"):
        change_lang("EN", "ES", page)

    with allure.step("Check that lang changed"):
        expect(page.get_by_text("Filtros adicionales")).to_be_visible(timeout=wait_until_visible)

    with allure.step("Change lang from ES to PT"):
        change_lang("ES", "PT", page)

    with allure.step("Check that lang changed"):
        expect(page.get_by_text("Filtros adicionais")).to_be_visible(timeout=wait_until_visible)

    with allure.step("Change lang from PT to RU"):
        change_lang("PT", "RU", page)

    with allure.step("Check that lang changed"):
        expect(page.get_by_text("Дополнительные фильтры")).to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)