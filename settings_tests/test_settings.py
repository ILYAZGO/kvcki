from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.settings import *
from utils.create_delete_user import create_user, delete_user, give_user_to_manager, create_operator
import pytest
import allure

# input text to address-book, save, check that text saved
@pytest.mark.independent
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


@pytest.mark.independent
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
        page.wait_for_timeout(300)
    
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
@pytest.mark.independent
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


@pytest.mark.independent
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
    
    with allure.step("Check that manager have 5 right"):
        expect(page.locator(BLOCK_ONE_RIGHT)).to_have_count(5)
    
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
    
    with allure.step("Check that operator have 22 rights"):
        expect(page.locator(BLOCK_ONE_RIGHT)).to_have_count(22)
    
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

    with allure.step("Check that operator have 22 rights in list"):
        expect(page.locator(BLOCK_ONE_RIGHT)).to_have_count(22)

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
        expect(page.get_by_text("Africa/Bamako")).to_be_visible()
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
        expect(page.get_by_text("Africa/Bamako")).to_be_visible()
        expect(page.locator(SELECT_INDUSTRY)).not_to_be_visible()
        expect(page.locator(SELECT_PARTNER)).not_to_be_visible()

    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN, USER_ID)



@pytest.mark.independent
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
        expect(page.get_by_text("Africa/Bamako")).to_be_visible()
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
        expect(page.get_by_text("Africa/Bamako")).to_be_visible()
        expect(page.locator(SELECT_INDUSTRY)).not_to_be_visible()
        expect(page.locator(SELECT_PARTNER)).not_to_be_visible()

    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
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
        expect(page.get_by_text("Africa/Bamako")).to_be_visible()
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
        expect(page.get_by_text("Africa/Bamako")).to_be_visible()
        expect(page.locator(SELECT_INDUSTRY)).not_to_be_visible()
        expect(page.locator(SELECT_PARTNER)).not_to_be_visible()

    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
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





@pytest.mark.independent
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


@pytest.mark.independent
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
@pytest.mark.independent
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
@pytest.mark.independent
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