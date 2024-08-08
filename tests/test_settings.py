from playwright.sync_api import Page, expect, Route
from utils.variables import *
from utils.auth import auth
from pages.settings import *
from utils.create_delete_user import create_user, delete_user, give_user_to_manager, create_operator
import pytest
import allure
import random


@pytest.mark.independent
@pytest.mark.settings
@allure.title("test_address_book_fill_by_user")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("input text to address-book, save, check that text saved")
def test_address_book_fill_by_user(base_url, page: Page) -> None:
    
    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)
    
    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)
    
    with allure.step("Auth as user"):
        auth(LOGIN, PASSWORD, page)
    
    with allure.step("Go to settings"):
        click_settings(page)
    
    with allure.step("Go to address book"):
        click_address_book(page)
    
    with allure.step("Fill address book"):
        fill_address_book("Телефон;Должность;ФИО\n12345;IVAN;BOSS", page)
    
    with allure.step("Press (Save) button"):
        press_save(page)
    
    with allure.step("Go to personal info"):
        click_personal_info(page)
    
    with allure.step("Go to address book"):
        click_address_book(page)
    
    with allure.step("Check that address book contain correct text"):
        expect(page.locator(INPUT_ADDRESS_BOOK)).to_contain_text(["Телефон;Должность;ФИО\n12345;IVAN;BOSS"])
    
    with allure.step("Page reload"):
        page.reload()
        page.wait_for_selector(INPUT_ADDRESS_BOOK)

    with allure.step("Check that address book contain correct text after page reload"):
        expect(page.locator(INPUT_ADDRESS_BOOK)).to_contain_text(["Телефон;Должность;ФИО\n12345;IVAN;BOSS"])

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.settings
@allure.title("test_admin_can_change_login_for_manager")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("check admin can change login for manager")
def test_admin_can_change_login_for_manager(base_url, page: Page) -> None:

    CHANGED_LOGIN = f"auto_test_user_ch_{datetime.now().strftime('%m%d%H%M')}{datetime.now().microsecond}"
    
    with allure.step("Create admin"):
        USER_ID_ADMIN, TOKEN_ADMIN, LOGIN_ADMIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)
    
    with allure.step("Create manager"):
        USER_ID_MANAGER, TOKEN_MANAGER, LOGIN_MANAGER = create_user(API_URL, ROLE_MANAGER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)
    
    with allure.step("Auth as admin"):
        auth(LOGIN_ADMIN, PASSWORD, page)
    
    with allure.step("Go to manager"):
        go_to_admin_or_manager(LOGIN_MANAGER, page)
    
    with allure.step("Go to settings"):
        click_settings(page)
    
    with allure.step("Check that manager have original login"):
        expect(page.locator(INPUT_LOGIN)).to_have_value(LOGIN_MANAGER)
    
    with allure.step("Change login"):
        change_login(CHANGED_LOGIN, page)
    
    with allure.step("Press (save) button"):
        press_save(page)
    
    with allure.step("Reload page"):
        page.reload()
        page.wait_for_selector(INPUT_LOGIN)
        page.wait_for_timeout(350)
    
    with allure.step("Check that login changed"):
        expect(page.locator(INPUT_LOGIN)).to_have_value(CHANGED_LOGIN)
    
    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN_ADMIN, USER_ID_ADMIN)
    
    with allure.step("Delete manager"):    
        delete_user(API_URL, TOKEN_MANAGER, USER_ID_MANAGER)


@pytest.mark.independent
@pytest.mark.settings
@allure.title("test_admin_can_change_login_for_user_and_operator")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("check admin can change login for user and operator")
def test_admin_can_change_login_for_user_and_operator(base_url, page: Page) -> None:

    NEW_OPERATOR_NAME = NEW_OPERATOR_LOGIN = f"auto_test_operator_{datetime.now().strftime('%m%d%H%M')}_{datetime.now().microsecond}"
    CHANGED_LOGIN = f"auto_test_user_ch_{datetime.now().strftime('%m%d%H%M')}{datetime.now().microsecond}"

    with allure.step("Create admin"):
        USER_ID_ADMIN, TOKEN_ADMIN, LOGIN_ADMIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)
    
    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)
    
    with allure.step("Create operator"):
        USER_ID_OPERATOR, TOKEN_OPERATOR, LOGIN_OPERATOR = create_operator(API_URL, USER_ID_USER, PASSWORD)
    
    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)
    
    with allure.step("Auth with admin"):
        auth(LOGIN_ADMIN, PASSWORD, page)
    
    # change login for user

    with allure.step("Go to user"):
        go_to_user(LOGIN_USER, page)
    
    with allure.step("Go to settings"):
        click_settings(page)
    
    with allure.step("Change login for user"):
        change_login(CHANGED_LOGIN, page)
    
    with allure.step("Press (save) button"):
        press_save(page)
    
    with allure.step("Reload page"):
        page.reload()
        page.wait_for_selector(INPUT_LOGIN)
        page.wait_for_timeout(500)
    
    with allure.step("Check that login changed"):
        expect(page.locator(INPUT_LOGIN)).to_have_value(CHANGED_LOGIN)

    # change for operator
    
    with allure.step("Go to employees from left menu"):
        page.locator(BUTTON_EMPLOYEES).click()
        page.wait_for_selector(BUTTON_DOBAVIT_SOTRUDNIKA)
    
    with allure.step("Go to operator from table"):
        go_to_operator_from_table(page)
    
    with allure.step("Change login for operator"):
        change_login(NEW_OPERATOR_LOGIN, page)
    
    with allure.step("Press (save) button"):
        press_save(page)
    
    with allure.step("Page reload"):
        page.reload()
        page.wait_for_selector(INPUT_LOGIN)
        page.wait_for_timeout(500)
    
    with allure.step("Check that login changed"):
        expect(page.locator(INPUT_LOGIN)).to_have_value(NEW_OPERATOR_LOGIN)
    
    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN_ADMIN, USER_ID_ADMIN)
    
    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)
    
    with allure.step("Delete operator"):
        delete_user(API_URL, TOKEN_OPERATOR, USER_ID_OPERATOR)


@pytest.mark.independent
@pytest.mark.settings
@allure.title("test_user_cant_change_login_for_operator")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("check that changing login disabled for operator")
def test_user_cant_change_login_for_operator(base_url, page: Page) -> None:

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Crete operator"):
        USER_ID_OPERATOR, TOKEN_OPERATOR, LOGIN_OPERATOR = create_operator(API_URL, USER_ID_USER, PASSWORD)

    with allure.step("Go to page"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with user"):
        auth(LOGIN_USER, PASSWORD, page)

    with allure.step("Go to settings"):
        click_settings(page)

    # check disabled for operator
    with allure.step("Go to employees"):
        click_employees(page)

    with allure.step("Go to operator from table"):
        go_to_operator_from_table(page)

    with allure.step("Check that login field in operators personal info disabled"):
        expect(page.locator(INPUT_LOGIN)).to_be_disabled()

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)

    with allure.step("Delete operator"):
        delete_user(API_URL, TOKEN_OPERATOR, USER_ID_OPERATOR)


