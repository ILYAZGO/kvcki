from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.settings import *
from utils.create_delete_user import create_user, delete_user, give_user_to_manager, create_operator
import pytest
import allure
import random

# input text to address-book, save, check that text saved

@pytest.mark.settings
@allure.title("test_address_book_fill_by_user")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("input text to address-book, save, check that text saved")
def test_address_book_fill_by_user(page: Page) -> None:
    
    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)
    
    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)
    
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


@pytest.mark.settings
@allure.title("test_admin_can_change_login_for_manager")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("check admin can change login for manager")
def test_admin_can_change_login_for_manager(page: Page) -> None:

    CHANGED_LOGIN = f"auto_test_user_ch_{datetime.now().strftime('%m%d%H%M')}{datetime.now().microsecond}"
    
    with allure.step("Create admin"):
        USER_ID_ADMIN, TOKEN_ADMIN, LOGIN_ADMIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)
    
    with allure.step("Create manager"):
        USER_ID_MANAGER, TOKEN_MANAGER, LOGIN_MANAGER = create_user(API_URL, ROLE_MANAGER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)
    
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


@pytest.mark.settings
@allure.title("test_admin_can_change_login_for_user_and_operator")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("check admin can change login for user and operator")
def test_admin_can_change_login_for_user_and_operator(page: Page) -> None:

    NEW_OPERATOR_NAME = NEW_OPERATOR_LOGIN = f"auto_test_operator_{datetime.now().strftime('%m%d%H%M')}_{datetime.now().microsecond}"
    CHANGED_LOGIN = f"auto_test_user_ch_{datetime.now().strftime('%m%d%H%M')}{datetime.now().microsecond}"

    with allure.step("Create admin"):
        USER_ID_ADMIN, TOKEN_ADMIN, LOGIN_ADMIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)
    
    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)
    
    with allure.step("Create operator"):
        USER_ID_OPERATOR, TOKEN_OPERATOR, LOGIN_OPERATOR = create_operator(API_URL, USER_ID_USER, PASSWORD)
    
    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)
    
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
        page.wait_for_timeout(300)
    
    with allure.step("Check that login changed"):
        expect(page.locator(INPUT_LOGIN)).to_have_value(CHANGED_LOGIN)

    # change for operator
    
    with allure.step("Go to employees from ltfy menu"):
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
        page.wait_for_timeout(300)
    
    with allure.step("Check that login changed"):
        expect(page.locator(INPUT_LOGIN)).to_have_value(NEW_OPERATOR_LOGIN)
    
    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN_ADMIN, USER_ID_ADMIN)
    
    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)
    
    with allure.step("Delete operator"):
        delete_user(API_URL, TOKEN_OPERATOR, USER_ID_OPERATOR)


#
@pytest.mark.settings
@allure.title("test_user_cant_change_login_for_operator")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("check that changing login disabled for operator")
def test_user_cant_change_login_for_operator(page: Page) -> None:

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Crete operator"):
        USER_ID_OPERATOR, TOKEN_OPERATOR, LOGIN_OPERATOR = create_operator(API_URL, USER_ID_USER, PASSWORD)

    with allure.step("Go to page"):
        page.goto(URL, timeout=timeout)

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


@pytest.mark.settings
@allure.title("test_manager_cant_change_login_for_user_and_operator")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_manager_cant_change_login_for_user_and_operator")
def test_manager_cant_change_login_for_user_and_operator(page: Page) -> None:
    with allure.step("Create manager"):
        USER_ID_MANAGER, TOKEN_MANAGER, LOGIN_MANAGER = create_user(API_URL, ROLE_MANAGER, PASSWORD)

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)
        give_user_to_manager(API_URL, USER_ID_MANAGER, USER_ID_USER, TOKEN_MANAGER)

    with allure.step("Create operator"):
        USER_ID_OPERATOR, TOKEN_OPERATOR, LOGIN_OPERATOR = create_operator(API_URL, USER_ID_USER, PASSWORD)

    with allure.step("Go to page"):
        page.goto(URL, timeout=timeout)

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



