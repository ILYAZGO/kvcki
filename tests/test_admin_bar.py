from playwright.sync_api import Page, expect
from utils.variables import *
from pages.adminbar import *
import pytest
from utils.create_delete_user import create_user, delete_user, give_user_to_manager, create_operator, give_access_right
import allure


@pytest.mark.e2e
@pytest.mark.adminbar
@allure.title("test_admin_bar_with_admin")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("")
def test_admin_bar_with_admin(base_url, page) -> None:
    admin_bar = AdminBar(page)

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Create admin"):
        USER_ID_ADMIN, TOKEN_ADMIN, LOGIN_ADMIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    with allure.step("Go to url"):
        admin_bar.navigate(base_url)

    with allure.step("Auth"):
        admin_bar.auth(LOGIN_ADMIN, PASSWORD)

    with allure.step("Check admin name have count 2"):
        expect(page.get_by_text(LOGIN_ADMIN)).to_have_count(2, timeout=wait_until_visible)

    with allure.step("Go to user"):
        admin_bar.go_to_user(LOGIN_USER)

    with allure.step("Check admin name have count 1 and user name have count 1 and users button have count 1"):
        expect(page.get_by_text(LOGIN_ADMIN)).to_have_count(1, timeout=wait_until_visible)
        expect(page.get_by_text(LOGIN_USER, exact=True)).to_have_count(1, timeout=wait_until_visible)
        expect(page.locator(BUTTON_USERS)).to_be_visible()

    with allure.step("Go back in admin"):
        admin_bar.back_arrow_click()

    with allure.step("Check admin name have count 2"):
        expect(page.get_by_text(LOGIN_ADMIN)).to_have_count(2, timeout=wait_until_visible)

    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN_ADMIN, USER_ID_ADMIN)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)


@pytest.mark.e2e
@pytest.mark.adminbar
@allure.title("test_admin_bar_with_manager")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("")
def test_admin_bar_with_manager(base_url, page: Page) -> None:
    admin_bar = AdminBar(page)

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Create manager"):
        USER_ID_MANAGER, TOKEN_MANAGER, LOGIN_MANAGER = create_user(API_URL, ROLE_MANAGER, PASSWORD)

    with allure.step("Give user to manager"):
        give_user_to_manager(API_URL, USER_ID_MANAGER, USER_ID_USER, TOKEN_MANAGER)

    with allure.step("Go to url"):
        admin_bar.navigate(base_url)

    with allure.step("Auth"):
        admin_bar.auth(LOGIN_MANAGER, PASSWORD)

    with allure.step("Check manager name have count 2"):
        expect(page.get_by_text(LOGIN_MANAGER)).to_have_count(2, timeout=wait_until_visible)

    with allure.step("Go to user"):
        admin_bar.go_to_user(LOGIN_USER)

    with allure.step("Check manager name have count 1 and user name have count 1 and users button have count 1"):
        expect(page.get_by_text(LOGIN_MANAGER)).to_have_count(1, timeout=wait_until_visible)
        expect(page.get_by_text(LOGIN_USER, exact=True)).to_have_count(1, timeout=wait_until_visible)
        expect(page.locator(BUTTON_USERS)).to_be_visible()

    with allure.step("Go back in manager"):
        admin_bar.back_arrow_click()

    with allure.step("Check manager name have count 2"):
        expect(page.get_by_text(LOGIN_MANAGER)).to_have_count(2, timeout=wait_until_visible)

    with allure.step("Delete manager"):
        delete_user(API_URL, TOKEN_MANAGER, USER_ID_MANAGER)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)