@pytest.mark.independent
@pytest.mark.settings
@allure.title("test_manager_cant_change_login_for_user_and_operator")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_manager_cant_change_login_for_user_and_operator")
def test_manager_cant_change_login_for_user_and_operator(base_url, page: Page) -> None:

    with allure.step("Create manager"):
        USER_ID_MANAGER, TOKEN_MANAGER, LOGIN_MANAGER = create_user(API_URL, ROLE_MANAGER, PASSWORD)

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)
        give_user_to_manager(API_URL, USER_ID_MANAGER, USER_ID_USER, TOKEN_MANAGER)

    with allure.step("Create operator"):
        USER_ID_OPERATOR, TOKEN_OPERATOR, LOGIN_OPERATOR = create_operator(API_URL, USER_ID_USER, PASSWORD)

    with allure.step("Go to page"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with manager"):
        auth(LOGIN_MANAGER, PASSWORD, page)

    with allure.step("Go to user"):
        # check disabled for user
        go_to_user(LOGIN_USER, page)

    with allure.step("Go to settings"):
        click_settings(page)

    with allure.step("Check that login field disabled"):
        expect(page.locator(INPUT_LOGIN)).to_be_disabled()

    with allure.step("Go to employees"):
        # check disabled for operator
        click_employees(page)

    with allure.step("Go to operator from table"):
        go_to_operator_from_table(page)

    with allure.step("Check that login field disabled"):
        expect(page.locator(INPUT_LOGIN)).to_be_disabled()

    with allure.step("Delete manager"):
        delete_user(API_URL, TOKEN_MANAGER, USER_ID_MANAGER)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)

    with allure.step("Delete operator"):
        delete_user(API_URL, TOKEN_OPERATOR, USER_ID_OPERATOR)


@pytest.mark.independent
@pytest.mark.settings
@allure.title("test_admin_can_change_rights_for_manager")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("check admin can change rights for manager")
def test_admin_can_change_rights_for_manager(base_url, page: Page) -> None:
    
    with allure.step("Create admin"):
        USER_ID_ADMIN, TOKEN_ADMIN, LOGIN_ADMIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)
    
    with allure.step("Create manager"):
        USER_ID_MANAGER, TOKEN_MANAGER, LOGIN_MANAGER = create_user(API_URL, ROLE_MANAGER, PASSWORD)
    
    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth as admin"):
        auth(LOGIN_ADMIN, PASSWORD, page)
    
    with allure.step("Go to manager"):
        go_to_admin_or_manager(LOGIN_MANAGER, page)
    
    with allure.step("Go to settings"):
        click_settings(page)
    
    with allure.step("Go to rights"):
        click_rights(page)
    
    with allure.step("Check that manager have 6 right"):
        expect(page.locator(BLOCK_ONE_RIGHT)).to_have_count(6)
    
    with allure.step("Click to all rights and check all checkboxes"):
        click_all_checkboxes_on_page(page)
    
    with allure.step("Press (save) in rights"):
        press_save_in_rights(page)
    
    with allure.step("Page reload"):
        page.reload()
        page.wait_for_selector(BUTTON_SAVE_IN_RIGHTS)
    
    with allure.step("Check that all rights checked after page reload"):
        all_checkboxes_to_be_checked(page)

        assert all_checkboxes_to_be_checked(page) == True
    
    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN_ADMIN, USER_ID_ADMIN)
    
    with allure.step("Delete manager"):
        delete_user(API_URL, TOKEN_MANAGER, USER_ID_MANAGER)


@pytest.mark.independent
@pytest.mark.settings
@allure.title("test_admin_can_change_rights_for_user_and_operator")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("check admin can change rights for user and operator")
def test_admin_can_change_rights_for_user_and_operator(base_url, page: Page) -> None:

    with allure.step("Create admin"):
        USER_ID_ADMIN, TOKEN_ADMIN, LOGIN_ADMIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)
    
    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)
    
    with allure.step("Create operator"):
        USER_ID_OPERATOR, TOKEN_OPERATOR, LOGIN_OPERATOR = create_operator(API_URL, USER_ID_USER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth as admin"):
        auth(LOGIN_ADMIN, PASSWORD, page)

    # change rights for user

    with allure.step("Go to user"):
        go_to_user(LOGIN_USER, page)
    
    with allure.step("Go to settings"):
        click_settings(page)

    with allure.step("Go to rights"):
        click_rights(page)
    
    with allure.step("Check that user have 3 right"):
        expect(page.locator(BLOCK_ONE_RIGHT)).to_have_count(3)
    
    with allure.step("Click to all rights and check all checkboxes"):
        click_all_checkboxes_on_page(page)
    
    with allure.step("Press (save) in rights"):
        press_save_in_rights(page)
    
    with allure.step("Page reload"):
        page.reload()
        page.wait_for_selector(BUTTON_SAVE_IN_RIGHTS)
    
    with allure.step("Check that all rights checked after page reload"):
        all_checkboxes_to_be_checked(page)

        assert all_checkboxes_to_be_checked(page) == True

    # change rights for operator
    
    with allure.step("Go to employees"):
        click_employees(page)
    
    with allure.step("Go to operator from table"):
        go_to_operator_from_table(page)
    
    with allure.step("Go to rights"):
        click_rights(page)
    
    with allure.step("Check that operator have 24 rights"):
        expect(page.locator(BLOCK_ONE_RIGHT)).to_have_count(24)
    
    with allure.step("Click to all rights and check all checkboxes"):
        click_all_checkboxes_on_page(page)
    
    with allure.step("Press (save) in rights"):
        press_save_in_rights(page)
    
    with allure.step("Page reload"):
        page.reload()
        page.wait_for_selector(BUTTON_SAVE_IN_RIGHTS)
    
    with allure.step("Check that all rights checked after page reload"):
        all_checkboxes_to_be_checked(page)

        assert all_checkboxes_to_be_checked(page) == True
    
    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN_ADMIN, USER_ID_ADMIN)
    
    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)
    
    with allure.step("Delete operator"):
        delete_user(API_URL, TOKEN_OPERATOR, USER_ID_OPERATOR)


@pytest.mark.independent
@pytest.mark.settings
@allure.title("test_user_can_change_rights_for_operator")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check user can change rights for operator")
def test_user_can_change_rights_for_operator(base_url, page: Page) -> None:

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Create operator"):
        USER_ID_OPERATOR, TOKEN_OPERATOR, LOGIN_OPERATOR = create_operator(API_URL, USER_ID_USER, PASSWORD)

    with allure.step("Go to page"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with user"):
        auth(LOGIN_USER, PASSWORD, page)

    # change rights for operator
    with allure.step("Go to settings"):
        click_settings(page)

    with allure.step("Go to employees"):
        click_employees(page)

    with allure.step("Go to operator from table"):
        go_to_operator_from_table(page)

    with allure.step("Go to rights"):
        click_rights(page)

    with allure.step("Check that operator have 24 rights in list"):
        expect(page.locator(BLOCK_ONE_RIGHT)).to_have_count(24)

    with allure.step("Click to all rights and check all checkboxes"):
        click_all_checkboxes_on_page(page)

    with allure.step("Press (Save) button"):
        press_save_in_rights(page)

    with allure.step("Page reload"):
        page.reload()
        page.wait_for_selector(BUTTON_SAVE_IN_RIGHTS)

    with allure.step("Check that all rights checked after page reload"):
        all_checkboxes_to_be_checked(page)

        assert all_checkboxes_to_be_checked(page) == True

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)

    with allure.step("Delete operator"):
        delete_user(API_URL, TOKEN_OPERATOR, USER_ID_OPERATOR)


