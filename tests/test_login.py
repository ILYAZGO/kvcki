from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.login import *
from utils.create_delete_user import create_user, delete_user, create_operator
import pytest
import allure


@pytest.mark.independent
@pytest.mark.login
@allure.title("test_login_admin_positive")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_admin_positive(base_url, page: Page) -> None:

    with allure.step("Create admin"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=timeout)

    with allure.step("Auth"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Quit from profile"):
        quit_from_profile(page)

    with allure.step("Check that quit was successful"):
        expect(page.locator(BUTTON_VOITI)).to_be_visible()

    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.login
@allure.title("test_login_manager_positive")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_manager_positive(base_url, page: Page) -> None:

    with allure.step("Create manager"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_MANAGER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=timeout)

    with allure.step("Auth"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Quit from profile"):
        quit_from_profile(page)

    with allure.step("Check that quit was successful"):
        expect(page.locator(BUTTON_VOITI)).to_be_visible()

    with allure.step("Delete manager"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.login
@allure.title("test_login_user_positive")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_user_positive(base_url, page: Page) -> None:

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=timeout)

    with allure.step("Auth"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Quit from profile"):
        quit_from_profile(page)

    with allure.step("Check that quit was successful"):
        expect(page.locator(BUTTON_VOITI)).to_be_visible()

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.login
@allure.title("test_login_operator_positive")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_operator_positive(base_url, page: Page) -> None:

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Create operator"):
        USER_ID_OPERATOR, TOKEN_OPERATOR, LOGIN_OPERATOR = create_operator(API_URL, USER_ID_USER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=timeout)

    with allure.step("Auth"):
        auth(LOGIN_OPERATOR, PASSWORD, page)

    with allure.step("Quit from profile"):
        quit_from_profile(page)

    with allure.step("Check that quit was successful"):
        expect(page.locator(BUTTON_VOITI)).to_be_visible()

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)

    with allure.step("Delete operator"):
        delete_user(API_URL, TOKEN_OPERATOR, USER_ID_OPERATOR)


@pytest.mark.independent
@pytest.mark.login
@allure.title("test_login_user_negotive")
@allure.severity(allure.severity_level.NORMAL)
def test_login_user_negotive(base_url, page: Page) -> None:

    with allure.step("Go to url"):
        page.goto(base_url, timeout=timeout)

    with allure.step("Auth"):
        auth(LOGIN_NEGOTIVE, PASSWORD, page)

    with allure.step("Check that alert message visible"):
        expect(page.locator(ALERT_MESSAGE)).to_be_visible()


@pytest.mark.independent
@pytest.mark.login
@allure.title("test_password_user_negotive")
@allure.severity(allure.severity_level.NORMAL)
def test_password_user_negotive(base_url, page: Page) -> None:
    with allure.step("Go to url"):
        page.goto(base_url, timeout=timeout)

    with allure.step("Auth"):
        auth(USER, PASSWORD_NEGOTIVE, page)

    with allure.step("Check that alert message visible"):
        expect(page.locator(ALERT_MESSAGE)).to_be_visible()