###
@pytest.mark.e2e
@pytest.mark.adminbar
@allure.title("test_admin_bar_with_manager")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("")
def test_new_admin_bar_with_manager(base_url, page: Page) -> None:
    admin_bar = AdminBar(page)

    with allure.step("Create user1"):
        USER_ID_USER1, TOKEN_USER, LOGIN_USER1 = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Create user2"):
        USER_ID_USER2, TOKEN_USER, LOGIN_USER2 = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Create manager"):
        USER_ID_MANAGER, TOKEN_MANAGER, LOGIN_MANAGER = create_user(API_URL, ROLE_MANAGER, PASSWORD)

    # with allure.step("Give user to manager"):
    #     give_user_to_manager(API_URL, USER_ID_MANAGER, USER_ID_USER, TOKEN_MANAGER)

    with allure.step("Go to url"):
        admin_bar.navigate(base_url)

    with allure.step("Auth with manager"):
        admin_bar.auth(LOGIN_MANAGER, PASSWORD)

    with allure.step("Check manager name have count 2 and admin bar is visible"):
        expect(page.locator(BLOCK_ADMIN_BAR)).to_be_visible()
        expect(page.locator(BUTTON_USERS)).to_be_visible()
        expect(page.get_by_text(LOGIN_MANAGER)).to_have_count(2, timeout=wait_until_visible)

    with allure.step("Click users list"):
        page.locator("#react-select-2-input").click()
        page.wait_for_selector(MENU)

    with allure.step("Check that users list is empty"):
        expect(page.locator(MENU)).to_have_text("No options")

    with allure.step("Quit from profile"):
        admin_bar.quit_from_profile()

    with allure.step("Change access right add_user:True"):
        rights = {
            "restt":False,
            "delete_user":False,
            "add_user":True,
            "set_default_engine":False,
            "quota_edit":False,
            "gpt_quota":False,
            "user_modules_setup":False}
        give_access_right(API_URL, TOKEN_USER, USER_ID_MANAGER, rights)

    with allure.step("Auth with manager"):
        admin_bar.auth(LOGIN_MANAGER, PASSWORD)

    with allure.step("Check manager name have count 2 and admin bar is visible"):
        expect(page.locator(BLOCK_ADMIN_BAR)).to_be_visible()
        expect(page.locator(BUTTON_USERS)).to_be_visible()
        expect(page.get_by_text(LOGIN_MANAGER)).to_have_count(2, timeout=wait_until_visible)

    with allure.step("Click users list"):
        page.locator("#react-select-2-input").click()
        page.wait_for_selector(MENU)

    with allure.step("Check that users list is empty"):
        expect(page.locator(MENU)).to_have_text("No options")

    with allure.step("Quit from profile"):
        admin_bar.quit_from_profile()

    with allure.step("Give user to manager"):
        give_user_to_manager(API_URL, USER_ID_MANAGER, USER_ID_USER1, TOKEN_MANAGER)

    with allure.step("Auth with manager"):
        admin_bar.auth(LOGIN_MANAGER, PASSWORD)

    with allure.step("Go to user"):
        admin_bar.go_to_user(LOGIN_USER1)

    with allure.step("Check manager name have count 1 and user name have count 1 and users button have count 1"):
        expect(page.get_by_text(LOGIN_MANAGER)).to_have_count(1, timeout=wait_until_visible)
        expect(page.get_by_text(LOGIN_USER1, exact=True)).to_have_count(1, timeout=wait_until_visible)
        expect(page.locator(BUTTON_USERS)).to_be_visible()

    with allure.step("Go back in manager"):
        admin_bar.back_arrow_click()

    with allure.step("Check manager name have count 2"):
        expect(page.locator(BLOCK_ADMIN_BAR)).to_be_visible()
        expect(page.locator(BUTTON_USERS)).to_be_visible()
        expect(page.get_by_text(LOGIN_MANAGER)).to_have_count(2, timeout=wait_until_visible)

    with allure.step("Quit from profile"):
        admin_bar.quit_from_profile()

    with allure.step("Change access right all False"):
        rights = {
            "restt":False,
            "delete_user":False,
            "add_user":False,
            "set_default_engine":False,
            "quota_edit":False,
            "gpt_quota":False,
            "user_modules_setup":False}
        give_access_right(API_URL, TOKEN_USER, USER_ID_MANAGER, rights)

    with allure.step("Auth"):
        admin_bar.auth(LOGIN_MANAGER, PASSWORD)

    with allure.step("Check that admin bar not visible and we inside manager's user"):
        expect(page.locator(BLOCK_ADMIN_BAR)).not_to_be_visible()
        expect(page.locator(BUTTON_USERS)).not_to_be_visible()
        expect(page.locator(BUTTON_FIND_COMMUNICATIONS)).to_be_visible()
        expect(page.locator('[class*="MuiAccordionSummary-content"]')).to_have_count(1)

    with allure.step("Quit from profile"):
        admin_bar.quit_from_profile()

    with allure.step("Give user2 to manager"):
        give_user_to_manager(API_URL, USER_ID_MANAGER, USER_ID_USER2, TOKEN_MANAGER)

    with allure.step("Auth"):
        admin_bar.auth(LOGIN_MANAGER, PASSWORD)

    with allure.step("Click users list"):
        page.locator("#react-select-2-input").click()
        page.wait_for_selector(MENU)

    with allure.step("Check that users list is empty"):
        expect(page.locator(MENU)).to_have_text(f"{LOGIN_USER1}{LOGIN_USER2}")

    with allure.step("Quit from profile"):
        admin_bar.quit_from_profile()

    with allure.step("Change access right add_user: True"):
        rights = {
            "restt": False,
            "delete_user": False,
            "add_user": True,
            "set_default_engine": False,
            "quota_edit": False,
            "gpt_quota": False,
            "user_modules_setup": False}
        give_access_right(API_URL, TOKEN_USER, USER_ID_MANAGER, rights)

    with allure.step("Auth"):
        admin_bar.auth(LOGIN_MANAGER, PASSWORD)

    with allure.step("Click users list"):
        page.locator("#react-select-2-input").click()
        page.wait_for_selector(MENU)

    with allure.step("Check that users list is empty"):
        expect(page.locator(MENU)).to_have_text(f"{LOGIN_USER1}{LOGIN_USER2}")

    with allure.step("Quit from profile"):
        admin_bar.quit_from_profile()

    with allure.step("Delete manager"):
        delete_user(API_URL, TOKEN_MANAGER, USER_ID_MANAGER)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER1)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER1)