@pytest.mark.independent
@pytest.mark.settings
@allure.title("test_change_personal_information_save_admin_itself")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check changing and saving personal info for admin")
def test_change_personal_information_save_admin_itself(base_url, page: Page) -> None:

    NEW_NAME = NEW_LOGIN = f"auto_test_user_{datetime.now().strftime('%m%d%H%M')}_{datetime.now().microsecond}"
    EMAIL = f"email_{datetime.now().microsecond}{random.randint(100, 200)}@mail.ru"

    with allure.step("Create admin"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    with allure.step("Go to page"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with admin"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to settings"):
        click_settings(page)

    with allure.step("Change login"):
        change_login(NEW_LOGIN, page)

    with allure.step("Press (Save) button"):
        press_save(page)

    with allure.step("Change person al information"):
        fill_personal_information_admin_and_manager(NEW_NAME, EMAIL, "1234567890", "someComment", "Africa/Bamako", page)

    with allure.step("Press (Save) button"):
        press_save(page)

    with allure.step("Click notifications"):
        click_notifications(page)

    with allure.step("Go to settings"):
        click_settings(page)

    with allure.step("Check that personal information changed"):
        expect(page.locator(INPUT_LOGIN)).to_have_value(NEW_LOGIN)
        expect(page.locator(INPUT_EMAIL)).to_have_value(EMAIL)
        expect(page.locator(INPUT_PHONE)).to_have_value("1234567890")
        expect(page.locator(INPUT_COMMENT)).to_have_value("someComment")
        expect(page.locator(SELECT_TIMEZONE).get_by_text("Africa/Bamako")).to_be_visible()
        expect(page.locator(SELECT_INDUSTRY)).not_to_be_visible()
        expect(page.locator(SELECT_PARTNER)).not_to_be_visible()

    with allure.step("Page reload"):
        page.reload()
        page.wait_for_selector(INPUT_EMAIL)
        page.wait_for_timeout(500)

    with allure.step("Check that personal information still have after reboot"):
        expect(page.locator(INPUT_LOGIN)).to_have_value(NEW_LOGIN)
        expect(page.locator(INPUT_EMAIL)).to_have_value(EMAIL)
        expect(page.locator(INPUT_PHONE)).to_have_value("1234567890")
        expect(page.locator(INPUT_COMMENT)).to_have_value("someComment")
        expect(page.locator(SELECT_TIMEZONE).get_by_text("Africa/Bamako")).to_be_visible()
        expect(page.locator(SELECT_INDUSTRY)).not_to_be_visible()
        expect(page.locator(SELECT_PARTNER)).not_to_be_visible()

    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.settings
@allure.title("test_change_personal_information_save_manager_itself")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check changing and saving personal info for manager")
def test_change_personal_information_save_manager_itself(base_url, page: Page) -> None:

    NEW_NAME = NEW_LOGIN = f"auto_test_user_{datetime.now().strftime('%m%d%H%M')}_{datetime.now().microsecond}"
    EMAIL = f"email_{datetime.now().microsecond}{random.randint(100, 999)}@mail.ru"

    with allure.step("Create manager"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_MANAGER, PASSWORD)

    with allure.step("Go to page"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with admin"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to settings"):
        click_settings(page)

    with allure.step("Change person al information"):
        fill_personal_information_admin_and_manager(NEW_NAME, EMAIL, "1234567890", "someComment", "Africa/Bamako", page)

    with allure.step("Press (Save) button"):
        press_save(page)

    with allure.step("Click notifications"):
        click_notifications(page)

    with allure.step("Go to settings"):
        click_settings(page)

    with allure.step("Check that personal information changed"):
        expect(page.locator(INPUT_LOGIN)).to_be_disabled()
        expect(page.locator(INPUT_NAME)).to_have_value(NEW_NAME)
        expect(page.locator(INPUT_EMAIL)).to_have_value(EMAIL)
        expect(page.locator(INPUT_PHONE)).to_have_value("1234567890")
        expect(page.locator(INPUT_COMMENT)).to_have_value("someComment")
        expect(page.locator(SELECT_TIMEZONE).get_by_text("Africa/Bamako")).to_be_visible()
        expect(page.locator(SELECT_INDUSTRY)).not_to_be_visible()
        expect(page.locator(SELECT_PARTNER)).not_to_be_visible()

    with allure.step("Page reload"):
        page.reload()
        page.wait_for_selector(INPUT_EMAIL)
        page.wait_for_timeout(500)

    with allure.step("Check that personal information still have after reboot"):
        expect(page.locator(INPUT_LOGIN)).to_be_disabled()
        expect(page.locator(INPUT_NAME)).to_have_value(NEW_NAME)
        expect(page.locator(INPUT_EMAIL)).to_have_value(EMAIL)
        expect(page.locator(INPUT_PHONE)).to_have_value("1234567890")
        expect(page.locator(INPUT_COMMENT)).to_have_value("someComment")
        expect(page.locator(SELECT_TIMEZONE).get_by_text("Africa/Bamako")).to_be_visible()
        expect(page.locator(SELECT_INDUSTRY)).not_to_be_visible()
        expect(page.locator(SELECT_PARTNER)).not_to_be_visible()

    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.settings
@allure.title("test_change_personal_information_save_user_itself")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check changing and saving personal info for user")
def test_change_personal_information_save_user_itself(base_url, page: Page) -> None:

    NEW_NAME = NEW_LOGIN = f"auto_test_user_{datetime.now().strftime('%m%d%H%M')}_{datetime.now().microsecond}"
    EMAIL = f"email_{datetime.now().microsecond}{random.randint(100, 999)}@mail.ru"

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to page"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with admin"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to settings"):
        click_settings(page)

    with allure.step("Change person al information"):
        fill_personal_information_user_and_operator(NEW_NAME, EMAIL, "1234567890", "Africa/Bamako", page)

    with allure.step("Press (Save) button"):
        press_save(page)

    with allure.step("Click notifications"):
        click_notifications(page)

    with allure.step("Go to settings"):
        click_settings(page)

    with allure.step("Check that personal information changed"):
        expect(page.locator(INPUT_LOGIN)).to_be_disabled()
        expect(page.locator(INPUT_EMAIL)).to_have_value(EMAIL)
        expect(page.locator(INPUT_PHONE)).to_have_value("1234567890")
        expect(page.locator(INPUT_COMMENT)).not_to_be_visible()
        expect(page.locator(SELECT_TIMEZONE).get_by_text("Africa/Bamako")).to_be_visible()
        expect(page.locator(SELECT_INDUSTRY)).not_to_be_visible()
        expect(page.locator(SELECT_PARTNER)).not_to_be_visible()

    with allure.step("Page reload"):
        page.reload()
        page.wait_for_selector(INPUT_EMAIL)
        page.wait_for_timeout(300)

    with allure.step("Check that personal information still have after reboot"):
        expect(page.locator(INPUT_LOGIN)).to_be_disabled()
        expect(page.locator(INPUT_EMAIL)).to_have_value(EMAIL)
        expect(page.locator(INPUT_PHONE)).to_have_value("1234567890")
        expect(page.locator(INPUT_COMMENT)).not_to_be_visible()
        expect(page.locator(SELECT_TIMEZONE).get_by_text("Africa/Bamako")).to_be_visible()
        expect(page.locator(SELECT_INDUSTRY)).not_to_be_visible()
        expect(page.locator(SELECT_PARTNER)).not_to_be_visible()

    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.settings
@allure.title("test_change_personal_information_save_operator_itself")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check changing and saving personal info for operator")
def test_change_personal_information_save_operator_itself(base_url, page: Page) -> None:

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Create operator"):
        USER_ID_OPERATOR, TOKEN_OPERATOR, LOGIN_OPERATOR = create_operator(API_URL, USER_ID_USER, PASSWORD)

    with allure.step("Go to page"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with operator"):
        auth(LOGIN_OPERATOR, PASSWORD, page)

    with allure.step("Go to settings"):
        click_settings(page)

    with allure.step("Check that operator cant change personal information"):
        expect(page.locator(INPUT_EMAIL)).to_be_disabled()
        expect(page.locator(INPUT_PHONE)).to_be_disabled()
        expect(page.locator(INPUT_COMMENT)).not_to_be_visible()
        expect(page.locator(INPUT_LOGIN)).to_be_disabled()
        expect(page.locator(INPUT_NAME)).to_be_disabled()
        expect(page.locator(INPUT_NEW_PASSWORD)).to_be_disabled()
        expect(page.locator(INPUT_NEW_PASSWORD_REPEAT)).to_be_disabled()
        expect(page.locator(SELECT_INDUSTRY)).not_to_be_visible()
        expect(page.locator(SELECT_PARTNER)).not_to_be_visible()

    with allure.step("Check that message (Can change only administrator) exists"):
        expect(page.locator('[class*="typography--variant-body2"]')).to_contain_text("Редактировать персональную информацию может только администратор")

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)

    with allure.step("Delete operator"):
        delete_user(API_URL, TOKEN_OPERATOR, USER_ID_OPERATOR)


@pytest.mark.independent
@pytest.mark.settings
@allure.title("test_change_personal_information_save_operator_by_admin")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check changing and saving personal info for operator by admin")
def test_change_personal_information_save_operator_by_admin(base_url, page: Page) -> None:

    NEW_OPERATOR_NAME = NEW_OPERATOR_LOGIN = f"auto_test_operator_{datetime.now().strftime('%m%d%H%M')}_{datetime.now().microsecond}"
    EMAIL = f"email_{datetime.now().microsecond}{random.randint(100, 999)}@mail.ru"

    with allure.step("Create admin"):
        USER_ID_ADMIN, TOKEN_ADMIN, LOGIN_ADMIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Create operator"):
        USER_ID_OPERATOR, TOKEN_OPERATOR, LOGIN_OPERATOR = create_operator(API_URL, USER_ID_USER, PASSWORD)

    with allure.step("Go to page"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with admin"):
        auth(LOGIN_ADMIN, PASSWORD, page)

    with allure.step("Go to user"):
        go_to_user(LOGIN_USER, page)

    with allure.step("Go to settings"):
        click_settings(page)

    with allure.step("Go to employees"):
        click_employees(page)

    with allure.step("Go to operator from table"):
        go_to_operator_from_table(page)

    with allure.step("Fill personal information"):
        fill_personal_information_admin_and_manager(NEW_OPERATOR_NAME, EMAIL, "1234567890", "someComment", "Africa/Bamako", page)

    with allure.step("Press (save)"):
        press_save(page)

    with allure.step("Go to rights"):
        click_rights(page)

    with allure.step("Go to personal info"):
        click_personal_info(page)

    with allure.step("Check that personal information saved"):
        expect(page.locator(BLOCK_PERSONAL_INFO)).not_to_contain_text("Редактировать ")
        expect(page.locator(INPUT_NAME)).to_have_value(NEW_OPERATOR_NAME)
        expect(page.locator(INPUT_EMAIL)).to_have_value(EMAIL)
        expect(page.locator(INPUT_PHONE)).to_have_value("1234567890")
        expect(page.locator(INPUT_COMMENT)).to_have_value("someComment")
        expect(page.locator(SELECT_TIMEZONE).get_by_text("Africa/Bamako")).to_be_visible()
        expect(page.locator(SELECT_INDUSTRY)).not_to_be_visible()
        expect(page.locator(SELECT_PARTNER)).not_to_be_visible()

    with allure.step("Page reload"):
        page.reload()
        page.wait_for_selector(INPUT_NAME)
        page.wait_for_timeout(300)

    with allure.step("Check that personal information saved"):
        expect(page.locator(BLOCK_PERSONAL_INFO)).not_to_contain_text("Редактировать ")
        expect(page.locator(INPUT_NAME)).to_have_value(NEW_OPERATOR_NAME)
        expect(page.locator(INPUT_EMAIL)).to_have_value(EMAIL)
        expect(page.locator(INPUT_PHONE)).to_have_value("1234567890")
        expect(page.locator(INPUT_COMMENT)).to_have_value("someComment")
        expect(page.locator(SELECT_TIMEZONE).get_by_text("Africa/Bamako")).to_be_visible()
        expect(page.locator(SELECT_INDUSTRY)).not_to_be_visible()
        expect(page.locator(SELECT_PARTNER)).not_to_be_visible()

    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN_ADMIN, USER_ID_ADMIN)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)

    with allure.step("Delete operator"):
        delete_user(API_URL, TOKEN_OPERATOR, USER_ID_OPERATOR)


