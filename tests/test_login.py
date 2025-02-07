#from playwright.sync_api import Page, expect
from utils.variables import *
from pages.login import *
from utils.create_delete_user import create_user, delete_user, create_operator
import pytest
import allure


"""THIS TEST NOT USEFULL CHECK THIS IN OTHER TESTS"""
# @pytest.mark.independent
# @pytest.mark.login
# @allure.title("test_login_admin_positive")
# @allure.severity(allure.severity_level.CRITICAL)
# def test_login_admin_positive(base_url, page: Page) -> None:
#     login_page = LoginPage(page)
#
#     with allure.step("Create admin"):
#         USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)
#
#     with allure.step("Go to url"):
#         login_page.navigate(base_url)
#
#     with allure.step("Auth"):
#         login_page.auth(LOGIN, PASSWORD)
#
#     with allure.step("Quit from profile"):
#         login_page.quit_from_profile()
#
#     with allure.step("Check that quit was successful"):
#         login_page.assert_quited()
#
#     with allure.step("Delete admin"):
#         delete_user(API_URL, TOKEN, USER_ID)

"""THIS TEST NOT USEFULL CHECK THIS IN OTHER TESTS"""
# @pytest.mark.independent
# @pytest.mark.login
# @allure.title("test_login_manager_positive")
# @allure.severity(allure.severity_level.CRITICAL)
# def test_login_manager_positive(base_url, page: Page) -> None:
#     login_page = LoginPage(page)
#
#     with allure.step("Create manager"):
#         USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_MANAGER, PASSWORD)
#
#     with allure.step("Go to url"):
#         login_page.navigate(base_url)
#
#     with allure.step("Auth"):
#         login_page.auth(LOGIN, PASSWORD)
#
#     with allure.step("Quit from profile"):
#         login_page.quit_from_profile()
#
#     with allure.step("Check that quit was successful"):
#         login_page.assert_quited()
#
#     with allure.step("Delete manager"):
#         delete_user(API_URL, TOKEN, USER_ID)


"""THIS TEST NOT USEFULL CHECK THIS IN OTHER TESTS"""
# @pytest.mark.independent
# @pytest.mark.login
# @allure.title("test_login_user_positive")
# @allure.severity(allure.severity_level.CRITICAL)
# def test_login_user_positive(base_url, page: Page) -> None:
#     login_page = LoginPage(page)
#
#     with allure.step("Create user"):
#         USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)
#
#     with allure.step("Go to url"):
#         login_page.navigate(base_url)
#
#     with allure.step("Auth"):
#         login_page.auth(LOGIN, PASSWORD)
#
#     with allure.step("Quit from profile"):
#         login_page.quit_from_profile()
#
#     with allure.step("Check that quit was successful"):
#         login_page.assert_quited()
#
#     with allure.step("Delete user"):
#         delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.e2e
@pytest.mark.login
@allure.title("test_login_operator_positive")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_operator_positive(base_url, page: Page) -> None:
    login_page = LoginPage(page)

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Create operator"):
        USER_ID_OPERATOR, TOKEN_OPERATOR, LOGIN_OPERATOR = create_operator(API_URL, USER_ID_USER, PASSWORD)

    with allure.step("Go to url"):
        login_page.navigate(base_url)

    with allure.step("Auth"):
        login_page.auth(LOGIN_OPERATOR, PASSWORD)

    with allure.step("Quit from profile"):
        login_page.quit_from_profile()

    with allure.step("Check that quit was successful"):
        login_page.assert_quited()

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)

    with allure.step("Delete operator"):
        delete_user(API_URL, TOKEN_OPERATOR, USER_ID_OPERATOR)


@pytest.mark.e2e
@pytest.mark.login
@allure.title("test_login_user_negotive")
@allure.severity(allure.severity_level.NORMAL)
def test_login_user_negotive(base_url, page: Page) -> None:
    login_page = LoginPage(page)

    with allure.step("Go to url"):
        login_page.navigate(base_url)

    with allure.step("Auth"):
        login_page.auth(LOGIN_NEGOTIVE, PASSWORD)

    with allure.step("Check that alert message visible"):
        login_page.assert_alert_visible("Wrong login or password")


@pytest.mark.e2e
@pytest.mark.login
@allure.title("test_password_user_negotive")
@allure.severity(allure.severity_level.NORMAL)
def test_password_user_negotive(base_url, page: Page) -> None:
    login_page = LoginPage(page)

    with allure.step("Go to url"):
        login_page.navigate(base_url)

    with allure.step("Auth"):
        login_page.auth(USER, PASSWORD_NEGOTIVE)

    with allure.step("Check that alert message visible"):
        login_page.assert_alert_visible("Wrong login or password")