from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.users import *
from utils.create_delete_user import create_user, delete_user
import pytest
import allure


@pytest.mark.independent
@pytest.mark.users
@allure.title("test_add_delete_admin_by_admin")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_delete_admin_by_admin(page: Page) -> None:

    with allure.step("Create admin 1"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)

    with allure.step("Auth"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to users"):
        go_to_users(page)

    with allure.step("Press button (Add User)"):
        press_button_add_user(page)

    with allure.step("Set admin 2 info"):
        set_user(NEW_NAME,
                 NEW_LOGIN,
                 PASSWORD,
                 EMAIL1,
                 "someComment",
                 "Администратор",
                 page)

    with allure.step("Press button (Add) in modal window"):
        press_button_add_in_modal(page)

    with allure.step("Check"):
        expect(page.locator(INPUT_NAME)).to_have_value(NEW_NAME, timeout=wait_until_visible)
        expect(page.locator(INPUT_LOGIN)).to_have_value(NEW_LOGIN, timeout=wait_until_visible)
        expect(page.locator(INPUT_EMAIL)).to_have_value(EMAIL1, timeout=wait_until_visible)
        expect(page.locator(INPUT_COMMENT)).to_have_text("someComment", timeout=wait_until_visible)
        expect(page.locator(SELECT_ROLE)).to_have_text("Администратор", timeout=wait_until_visible)
        expect(page.locator(INPUT_PHONE)).to_be_visible(timeout=wait_until_visible)
        expect(page.locator(INPUT_NEW_PASSWORD)).to_be_visible(timeout=wait_until_visible)
        expect(page.locator(INPUT_NEW_PASSWORD_REPEAT)).to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete admin 2"):
        delete_added_user(page)

    with allure.step("Check that admin 2 deleted"):
        expect(page.locator(INPUT_LOGIN)).to_have_value(LOGIN, timeout=wait_until_visible)

    with allure.step("Delete admin 1"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.users
@allure.title("test_add_delete_manager_by_admin")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_delete_manager_by_admin(page: Page) -> None:

    with allure.step("Create admin"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)

    with allure.step("Auth"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to users"):
        go_to_users(page)

    with allure.step("Press button (Add User)"):
        press_button_add_user(page)

    with allure.step("Set manager info"):
        set_user(NEW_NAME,
                 NEW_LOGIN,
                 PASSWORD,
                 EMAIL2,
                 "someComment",
                 "Интегратор",
                  page)

    with allure.step("Press button (Add) in modal window"):
        press_button_add_in_modal(page)

    with allure.step("Check"):
        expect(page.locator(INPUT_LOGIN)).to_have_value(NEW_LOGIN, timeout=wait_until_visible)
        expect(page.locator(INPUT_NAME)).to_have_value(NEW_NAME, timeout=wait_until_visible)
        expect(page.locator(INPUT_EMAIL)).to_have_value(EMAIL2, timeout=wait_until_visible)
        expect(page.locator(INPUT_COMMENT)).to_have_text("someComment", timeout=wait_until_visible)
        expect(page.locator(SELECT_ROLE)).to_have_text("Интегратор", timeout=wait_until_visible)
        expect(page.locator(INPUT_PHONE)).to_be_visible(timeout=wait_until_visible)
        expect(page.locator(INPUT_NEW_PASSWORD)).to_be_visible(timeout=wait_until_visible)
        expect(page.locator(INPUT_NEW_PASSWORD_REPEAT)).to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete added manager"):
        delete_added_user(page)

    with allure.step("Check that manager deleted"):
        expect(page.locator(INPUT_LOGIN)).to_have_value(LOGIN, timeout=wait_until_visible)

    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.users
@allure.title("test_add_delete_user_by_admin")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_delete_user_by_admin(page: Page) -> None:

    with allure.step("Create admin"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)

    with allure.step("Auth"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to users"):
        go_to_users(page)

    with allure.step("Press button (Add User)"):
        press_button_add_user(page)

    with allure.step("Set user info"):
        set_user(NEW_NAME,
                 NEW_LOGIN,
                 PASSWORD,
                 EMAIL3,
                 "someComment",
                 "Компания",
                 page)

    with allure.step("Set industry and partner for user"):
        set_industry_and_partner("Недвижимость",
                                 "managerIM",
                                 page)
    with allure.step("Set STT for user"):
        set_stt("Русский",
                "Deepgram",
                "whisper",
                page)
    with allure.step("Press button (Add) in modal window"):
        press_button_add_in_modal(page)

    with allure.step("Check"):
        expect(page.locator(INPUT_LOGIN)).to_have_value(NEW_LOGIN, timeout=wait_until_visible)
        expect(page.locator(INPUT_NAME)).to_have_value(NEW_NAME, timeout=wait_until_visible)
        expect(page.locator(INPUT_EMAIL)).to_have_value(EMAIL3, timeout=wait_until_visible)
        #page.wait_for_timeout(2300)
        expect(page.locator(INPUT_COMMENT)).to_have_text("someComment", timeout=wait_until_visible)
        expect(page.locator(SELECT_ROLE)).to_have_text("Компания", timeout=wait_until_visible)
        expect(page.locator(SELECT_INDUSTRY)).to_have_text("Недвижимость", timeout=wait_until_visible)
        expect(page.locator(SELECT_PARTNER)).to_have_text("managerIM", timeout=wait_until_visible)
        expect(page.locator(INPUT_PHONE)).to_be_visible(timeout=wait_until_visible)
        expect(page.locator(INPUT_NEW_PASSWORD)).to_be_visible(timeout=wait_until_visible)
        expect(page.locator(INPUT_NEW_PASSWORD_REPEAT)).to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete added user"):
        delete_added_user(page)

    with allure.step("Check that user deleted"):
        expect(page.locator(INPUT_LOGIN)).to_have_value(LOGIN, timeout=wait_until_visible)

    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.users
@allure.title("test_add_user_cancel_by_admin")
@allure.severity(allure.severity_level.NORMAL)
def test_example(page: Page) -> None:

    with allure.step("Create admin"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)

    with allure.step("Auth"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to users"):
        go_to_users(page)

    with allure.step("Press button (Add User)"):
        press_button_add_user(page)

    with allure.step("Cancel by button CANCEL"):
        page.locator(BUTTON_OTMENA).click()

    with allure.step("Check"):
        expect(page.locator(INPUT_PASSWORD)).not_to_be_visible()

    with allure.step("Press button (Add User)"):
        press_button_add_user(page)

    with allure.step("Cancel by button KRESTIK"):
        page.locator(BUTTON_KRESTIK).click()

    with allure.step("Check"):
        expect(page.locator(INPUT_PASSWORD)).not_to_be_visible()

    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.users
@allure.title("test_add_delete_user_by_manager")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Precondition : manager should have access_rights for create and delete user")
def test_add_delete_user_by_manager(page: Page) -> None:

    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)

    with allure.step("Auth"):
        auth(MANAGER, PASSWORD, page)

    with allure.step("Go to users"):
        go_to_users(page)

    with allure.step("Press button (Add User)"):
        press_button_add_user(page)

    with allure.step("Set user info"):
        set_user(NEW_NAME,
                 NEW_LOGIN,
                 PASSWORD,
                 EMAIL2,
                 "someComment",
                 "Компания",
                 page)

    with allure.step("Check that select partner not available"):
        expect(page.locator(SELECT_PARTNER)).not_to_be_visible(timeout=wait_until_visible)

    with allure.step("Set industry"):
        set_industry("Недвижимость", page)

    with allure.step("Set STT"):
        set_stt("Русский",
                "IMOT.IO",
                "Стандарт",
                 page)

    with allure.step("Press button (Add) in modal window"):
        press_button_add_in_modal(page)

    with allure.step("Check"):
        expect(page.locator(INPUT_LOGIN)).to_have_value(NEW_LOGIN, timeout=wait_until_visible)
        expect(page.locator(INPUT_NAME)).to_have_value(NEW_NAME, timeout=wait_until_visible)
        expect(page.locator(INPUT_EMAIL)).to_have_value(EMAIL2, timeout=wait_until_visible)
        page.wait_for_timeout(3500)
        expect(page.get_by_text("Компания")).to_have_count(1, timeout=wait_until_visible)
        expect(page.get_by_text("Недвижимость")).to_have_count(3, timeout=wait_until_visible)
        expect(page.locator(INPUT_PHONE)).to_be_visible(timeout=wait_until_visible)
        expect(page.locator(INPUT_NEW_PASSWORD)).to_be_visible(timeout=wait_until_visible)
        expect(page.locator(INPUT_NEW_PASSWORD_REPEAT)).to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete added user"):
        delete_added_user(page)

    with allure.step("Check that user deleted"):
        expect(page.locator(INPUT_LOGIN)).to_have_value("3managerIM", timeout=wait_until_visible)


@pytest.mark.independent
@pytest.mark.users
@allure.title("test_add_delete_operator_by_user")
@allure.severity(allure.severity_level.NORMAL)
def test_add_delete_operator_by_user(page: Page) -> None:

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)

    with allure.step("Auth"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to settings"):
        page.locator(BUTTON_NASTROIKI).click()

    with allure.step("Go to employees"):
        page.locator(BUTTON_SOTRUDNIKI).click()

    with allure.step("Press button (Add employee)"):
        press_button_add_employee(page)

    with allure.step("Set operator info"):
        set_operator(NEW_OPERATOR_NAME,
                     NEW_OPERATOR_LOGIN,
                     PASSWORD,
                     EMAIL1,
                     EMAIL2,
                     EMAIL3,
                     page)
    with allure.step("Press button (Add) in modal window"):
        press_button_add_in_modal(page)

    with allure.step("Check"):
        expect(page.locator(INPUT_NAME)).to_have_value(NEW_OPERATOR_NAME, timeout=wait_until_visible)
        expect(page.locator(INPUT_LOGIN)).to_have_value(NEW_OPERATOR_LOGIN, timeout=wait_until_visible)
        #expect(page.locator(INPUT_PHONE)).to_have_value(EMAIL1, timeout=wait_until_visible)  open after https://task.imot.io/browse/DEV-1982
        expect(page.locator(INPUT_EMAIL)).to_have_value(EMAIL2, timeout=wait_until_visible)
        expect(page.locator(INPUT_COMMENT)).to_have_text(EMAIL3, timeout=wait_until_visible)
        expect(page.locator(INPUT_PHONE)).to_be_visible(timeout=wait_until_visible)
        expect(page.locator(INPUT_NEW_PASSWORD)).to_be_visible(timeout=wait_until_visible)
        expect(page.locator(INPUT_NEW_PASSWORD_REPEAT)).to_be_visible(timeout=wait_until_visible)
    with allure.step("Delete added employee"):
        delete_added_user(page)

    with allure.step("Check that employee deleted"):
        expect(page.locator(BUTTON_DOBAVIT_SOTRUDNIKA)).to_be_visible(timeout=wait_until_visible)
        expect(page.locator(USER_LOGIN_IN_LEFT_MENU)).to_have_text(LOGIN, timeout=wait_until_visible)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.users
@allure.title("test_check_search")
@allure.severity(allure.severity_level.NORMAL)
def test_check_search(page: Page) -> None:

    with allure.step("Create admin"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)

    with allure.step("Auth"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to users"):
        go_to_users(page)

    with allure.step("Fill searchString"):
        page.locator(INPUT_POISK).fill("ecot")

    with allure.step("Check ecotelecom visible and 1userIM not visible"):
        expect(page.get_by_text("ecotelecom")).to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("1userIM")).not_to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN, USER_ID)