@pytest.mark.independent
@pytest.mark.settings
@allure.title("test_change_personal_information_save_operator_by_user")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check changing and saving personal info for operator by user")
def test_change_personal_information_save_operator_by_user(base_url, page: Page) -> None:

    NEW_OPERATOR_NAME = NEW_OPERATOR_LOGIN = f"auto_test_operator_{datetime.now().strftime('%m%d%H%M')}_{datetime.now().microsecond}"
    EMAIL = f"email_{datetime.now().microsecond}{random.randint(100, 999)}@mail.ru"

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Create operator"):
        USER_ID_OPERATOR, TOKEN_OPERATOR, LOGIN_OPERATOR = create_operator(API_URL, USER_ID_USER, PASSWORD)

    with allure.step("Go to page"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with user"):
        auth(LOGIN_USER, PASSWORD, page)

    with allure.step("Go to settings"):
        click_settings(page)

    with allure.step("Go to employees"):
        click_employees(page)

    with allure.step("Go to operator from table"):
        go_to_operator_from_table(page)

    with allure.step("Fill personal information"):
        fill_personal_information_user_and_operator(NEW_OPERATOR_NAME, EMAIL, "1234567890", "Africa/Bamako", page)

    with allure.step("Press (save)"):
        press_save(page)

    with allure.step("Go to rights"):
        click_rights(page)

    with allure.step("Go to personal info"):
        click_personal_info(page)

    with allure.step("Check that personal information saved"):
        expect(page.locator(BLOCK_PERSONAL_INFO)).not_to_contain_text("Редактировать ")
        expect(page.locator(INPUT_NAME)).to_have_value(NEW_OPERATOR_NAME)
        expect(page.locator(INPUT_EMAIL)).to_have_value(EMAIL)
        expect(page.locator(INPUT_PHONE)).to_have_value("1234567890")
        expect(page.locator(INPUT_COMMENT)).not_to_be_visible()
        expect(page.locator(SELECT_TIMEZONE).get_by_text("Africa/Bamako")).to_be_visible()
        expect(page.locator(SELECT_INDUSTRY)).not_to_be_visible()
        expect(page.locator(SELECT_PARTNER)).not_to_be_visible()

    with allure.step("Page reload"):
        page.reload()
        page.wait_for_selector(INPUT_NAME)
        page.wait_for_timeout(300)

    with allure.step("Check that personal information saved"):
        expect(page.locator(BLOCK_PERSONAL_INFO)).not_to_contain_text("Редактировать ")
        expect(page.locator(INPUT_NAME)).to_have_value(NEW_OPERATOR_NAME)
        expect(page.locator(INPUT_EMAIL)).to_have_value(EMAIL)
        expect(page.locator(INPUT_PHONE)).to_have_value("1234567890")
        expect(page.locator(INPUT_COMMENT)).not_to_be_visible()
        expect(page.locator(SELECT_TIMEZONE).get_by_text("Africa/Bamako")).to_be_visible()
        expect(page.locator(SELECT_INDUSTRY)).not_to_be_visible()
        expect(page.locator(SELECT_PARTNER)).not_to_be_visible()

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)

    with allure.step("Delete operator"):
        delete_user(API_URL, TOKEN_OPERATOR, USER_ID_OPERATOR)