@pytest.mark.settings
@allure.title("test_admin_can_change_rights_for_manager")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("check admin can change rights for manager")
def test_admin_can_change_rights_for_manager(page: Page) -> None:
    
    with allure.step("Create admin"):
        USER_ID_ADMIN, TOKEN_ADMIN, LOGIN_ADMIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)
    
    with allure.step("Create manager"):
        USER_ID_MANAGER, TOKEN_MANAGER, LOGIN_MANAGER = create_user(API_URL, ROLE_MANAGER, PASSWORD)
    
    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)

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


@pytest.mark.settings
@allure.title("test_admin_can_change_rights_for_user_and_operator")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("check admin can change rights for user and operator")
def test_admin_can_change_rights_for_user_and_operator(page: Page) -> None:

    with allure.step("Create admin"):
        USER_ID_ADMIN, TOKEN_ADMIN, LOGIN_ADMIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)
    
    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)
    
    with allure.step("Create operator"):
        USER_ID_OPERATOR, TOKEN_OPERATOR, LOGIN_OPERATOR = create_operator(API_URL, USER_ID_USER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)

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
    
    with allure.step("Check that operator have 23 rights"):
        expect(page.locator(BLOCK_ONE_RIGHT)).to_have_count(23)
    
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


@pytest.mark.settings
@allure.title("test_user_can_change_rights_for_operator")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check user can change rights for operator")
def test_user_can_change_rights_for_operator(page: Page) -> None:

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Create operator"):
        USER_ID_OPERATOR, TOKEN_OPERATOR, LOGIN_OPERATOR = create_operator(API_URL, USER_ID_USER, PASSWORD)

    with allure.step("Go to page"):
        page.goto(URL, timeout=timeout)

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

    with allure.step("Check that operator have 23 rights in list"):
        expect(page.locator(BLOCK_ONE_RIGHT)).to_have_count(23)

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