####


@pytest.mark.e2e
@pytest.mark.adminbar
@allure.title("test_language_change_by_user")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("")
def test_language_change_by_user(base_url, page: Page) -> None:
    admin_bar = AdminBar(page)

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        admin_bar.navigate(base_url)

    with allure.step("Auth"):
        admin_bar.auth(LOGIN_USER, PASSWORD)

    with allure.step("Change lang from RU to EN"):
        admin_bar.change_lang("RU", "EN")

    with allure.step("Check that lang changed"):
        expect(page.get_by_text("Additional filters")).to_be_visible(timeout=wait_until_visible)

    with allure.step("Change lang from EN to ES"):
        admin_bar.change_lang("EN", "ES")

    with allure.step("Check that lang changed"):
        expect(page.get_by_text("Filtros adicionales")).to_be_visible(timeout=wait_until_visible)

    with allure.step("Change lang from ES to PT"):
        admin_bar.change_lang("ES", "PT")

    with allure.step("Check that lang changed"):
        expect(page.get_by_text("Filtros adicionais")).to_be_visible(timeout=wait_until_visible)

    with allure.step("Change lang from PT to RU"):
        admin_bar.change_lang("PT", "RU")

    with allure.step("Check that lang changed"):
        expect(page.get_by_text("Дополнительные фильтры")).to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)


@pytest.mark.e2e
@pytest.mark.adminbar
@allure.title("test_language_change_by_user_and_operator")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("")
def test_language_change_by_user_and_operator(base_url, page: Page) -> None:
    admin_bar = AdminBar(page)

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Create operator"):
        USER_ID_OPERATOR, TOKEN_OPERATOR, LOGIN_OPERATOR = create_operator(API_URL, USER_ID_USER, PASSWORD)

    with allure.step("Go to url"):
        admin_bar.navigate(base_url)

    with allure.step("Auth with user"):
        admin_bar.auth(LOGIN_USER, PASSWORD)

    with allure.step("Change users lang from RU to EN"):
        admin_bar.change_lang("RU", "EN")

    with allure.step("Check that users lang changed"):
        expect(page.get_by_text("Additional filters")).to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("Communication time interval")).to_be_visible(timeout=wait_until_visible)

    with allure.step("Quit from user"):
        admin_bar.quit_from_profile()

    with allure.step("Check quited"):
        admin_bar.assert_quited()

    with allure.step("Auth with operator"):
        admin_bar.auth(LOGIN_OPERATOR, PASSWORD)

    with allure.step("Check that operators lang RU how it was created"):
        expect(page.get_by_text("Дополнительные фильтры")).to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("Время коммуникации")).to_be_visible(timeout=wait_until_visible)

    with allure.step("Change operator lang from RU to PT"):
        admin_bar.change_lang("RU", "PT")

    with allure.step("Check that operators lang PT"):
        expect(page.get_by_text("Filtros adicionais")).to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("Tempo de comunicação")).to_be_visible(timeout=wait_until_visible)

    with allure.step("Quit from operator"):
        admin_bar.quit_from_profile()

    with allure.step("Check quited"):
        admin_bar.assert_quited()

    with allure.step("Auth with user"):
        admin_bar.auth(LOGIN_USER, PASSWORD)

    with allure.step("Check that users lang changed"):
        expect(page.get_by_text("Additional filters")).to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("Communication time interval")).to_be_visible(timeout=wait_until_visible)

    with allure.step("Change users lang from RU to EN"):
        admin_bar.change_lang("EN", "ES")

    with allure.step("Check that users lang changed"):
        expect(page.get_by_text("Filtros adicionales")).to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("Tiempo de comunicación")).to_be_visible(timeout=wait_until_visible)

    with allure.step("Quit from user"):
        admin_bar.quit_from_profile()

    with allure.step("Check quited"):
        admin_bar.assert_quited()

    with allure.step("Auth with operator"):
        admin_bar.auth(LOGIN_OPERATOR, PASSWORD)

    with allure.step("Check that operators lang PT"):
        expect(page.get_by_text("Filtros adicionais")).to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("Tempo de comunicação")).to_be_visible(timeout=wait_until_visible)

    with allure.step("Quit from user"):
        admin_bar.quit_from_profile()

    with allure.step("Check quited"):
        admin_bar.assert_quited()

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)

    with allure.step("Delete operator"):
        delete_user(API_URL, TOKEN_OPERATOR, USER_ID_OPERATOR)