@pytest.mark.independent
@pytest.mark.settings
@allure.title("test_left_menu_items_for_admin_itself")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check how many items in left menu for role")
def test_left_menu_items_for_admin_itself(base_url, page: Page) -> None:

    with allure.step("Create admin"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    with allure.step("Go to page"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with admin"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to settings"):
        click_settings(page)

    with allure.step("Check items in left menu"):
        expect(page.locator(BLOCK_LEFT_MENU)).to_contain_text(['Персональная информация'])
        expect(page.locator(LEFT_MENU_ITEM)).to_have_count(1)

    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.settings
@allure.title("test_left_menu_items_for_manager_itself")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check how many items in left menu for role")
def test_left_menu_items_for_manager_itself(base_url, page: Page) -> None:

    with allure.step("Create manager"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_MANAGER, PASSWORD)

    with allure.step("Go to page"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with manager"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to settings"):
        click_settings(page)

    with allure.step("Check items in left menu"):
        expect(page.locator(BLOCK_LEFT_MENU)).to_contain_text(['Персональная информация'])
        expect(page.locator(LEFT_MENU_ITEM)).to_have_count(1)

    with allure.step("Delete manager"):
        delete_user(API_URL, TOKEN, USER_ID)


# check how many items in left menu for role
@pytest.mark.independent
@pytest.mark.settings
@allure.title("test_left_menu_items_for_user_itself")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check how many items in left menu for role")
def test_left_menu_items_for_user_itself(base_url, page: Page) -> None:

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to page"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with user"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to settings"):
        click_settings(page)

    with allure.step("Check items in left menu"):
        expect(page.locator(BLOCK_LEFT_MENU)).to_contain_text(['Персональная информацияСотрудникиДействия с коммуникациямиКвоты777История потребления услугАдресная книгаИнтеграции'])
        expect(page.locator(LEFT_MENU_ITEM)).to_have_count(7)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


# check how many items in left menu for role
@pytest.mark.independent
@pytest.mark.settings
@allure.title("test_left_menu_items_for_operator_itself")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check how many items in left menu for role")
def test_left_menu_items_for_operator_itself(base_url, page: Page) -> None:

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Create operstor"):
        USER_ID_OPERATOR, TOKEN_OPERATOR, LOGIN_OPERATOR = create_operator(API_URL,USER_ID_USER,PASSWORD)

    with allure.step("Go to page"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with operator"):
        auth(LOGIN_OPERATOR, PASSWORD, page)

    with allure.step("Go to settings"):
        click_settings(page)

    with allure.step("Check items in left menu"):
        expect(page.locator(BLOCK_LEFT_MENU)).to_contain_text(['Персональная информация'])
        expect(page.locator(LEFT_MENU_ITEM)).to_have_count(1)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)

    with allure.step("Delete operator"):
        delete_user(API_URL, TOKEN_OPERATOR, USER_ID_OPERATOR)


@pytest.mark.independent
@pytest.mark.settings
@allure.title("test_admin_check_industry_and_partner_for_manager")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_admin_check_industry_and_partner_for_manager")
def test_admin_check_industry_and_partner_for_manager(base_url, page: Page) -> None:

    with allure.step("Create admin"):
        USER_ID_ADMIN, TOKEN_ADMIN, LOGIN_ADMIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    with allure.step("Create manager"):
        USER_ID_MANAGER, TOKEN_MANAGER, LOGIN_MANAGER = create_user(API_URL, ROLE_MANAGER, PASSWORD)

    with allure.step("Go to page"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with admin"):
        auth(LOGIN_ADMIN, PASSWORD, page)

    with allure.step("Go to manager"):
        go_to_admin_or_manager(LOGIN_MANAGER, page)

    with allure.step("Go to settings"):
        click_settings(page)

    with allure.step("Check that industry and partner not visible"):
        expect(page.locator(SELECT_INDUSTRY)).not_to_be_visible()
        expect(page.locator(SELECT_PARTNER)).not_to_be_visible()

    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN_ADMIN, USER_ID_ADMIN)

    with allure.step("Delete mamager"):
        delete_user(API_URL, TOKEN_MANAGER, USER_ID_MANAGER)


@pytest.mark.independent
@pytest.mark.settings
@allure.title("test_admin_check_industry_and_partner_for_user_and_operator")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_admin_check_industry_and_partner_for_user_and_operator")
def test_admin_check_industry_and_partner_for_user_and_operator(base_url, page: Page) -> None:

    with allure.step("Create admin"):
        USER_ID_ADMIN, TOKEN_ADMIN, LOGIN_ADMIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Create operator"):
        USER_ID_OPERATOR, TOKEN_OPERATOR, LOGIN_OPERATOR = create_operator(API_URL, USER_ID_USER, PASSWORD)

    with allure.step("Go to page"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with admin"):
        auth(LOGIN_ADMIN, PASSWORD, page)

    with allure.step("Go to user"):
        # check and change for user
        go_to_user(LOGIN_USER, page)

    with allure.step("Go to settings"):
        click_settings(page)

    with allure.step("Check that industry and partner visible"):
        expect(page.locator(SELECT_INDUSTRY)).to_be_visible()
        expect(page.locator(SELECT_PARTNER)).to_be_visible()

    with allure.step("Change industry"):
        change_industry('Ed-tech', page)

    with allure.step("Change partner"):
        change_partner('managerIM', page)

    with allure.step("Press (save)"):
        press_save(page)

    with allure.step("Page reload"):
        page.reload()
        page.wait_for_selector(INPUT_LOGIN)
        page.wait_for_timeout(300)

    with allure.step("Check that industry and partner changed"):
        expect(page.locator(SELECT_INDUSTRY)).to_have_text('Ed-tech')
        expect(page.locator(SELECT_PARTNER)).to_have_text('managerIM')

    with allure.step("Go to employees"):
        # check for operator
        click_employees(page)

    with allure.step("Go to operator from table"):
        go_to_operator_from_table(page)

    with allure.step("Check that industry and partner NOT visible"):
        expect(page.locator(SELECT_INDUSTRY)).not_to_be_visible()
        expect(page.locator(SELECT_PARTNER)).not_to_be_visible()

    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN_ADMIN, USER_ID_ADMIN)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)

    with allure.step("Delete operator"):
        delete_user(API_URL, TOKEN_OPERATOR, USER_ID_OPERATOR)