@pytest.mark.settings
@allure.title("test_change_personal_information_save_admin_itself")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check changing and saving personal info for admin")
def test_change_personal_information_save_admin_itself(page: Page) -> None:

    NEW_NAME = NEW_LOGIN = f"auto_test_user_{datetime.now().strftime('%m%d%H%M')}_{datetime.now().microsecond}"
    EMAIL = f"email_{datetime.now().microsecond}{random.randint(100, 200)}@mail.ru"

    with allure.step("Create admin"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    with allure.step("Go to page"):
        page.goto(URL, timeout=timeout)

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
        page.wait_for_timeout(300)

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



@pytest.mark.settings
@allure.title("test_change_personal_information_save_manager_itself")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check changing and saving personal info for manager")
def test_change_personal_information_save_manager_itself(page: Page) -> None:

    NEW_NAME = NEW_LOGIN = f"auto_test_user_{datetime.now().strftime('%m%d%H%M')}_{datetime.now().microsecond}"
    EMAIL = f"email_{datetime.now().microsecond}{random.randint(100, 999)}@mail.ru"

    with allure.step("Create admin"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_MANAGER, PASSWORD)

    with allure.step("Go to page"):
        page.goto(URL, timeout=timeout)

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
        page.wait_for_timeout(300)

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


@pytest.mark.settings
@allure.title("test_change_personal_information_save_user_itself")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check changing and saving personal info for user")
def test_change_personal_information_save_user_itself(page: Page) -> None:

    NEW_NAME = NEW_LOGIN = f"auto_test_user_{datetime.now().strftime('%m%d%H%M')}_{datetime.now().microsecond}"
    EMAIL = f"email_{datetime.now().microsecond}{random.randint(100, 999)}@mail.ru"

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to page"):
        page.goto(URL, timeout=timeout)

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


@pytest.mark.settings
@allure.title("test_change_personal_information_save_operator_itself")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check changing and saving personal info for operator")
def test_change_personal_information_save_operator_itself(page: Page) -> None:

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Create operator"):
        USER_ID_OPERATOR, TOKEN_OPERATOR, LOGIN_OPERATOR = create_operator(API_URL, USER_ID_USER, PASSWORD)

    with allure.step("Go to page"):
        page.goto(URL, timeout=timeout)

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


@pytest.mark.settings
@allure.title("test_change_personal_information_save_operator_by_admin")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check changing and saving personal info for operator by admin")
def test_change_personal_information_save_operator_by_admin(page: Page) -> None:

    NEW_OPERATOR_NAME = NEW_OPERATOR_LOGIN = f"auto_test_operator_{datetime.now().strftime('%m%d%H%M')}_{datetime.now().microsecond}"
    EMAIL = f"email_{datetime.now().microsecond}{random.randint(100, 999)}@mail.ru"

    with allure.step("Create admin"):
        USER_ID_ADMIN, TOKEN_ADMIN, LOGIN_ADMIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Create operator"):
        USER_ID_OPERATOR, TOKEN_OPERATOR, LOGIN_OPERATOR = create_operator(API_URL, USER_ID_USER, PASSWORD)

    with allure.step("Go to page"):
        page.goto(URL, timeout=timeout)

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


@pytest.mark.settings
@allure.title("test_change_personal_information_save_operator_by_user")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check changing and saving personal info for operator by user")
def test_change_personal_information_save_operator_by_user(page: Page) -> None:

    NEW_OPERATOR_NAME = NEW_OPERATOR_LOGIN = f"auto_test_operator_{datetime.now().strftime('%m%d%H%M')}_{datetime.now().microsecond}"
    EMAIL = f"email_{datetime.now().microsecond}{random.randint(100, 999)}@mail.ru"

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Create operator"):
        USER_ID_OPERATOR, TOKEN_OPERATOR, LOGIN_OPERATOR = create_operator(API_URL, USER_ID_USER, PASSWORD)

    with allure.step("Go to page"):
        page.goto(URL, timeout=timeout)

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


@pytest.mark.settings
@allure.title("test_left_menu_items_for_admin_itself")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check how many items in left menu for role")
def test_left_menu_items_for_admin_itself(page: Page) -> None:

    with allure.step("Create admin"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    with allure.step("Go to page"):
        page.goto(URL, timeout=timeout)

    with allure.step("Auth with admin"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to settings"):
        click_settings(page)

    with allure.step("Check items in left menu"):
        expect(page.locator(BLOCK_LEFT_MENU)).to_contain_text(['Персональная информация'])
        expect(page.locator(LEFT_MENU_ITEM)).to_have_count(1)

    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.settings
@allure.title("test_left_menu_items_for_manager_itself")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check how many items in left menu for role")
def test_left_menu_items_for_manager_itself(page: Page) -> None:

    with allure.step("Create manager"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_MANAGER, PASSWORD)

    with allure.step("Go to page"):
        page.goto(URL, timeout=timeout)

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
@pytest.mark.settings
@allure.title("test_left_menu_items_for_user_itself")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check how many items in left menu for role")
def test_left_menu_items_for_user_itself(page: Page) -> None:

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to page"):
        page.goto(URL, timeout=timeout)

    with allure.step("Auth with user"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to settings"):
        click_settings(page)

    with allure.step("Check items in left menu"):
        expect(page.locator(BLOCK_LEFT_MENU)).to_contain_text(['Персональная информацияСотрудникиДействия с коммуникациямиКвоты777Адресная книгаИнтеграции'])
        expect(page.locator(LEFT_MENU_ITEM)).to_have_count(6)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


# check how many items in left menu for role
@pytest.mark.settings
@allure.title("test_left_menu_items_for_operator_itself")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check how many items in left menu for role")
def test_left_menu_items_for_operator_itself(page: Page) -> None:

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Create operstor"):
        USER_ID_OPERATOR, TOKEN_OPERATOR, LOGIN_OPERATOR = create_operator(API_URL,USER_ID_USER,PASSWORD)

    with allure.step("Go to page"):
        page.goto(URL, timeout=timeout)

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


@pytest.mark.settings
@allure.title("test_admin_check_industry_and_partner_for_manager")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_admin_check_industry_and_partner_for_manager")
def test_admin_check_industry_and_partner_for_manager(page: Page) -> None:

    with allure.step("Create admin"):
        USER_ID_ADMIN, TOKEN_ADMIN, LOGIN_ADMIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    with allure.step("Create manager"):
        USER_ID_MANAGER, TOKEN_MANAGER, LOGIN_MANAGER = create_user(API_URL, ROLE_MANAGER, PASSWORD)

    with allure.step("Go to page"):
        page.goto(URL, timeout=timeout)

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


@pytest.mark.settings
@allure.title("test_admin_check_industry_and_partner_for_user_and_operator")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_admin_check_industry_and_partner_for_user_and_operator")
def test_admin_check_industry_and_partner_for_user_and_operator(page: Page) -> None:

    with allure.step("Create admin"):
        USER_ID_ADMIN, TOKEN_ADMIN, LOGIN_ADMIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Create operator"):
        USER_ID_OPERATOR, TOKEN_OPERATOR, LOGIN_OPERATOR = create_operator(API_URL, USER_ID_USER, PASSWORD)

    with allure.step("Go to page"):
        page.goto(URL, timeout=timeout)

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


@pytest.mark.settings
@allure.title("test_manager_check_industry_and_partner_for_user_and_operator")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_manager_check_industry_and_partner_for_user_and_operator")
def test_manager_check_industry_and_partner_for_user_and_operator(page: Page) -> None:

    with allure.step("Create manager"):
        USER_ID_MANAGER, TOKEN_MANAGER, LOGIN_MANAGER = create_user(API_URL, ROLE_MANAGER, PASSWORD)

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)
        give_user_to_manager(API_URL, USER_ID_MANAGER, USER_ID_USER, TOKEN_MANAGER)

    with allure.step("Create operator"):
        USER_ID_OPERATOR, TOKEN_OPERATOR, LOGIN_OPERATOR = create_operator(API_URL, USER_ID_USER, PASSWORD)

    with allure.step("Go to page"):
        page.goto(URL, timeout=timeout)

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


@pytest.mark.settings
@allure.title("test_giving_communications_quota_by_admin")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("every auto_test_user gets 777 min quota by default. test check that we can add more")
def test_giving_communications_quota_by_admin(page: Page) -> None:

    with allure.step("Create admin"):
        USER_ID_ADMIN, TOKEN_ADMIN, LOGIN_ADMIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to page"):
        page.goto(URL, timeout=timeout)

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


@pytest.mark.settings
@allure.title("test_giving_gpt_quota_by_admin")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("every auto_test_user gets 777 min quota by default. test check that we can add more")
def test_giving_gpt_quota_by_admin(page: Page) -> None:

    with allure.step("Create admin"):
        USER_ID_ADMIN, TOKEN_ADMIN, LOGIN_ADMIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to page"):
        page.goto(URL, timeout=timeout)

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
        expect(page.locator(BLOCK_CHAT_GPT).locator(BLOCK_WITH_AMOUNT).nth(1)).to_have_text("150")

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
        expect(page.locator(BLOCK_YANDEX_GPT).locator(BLOCK_WITH_AMOUNT).nth(1)).to_have_text("15000")

    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN_ADMIN, USER_ID_ADMIN)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)

@pytest.mark.settings
@allure.title("test_user_cant_change_quotas")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("every auto_test_user gets 777 min quota by default. test check that we can add more")
def test_user_cant_change_quotas(page: Page) -> None:

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to page"):
        page.goto(URL, timeout=timeout)

    with allure.step("Auth with admin"):
        auth(LOGIN_USER, PASSWORD, page)

    #with allure.step("Go to user"):
    #    go_to_user(LOGIN_USER, page)

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