@pytest.mark.independent
@pytest.mark.settings
@allure.title("test_manager_check_industry_and_partner_for_user_and_operator")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_manager_check_industry_and_partner_for_user_and_operator")
def test_manager_check_industry_and_partner_for_user_and_operator(base_url, page: Page) -> None:

    with allure.step("Create manager"):
        USER_ID_MANAGER, TOKEN_MANAGER, LOGIN_MANAGER = create_user(API_URL, ROLE_MANAGER, PASSWORD)

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)
        give_user_to_manager(API_URL, USER_ID_MANAGER, USER_ID_USER, TOKEN_MANAGER)

    with allure.step("Create operator"):
        USER_ID_OPERATOR, TOKEN_OPERATOR, LOGIN_OPERATOR = create_operator(API_URL, USER_ID_USER, PASSWORD)

    with allure.step("Go to page"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with manager"):
        auth(LOGIN_MANAGER, PASSWORD, page)

    with allure.step("Go to user"):
        # check and change for user
        go_to_user(LOGIN_USER, page)

    with allure.step("Go to settings"):
        click_settings(page)

    with allure.step("Check that industry visible and partner NOT visible"):
        expect(page.locator(SELECT_INDUSTRY)).to_be_visible()
        expect(page.locator(SELECT_PARTNER)).not_to_be_visible()

    with allure.step("Change industry"):
        change_industry('Ed-tech', page)

    with allure.step("Press (save)"):
        press_save(page)

    with allure.step("Page reload"):
        page.reload()
        page.wait_for_selector(INPUT_LOGIN)
        page.wait_for_timeout(300)

    with allure.step("Check that industry changed and partner NOT visible"):
        expect(page.locator(SELECT_INDUSTRY)).to_have_text('Ed-tech')
        expect(page.locator(SELECT_PARTNER)).not_to_be_visible()

    with allure.step("Go to employees"):
        # check for operator
        click_employees(page)

    with allure.step("Go to operator from table"):
        go_to_operator_from_table(page)

    with allure.step("Check that industry and partner NOT visible"):
        expect(page.locator(SELECT_INDUSTRY)).not_to_be_visible()
        expect(page.locator(SELECT_PARTNER)).not_to_be_visible()

    with allure.step("Delete manager"):
        delete_user(API_URL, TOKEN_MANAGER, USER_ID_MANAGER)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)

    with allure.step("Delete operator"):
        delete_user(API_URL, TOKEN_OPERATOR, USER_ID_OPERATOR)


@pytest.mark.independent
@pytest.mark.settings
@allure.title("test_giving_communications_quota_by_admin")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("every auto_test_user gets 777 min quota by default. test check that we can add more")
def test_giving_communications_quota_by_admin(base_url, page: Page) -> None:

    with allure.step("Create admin"):
        USER_ID_ADMIN, TOKEN_ADMIN, LOGIN_ADMIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to page"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with admin"):
        auth(LOGIN_ADMIN, PASSWORD, page)

    with allure.step("Go to user"):
        go_to_user(LOGIN_USER, page)

    with allure.step("Go to settings"):
        click_settings(page)

    with allure.step("Go to quotas"):
        click_quota(page)

    with allure.step("Click (add quota)"):
        press_add_in_quotas(page)

    with allure.step("Check that system will recommend last gived quota (777)"):
        expect(page.locator(INPUT_QUOTA_TIME)).to_have_value("777")

    with allure.step("Click checkbox (bessro4no)"):
        page.locator('[role="dialog"]').locator('[type="checkbox"]').click()

    with allure.step("Check that checkbox was checked"):
        expect(page.locator('[role="dialog"]').locator('[type="checkbox"]')).to_be_checked()

    with allure.step("Check that dates disabled"):
        expect(page.locator('[class*="ant-picker-disabled"]')).to_be_visible()

    with allure.step("Fill quota 100"):
        fill_quota_time("100", page)

    with allure.step("press (add)"):
        press_add_in_quotas(page)
        page.wait_for_selector('[aria-rowindex="2"]', timeout=wait_until_visible)

    with allure.step("Reload page"):
        page.reload()
        page.wait_for_selector('[aria-rowindex="2"]', timeout=wait_until_visible)
        page.wait_for_timeout(2000)

    with allure.step("Check that quota added"):
        expect(page.locator('[role="gridcell"]')).to_have_count(12)
        expect(page.locator('[aria-rowindex="2"]').locator('[aria-colindex="4"]')).to_have_text("Бессрочно")

    with allure.step("Delete added quota"):
        page.locator('[fill="#FF4D4F"]').click()
        page.wait_for_timeout(3500)

    with allure.step("Check that quota deleted"):
        expect(page.locator('[fill="#FF4D4F"]')).not_to_be_visible(timeout=wait_until_visible)
        #expect(page.locator('[class="rs-table-body-info"]')).to_have_text("Информация отсутствует")

    with allure.step("Click (add quota)"):
        press_add_in_quotas(page)

    with allure.step("Check that system will recommend last gived quota (100)"):
        expect(page.locator(INPUT_QUOTA_TIME)).to_have_value("100")

    with allure.step("Choose period for quota"):
        choose_preiod_date("30/12/2024", "31/12/2024", page)

    with allure.step("Fill quota 100"):
        fill_quota_time("100", page)

    with allure.step("press (add)"):
        press_add_in_quotas(page)
        page.wait_for_selector('[aria-rowindex="2"]', timeout=wait_until_visible)

    with allure.step("Reload page"):
        page.reload()
        page.wait_for_selector('[aria-rowindex="2"]', timeout=wait_until_visible)
        page.wait_for_timeout(1500)

    with allure.step("Check that quota added"):
        expect(page.locator('[role="gridcell"]')).to_have_count(18)
        expect(page.locator('[aria-rowindex="2"]').locator('[aria-colindex="4"]')).to_have_text("2024-12-30 - 2024-12-31")

    with allure.step("Delete added quota"):
        page.locator('[fill="#FF4D4F"]').click()
        page.wait_for_timeout(500)

    with allure.step("Check that quota deleted"):
        expect(page.locator('[fill="#FF4D4F"]')).not_to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN_ADMIN, USER_ID_ADMIN)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)


@pytest.mark.independent
@pytest.mark.settings
@allure.title("test_giving_gpt_quota_by_admin")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("every auto_test_user gets 777 min quota by default. test check that we can add more")
def test_giving_gpt_quota_by_admin(base_url, page: Page) -> None:

    with allure.step("Create admin"):
        USER_ID_ADMIN, TOKEN_ADMIN, LOGIN_ADMIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to page"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with admin"):
        auth(LOGIN_ADMIN, PASSWORD, page)

    with allure.step("Go to user"):
        go_to_user(LOGIN_USER, page)

    with allure.step("Go to settings"):
        click_settings(page)

    with allure.step("Go to quotas"):
        click_quota(page)

    with allure.step("Click to (GPT) tab"):
        page.locator(BUTTON_GPT_QUOTAS).click()
        page.wait_for_selector(BLOCK_GPT_QUOTAS)

        # gpt

    with allure.step("Check negative value"):
        page.locator(BLOCK_CHAT_GPT).locator(INPUT_NEW_QUOTA).fill("-1")

    with allure.step("Check that (save) button disabled"):
        expect(page.locator(BLOCK_WITH_SAVE_BUTTON).locator(BUTTON_SAVE)).to_be_disabled()
        page.wait_for_timeout(500)

    with allure.step("Check value more than limit"):
        page.locator(BLOCK_CHAT_GPT).locator(INPUT_NEW_QUOTA).clear()
        page.locator(BLOCK_CHAT_GPT).locator(INPUT_NEW_QUOTA).fill("151")

    with allure.step("Check that (save) button disabled"):
        expect(page.locator(BLOCK_WITH_SAVE_BUTTON).locator(BUTTON_SAVE)).to_be_disabled()
        page.wait_for_timeout(500)

    with allure.step("Check value more than limit"):
        page.locator(BLOCK_CHAT_GPT).locator(INPUT_NEW_QUOTA).clear()
        page.locator(BLOCK_CHAT_GPT).locator(INPUT_NEW_QUOTA).fill("150")

    with allure.step("Click (save)"):
        page.locator(BLOCK_WITH_SAVE_BUTTON).locator(BUTTON_SAVE).click()

    with allure.step("Reload page and check that saved and have residue"):
        page.reload()
        page.wait_for_selector(BLOCK_GPT_QUOTAS)
        expect(page.locator(BLOCK_CHAT_GPT).locator(BLOCK_WITH_AMOUNT).nth(0)).to_have_text("150")
        expect(page.locator(BLOCK_CHAT_GPT).locator(BLOCK_WITH_AMOUNT).nth(1)).to_have_text("150.0")

        # yandex

    with allure.step("Check negative value"):
        page.locator(BLOCK_YANDEX_GPT).locator(INPUT_NEW_QUOTA).fill("-1")

    with allure.step("Check that (save) button disabled"):
        expect(page.locator(BLOCK_WITH_SAVE_BUTTON).locator(BUTTON_SAVE)).to_be_disabled()
        page.wait_for_timeout(500)

    with allure.step("Check value more than limit"):
        page.locator(BLOCK_YANDEX_GPT).locator(INPUT_NEW_QUOTA).clear()
        page.locator(BLOCK_YANDEX_GPT).locator(INPUT_NEW_QUOTA).fill("15001")

    with allure.step("Check that (save) button disabled"):
        expect(page.locator(BLOCK_WITH_SAVE_BUTTON).locator(BUTTON_SAVE)).to_be_disabled()
        page.wait_for_timeout(500)

    with allure.step("Check value more than limit"):
        page.locator(BLOCK_YANDEX_GPT).locator(INPUT_NEW_QUOTA).clear()
        page.locator(BLOCK_YANDEX_GPT).locator(INPUT_NEW_QUOTA).fill("15000")

    with allure.step("Click (save)"):
        page.locator(BLOCK_WITH_SAVE_BUTTON).locator(BUTTON_SAVE).click()

    with allure.step("Reload page and check that saved and have residue"):
        page.reload()
        page.wait_for_selector(BLOCK_GPT_QUOTAS)
        expect(page.locator(BLOCK_YANDEX_GPT).locator(BLOCK_WITH_AMOUNT).nth(0)).to_have_text("15000")
        expect(page.locator(BLOCK_YANDEX_GPT).locator(BLOCK_WITH_AMOUNT).nth(1)).to_have_text("15000.0")

    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN_ADMIN, USER_ID_ADMIN)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)


@pytest.mark.independent
@pytest.mark.settings
@allure.title("test_user_cant_change_quotas")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("every auto_test_user gets 777 min quota by default. test check that we can add more")
def test_user_cant_change_quotas(base_url, page: Page) -> None:

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to page"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with user"):
        auth(LOGIN_USER, PASSWORD, page)

    with allure.step("Go to settings"):
        click_settings(page)

    with allure.step("Go to quotas"):
        click_quota(page)

    with allure.step("Check that button (Add) not visible for user"):
        expect(page.get_by_role("button", name="Добавить", exact=True)).not_to_be_visible()

    with allure.step("Click to (GPT) tab"):
        page.locator(BUTTON_GPT_QUOTAS).click()
        page.wait_for_selector(BLOCK_GPT_QUOTAS)

    with allure.step("Check that button (save) and input for new amount - disabled"):
        expect(page.locator(BLOCK_WITH_SAVE_BUTTON).locator(BUTTON_SAVE)).to_be_disabled()
        expect(page.locator(BLOCK_CHAT_GPT).locator(INPUT_NEW_QUOTA)).to_be_disabled()
        expect(page.locator(BLOCK_YANDEX_GPT).locator(INPUT_NEW_QUOTA)).to_be_disabled()

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)



@pytest.mark.independent
@pytest.mark.settings
@allure.title("test_user_consumption_history")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_user_consumption_history. mocked")
def test_user_consumption_history(base_url, page: Page) -> None:

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    # mocks
    def handle_calls(route: Route):
        json_calls = [
            {"callDate": "2024-07-30", "fromServices": ["service1"], "callCount": 111, "sumDuration": 395},
            {"callDate": "2024-07-29", "fromServices": ["service2"], "callCount": 222, "sumDuration": 678}
        ]
        # fulfill the route with the mock data
        route.fulfill(json=json_calls)
        # Intercept the route
    page.route("**/history/calls?**", handle_calls)

    def handle_gpt(route: Route):
        json = [
            {"gptDate": "2024-07-30", "engine": "yandex_gpt", "model": "yandexgpt-lite", "communicationType": "call",
             "gptRequestId": "66A8B7129D963878D93D73CD", "gptRequestTitle": "title1", "requestCount": "200",
             "communicationCount": "111", "totalAmmount": "7.468260013125836"},
            {"gptDate": "2024-07-29", "engine": "chat_gpt", "model": "gpt-3.5-turbo", "communicationType": "call",
             "gptRequestId": "66A8B7129D963878D93D73CF", "gptRequestTitle": "title2", "requestCount": "299",
             "communicationCount": "222", "totalAmmount": "7.418260013125836"}
        ]
        # fulfill the route with the mock data
        route.fulfill(json=json)
        # Intercept the route
    page.route("**/history/gpt?**", handle_gpt)

    def handle_chats(route: Route):
        json_calls = [
            {"chatDate": "2024-07-29", "fromServices": ["chat1"], "chatCount": 999},
            {"chatDate": "2024-07-30", "fromServices": ["chat2"], "chatCount": 9002}
        ]
        # fulfill the route with the mock data
        route.fulfill(json=json_calls)
        # Intercept the route
    page.route("**/history/chats?**", handle_chats)

    with allure.step("Go to page"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with user"):
        auth(LOGIN_USER, PASSWORD, page)

    with allure.step("Go to settings"):
        click_settings(page)

    with allure.step("Go to consumption history"):
        page.locator(BUTTON_CONSUMPTION_HISTORY).click()

    with allure.step("Check exist search, calendar, mocked data and total count"):
        expect(page.locator(SEARCH_IN_CONSUMPTION_AUDIO)).to_have_count(1)
        expect(page.locator('[placeholder="Поиск по источнику"]')).to_have_count(1)
        expect(page.locator(CALENDAR_IN_CONSUMPTION)).to_have_count(1)
        #  check first row
        expect(page.locator('[aria-rowindex="2"]').locator('[aria-colindex="1"]')).to_contain_text("30.07.2024")
        expect(page.locator('[aria-rowindex="2"]').locator('[aria-colindex="2"]')).to_contain_text("service1")
        expect(page.locator('[aria-rowindex="2"]').locator('[aria-colindex="3"]')).to_contain_text("111")
        expect(page.locator('[aria-rowindex="2"]').locator('[aria-colindex="4"]')).to_contain_text("395")
        expect(page.locator('[aria-rowindex="2"]').locator('[aria-colindex="5"]')).to_contain_text("6:35")
        #  check second row
        expect(page.locator('[aria-rowindex="3"]').locator('[aria-colindex="1"]')).to_contain_text("29.07.2024")
        expect(page.locator('[aria-rowindex="3"]').locator('[aria-colindex="2"]')).to_contain_text("service2")
        expect(page.locator('[aria-rowindex="3"]').locator('[aria-colindex="3"]')).to_contain_text("222")
        expect(page.locator('[aria-rowindex="3"]').locator('[aria-colindex="4"]')).to_contain_text("678")
        expect(page.locator('[aria-rowindex="3"]').locator('[aria-colindex="5"]')).to_contain_text("11:18")
        #  check total count
        expect(page.locator(TOTAL_AUDIO_MIN)).to_contain_text("1073")
        expect(page.locator(TOTAL_AUDIO_HOURS)).to_contain_text("17:53")

    with allure.step("Fill search by service1"):
        page.locator(SEARCH_IN_CONSUMPTION_AUDIO).locator('[type="text"]').fill("service1")

    with allure.step("Check search that service2 not visible"):
        expect(page.locator('[class*="communicationsStyles_table_"]')).not_to_contain_text("service2")

    with allure.step("Go to consumption history GPT"):
        page.locator(BUTTON_CONSUMPTION_HISTORY_GPT).click()

    with allure.step("Check exist search, calendar, mocked data and total count"):
        expect(page.locator(SEARCH_IN_CONSUMPTION_GPT)).to_have_count(1)
        expect(page.locator('[placeholder="Поиск по движку, модели, типу коммуникации или запросу"]')).to_have_count(1)
        expect(page.locator(CALENDAR_IN_CONSUMPTION)).to_have_count(1)
        #  check first row
        expect(page.locator('[aria-rowindex="2"]').locator('[aria-colindex="1"]')).to_contain_text("30.07.2024")
        expect(page.locator('[aria-rowindex="2"]').locator('[aria-colindex="2"]')).to_contain_text("yandex_gpt")
        expect(page.locator('[aria-rowindex="2"]').locator('[aria-colindex="3"]')).to_contain_text("yandexgpt-lite")
        expect(page.locator('[aria-rowindex="2"]').locator('[aria-colindex="4"]')).to_contain_text("call")
        expect(page.locator('[aria-rowindex="2"]').locator('[aria-colindex="5"]')).to_contain_text("title1")
        expect(page.locator('[aria-rowindex="2"]').locator('[aria-colindex="6"]')).to_contain_text("200")
        expect(page.locator('[aria-rowindex="2"]').locator('[aria-colindex="7"]')).to_contain_text("111")
        expect(page.locator('[aria-rowindex="2"]').locator('[aria-colindex="8"]')).to_contain_text("7.47")
        #  check second row
        expect(page.locator('[aria-rowindex="3"]').locator('[aria-colindex="1"]')).to_contain_text("29.07.2024")
        expect(page.locator('[aria-rowindex="3"]').locator('[aria-colindex="2"]')).to_contain_text("chat_gpt")
        expect(page.locator('[aria-rowindex="3"]').locator('[aria-colindex="3"]')).to_contain_text("gpt-3.5-turbo")
        expect(page.locator('[aria-rowindex="3"]').locator('[aria-colindex="4"]')).to_contain_text("call")
        expect(page.locator('[aria-rowindex="3"]').locator('[aria-colindex="5"]')).to_contain_text("title2")
        expect(page.locator('[aria-rowindex="3"]').locator('[aria-colindex="6"]')).to_contain_text("299")
        expect(page.locator('[aria-rowindex="3"]').locator('[aria-colindex="7"]')).to_contain_text("222")
        expect(page.locator('[aria-rowindex="3"]').locator('[aria-colindex="8"]')).to_contain_text("7.42")
        #  check total count
        expect(page.locator(TOTAL_GPT_MONEY)).to_contain_text("14.89")

    with allure.step("Fill search by ya"):
        page.locator(SEARCH_IN_CONSUMPTION_GPT).locator('[type="text"]').fill("ya")

    with allure.step("Check search that chat_gpt not visible"):
        expect(page.locator('[class*="communicationsStyles_table_"]')).not_to_contain_text("chat_gpt")

    with allure.step("Go to consumption history chats"):
        page.locator(BUTTON_CONSUMPTION_HISTORY_CHATS).click()

    with allure.step("Check exist search, calendar, mocked data and total count"):
        expect(page.locator(SEARCH_IN_CONSUMPTION_CHATS)).to_have_count(1)
        expect(page.locator('[placeholder="Поиск по источнику"]')).to_have_count(1)
        expect(page.locator(CALENDAR_IN_CONSUMPTION)).to_have_count(1)
        #  check first row
        expect(page.locator('[aria-rowindex="2"]').locator('[aria-colindex="1"]')).to_contain_text("29.07.2024")
        expect(page.locator('[aria-rowindex="2"]').locator('[aria-colindex="2"]')).to_contain_text("chat1")
        expect(page.locator('[aria-rowindex="2"]').locator('[aria-colindex="3"]')).to_contain_text("999")
        #  check second row
        expect(page.locator('[aria-rowindex="3"]').locator('[aria-colindex="1"]')).to_contain_text("30.07.2024")
        expect(page.locator('[aria-rowindex="3"]').locator('[aria-colindex="2"]')).to_contain_text("chat2")
        expect(page.locator('[aria-rowindex="3"]').locator('[aria-colindex="3"]')).to_contain_text("9002")
        #  check total count
        expect(page.locator(TOTAL_CHATS)).to_contain_text("10001")

    with allure.step("Fill search by chat1"):
        page.locator(SEARCH_IN_CONSUMPTION_CHATS).locator('[type="text"]').fill("chat1")

    with allure.step("Check search that chat_gpt not visible"):
        expect(page.locator('[class*="communicationsStyles_table_"]')).not_to_contain_text("chat2")

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)



@pytest.mark.independent
@pytest.mark.settings
@allure.title("test_user_consumption_history_if_empty")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_user_consumption_history. mocked. check have warning if []")
def test_user_consumption_history_if_empty(base_url, page: Page) -> None:

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to page"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with user"):
        auth(LOGIN_USER, PASSWORD, page)

    with allure.step("Go to settings"):
        click_settings(page)

    with allure.step("Go to consumption history"):
        page.locator(BUTTON_CONSUMPTION_HISTORY).click()

    with allure.step("Check exist search, calendar, mocked data and total count"):
        expect(page.locator('[class*="styles_firstLine"]')).to_have_count(1) # warning message
        expect(page.locator(SEARCH_IN_CONSUMPTION_AUDIO)).to_have_count(1)
        expect(page.locator('[placeholder="Поиск по источнику"]')).to_have_count(1)
        expect(page.locator(CALENDAR_IN_CONSUMPTION)).to_have_count(1)

    with allure.step("Go to consumption history GPT"):
        page.locator(BUTTON_CONSUMPTION_HISTORY_GPT).click()

    with allure.step("Check exist search, calendar, mocked data and total count"):
        expect(page.locator('[class*="styles_firstLine"]')).to_have_count(1)  # warning message
        expect(page.locator(SEARCH_IN_CONSUMPTION_GPT)).to_have_count(1)
        expect(page.locator('[placeholder="Поиск по движку, модели, типу коммуникации или запросу"]')).to_have_count(1)
        expect(page.locator(CALENDAR_IN_CONSUMPTION)).to_have_count(1)

    with allure.step("Go to consumption history chats"):
        page.locator(BUTTON_CONSUMPTION_HISTORY_CHATS).click()

    with allure.step("Check exist search, calendar, mocked data and total count"):
        expect(page.locator('[class*="styles_firstLine"]')).to_have_count(1)  # warning message
        expect(page.locator(SEARCH_IN_CONSUMPTION_CHATS)).to_have_count(1)
        expect(page.locator('[placeholder="Поиск по источнику"]')).to_have_count(1)
        expect(page.locator(CALENDAR_IN_CONSUMPTION)).to_have_count(1)


    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)