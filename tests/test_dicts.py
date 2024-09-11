from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.markup import *
from utils.create_delete_user import create_user, delete_user, give_user_to_manager
import pytest
import allure


@pytest.mark.independent
@pytest.mark.dictionaries
@allure.title("test_add_dict_inside_group")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Create dict inside group by user")
def test_add_dict_inside_group(base_url, page: Page) -> None:

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with user"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to dicts"):
        go_to_dicts(page)

    with allure.step("Create group"):
        create_group("12345", page)

    with allure.step("Click on group"):
        page.locator(CLICK_ON_GROUP).click()

    with allure.step("Create dict"):
        create_dict("98765", page)

    with allure.step("Check that dict created"):
        expect(page.locator(NAZVANIE_SLOVARYA)).to_have_value("98765")

    with allure.step("Check that dict belongs to parent group"):
        expect(page.get_by_text("12345").nth(1)).to_have_text("12345")
        page.wait_for_timeout(300)

    with allure.step("Rename dict"):
        page.locator(NAZVANIE_SLOVARYA).clear()
        page.locator(NAZVANIE_SLOVARYA).fill("newName")
        page.get_by_role("button", name="Сохранить").click()
        page.wait_for_timeout(1000)

    with allure.step("Check that name changed"):
        expect(page.locator(NAZVANIE_SLOVARYA)).to_have_value("newName")
        expect(page.locator('[data-testid="test"]')).to_have_text("newName")

    with allure.step("Delete dict and group"):
        delete_group_and_rule_or_dict(page)

    with allure.step("Check that group deleted (group will not be delete if you didnt delete dict)"):
        expect(page.get_by_text("12345")).not_to_be_visible()

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.dictionaries
@allure.title("test_add_dict_outside_group_disabled")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_add_dict_outside_group_disabled")
def test_add_dict_outside_group_disabled(base_url, page: Page) -> None:

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with user"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to dicts"):
        go_to_dicts(page)

    with allure.step("Check that disabled"):
        expect(page.locator(TOOLTIP_BUTTON_DOBAVIT_SLOVAR)).to_be_visible()

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.dictionaries
@allure.title("test_add_dict_group_rename_delete")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_add_dict_group_rename_delete")
def test_add_dict_group_rename_delete(base_url, page: Page) -> None:

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with user"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to dicts"):
        go_to_dicts(page)

    #
    with allure.step("Press (Add group)"):
        page.locator(BUTTON_DOBAVIT_GRUPPU).click()

    with allure.step("Press (Cancel)"):
        page.locator(BUTTON_OTMENA).click()

    with allure.step("Check canceled"):
        expect(page.locator(NI4EGO_NE_NAYDENO)).to_be_visible(timeout=wait_until_visible)  # надпись Ничего не найдено

    with allure.step("Press (Add group)"):
        page.locator(BUTTON_DOBAVIT_GRUPPU).click()

    with allure.step("Press (cross button)"):
        page.locator(BUTTON_KRESTIK).click()

    with allure.step("Check canceled"):
        expect(page.locator(NI4EGO_NE_NAYDENO)).to_be_visible(timeout=wait_until_visible)  # надпись Ничего не найдено
    #

    with allure.step("Create group"):
        create_group("12345", page)

    with allure.step("Rename group"):
        page.wait_for_selector(BUTTON_PENCIL)
        page.locator(BUTTON_PENCIL).click()
        page.locator(INPUT_EDIT_GROUP_NAME).fill("54321")
        page.locator(BUTTON_SAVE_EDITED_NAME).get_by_role("button").first.click()

    with allure.step("Check group created and renamed"):
        expect(page.get_by_text("54321")).to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete group"):
        page.locator(BUTTON_KORZINA).click()

    with allure.step("Check deleted"):
        expect(page.get_by_text("54321")).not_to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.dictionaries
@allure.title("test_check_dict_type")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_check_dict_type")
def test_check_dict_type(base_url, page: Page) -> None:

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with user"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to dicts"):
        go_to_dicts(page)

    with allure.step("Create group"):
        create_group("12345", page)

    with allure.step("Click on group"):
        page.locator(CLICK_ON_GROUP).click()

    with allure.step("Create  group"):
        create_dict("98765", page)

    with allure.step("Check created dict name"):
        expect(page.locator(NAZVANIE_SLOVARYA)).to_have_value("98765")

    with allure.step("Check created dict parent group"):
        expect(page.get_by_text("12345").nth(1)).to_have_text("12345")
        page.wait_for_timeout(500)

    with allure.step("Change dict type"):
        change_dict_type("Обычный словарь", "Словарь автозамен", page)

    with allure.step("Press (Save)"):
        page.get_by_role("button", name="Сохранить").click()
        page.wait_for_timeout(1800)

    with allure.step("Reload page and go to dict"):
        page.reload()
        page.wait_for_selector(BUTTON_DOBAVIT_SLOVAR, timeout=wait_until_visible)
        page.wait_for_timeout(800)
        page.locator('[data-testid="test"]').click()
        page.wait_for_selector(INPUT_SPISOK_SLOV)

    with allure.step("Check that dict type changed and saved"):
        expect(page.get_by_text("Словарь автозамен")).to_have_count(1)

    with allure.step("Change dict type"):
        change_dict_type("Словарь автозамен", "Словарь грамматики", page)

    with allure.step("Press (Save)"):
        page.get_by_role("button", name="Сохранить").click()
        page.wait_for_timeout(1800)

    with allure.step("Reload page and go to dict"):
        page.reload()
        page.wait_for_selector(BUTTON_DOBAVIT_SLOVAR, timeout=wait_until_visible)
        page.wait_for_timeout(800)
        page.locator('[data-testid="test"]').click()
        page.wait_for_selector(INPUT_SPISOK_SLOV)

    with allure.step("Check that dict type changed and saved"):
        expect(page.get_by_text("Словарь грамматики")).to_have_count(1)

    with allure.step("Change dict type"):
        change_dict_type("Словарь грамматики", "Словарь правил грамматики", page)

    with allure.step("Press (Save)"):
        page.get_by_role("button", name="Сохранить").click()
        page.wait_for_timeout(1800)

    with allure.step("Reload page and go to dict"):
        page.reload()
        page.wait_for_selector(BUTTON_DOBAVIT_SLOVAR, timeout=wait_until_visible)
        page.wait_for_timeout(800)
        page.locator('[data-testid="test"]').click()
        page.wait_for_selector(INPUT_SPISOK_SLOV)

    with allure.step("Check that dict type changed and saved"):
        expect(page.get_by_text("Словарь правил грамматики")).to_have_count(1)

    with allure.step("Change dict type"):
        change_dict_type("Словарь правил грамматики", "Обычный словарь", page)

    with allure.step("Press (Save)"):
        page.get_by_role("button", name="Сохранить").click()
        page.wait_for_timeout(2000)

    with allure.step("Reload page and go to dict"):
        page.reload()
        page.wait_for_selector(BUTTON_DOBAVIT_SLOVAR, timeout=wait_until_visible)
        page.wait_for_timeout(800)
        page.locator('[data-testid="test"]').click()
        page.wait_for_selector(INPUT_SPISOK_SLOV)

    with allure.step("Check that dict type changed and saved"):
        expect(page.get_by_text("Обычный словарь")).to_have_count(1)

    with allure.step("Delete dict and group"):
        delete_group_and_rule_or_dict(page)

    with allure.step("Check that dict and group deleted"):
        expect(page.get_by_text("12345")).not_to_be_visible()

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.dictionaries
@allure.title("test_check_old_dict")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("https://task.imot.io/browse/DEV-1784   check old dict from ecotelecom")
def test_check_old_dict(base_url, page: Page) -> None:

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with ECOTELECOM"):
        auth(ECOTELECOM, ECOPASS, page)

    with allure.step("Go to dicts"):
        go_to_dicts(page)
        page.wait_for_selector('[href*="/tags?group"]')

    with allure.step("Click to first dict"):
        page.locator('[data-testid="test"]').first.click()
        page.wait_for_selector(NAZVANIE_SLOVARYA)

    with allure.step("Check that dict opened"):
        expect(page.locator(INPUT_SPISOK_SLOV)).to_be_visible(timeout=wait_until_visible)


@pytest.mark.independent
@pytest.mark.dictionaries
@allure.title("test_search_dict")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_search_dict")
def test_search_dict(base_url, page: Page) -> None:

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with ECOTELECOM"):
        auth(ECOTELECOM, ECOPASS, page)

    with allure.step("Go to dicts"):
        go_to_dicts(page)

    with allure.step("Search (should not depend on register)"):
        page.locator(INPUT_POISK).nth(1).fill("seat")
        #page.locator("form").get_by_role("button").click()

    with allure.step("Check that found"):
        expect(page.get_by_text("Seat")).to_have_count(1, timeout=wait_until_visible)


@pytest.mark.independent
@pytest.mark.dictionaries
@allure.title("test_import_dict_disabled_for_user")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_import_dict_disabled_for_user")
def test_import_dict_disabled_for_user(base_url, page: Page) -> None:

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with user"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to dicts"):
        go_to_dicts(page)

    with allure.step("Check"):
        expect(page.locator(BUTTON_IMPORTIROVAT_SLOVARI)).not_to_be_visible()

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.dictionaries
@allure.title("test_import_group_and_dict_by_admin")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Precondition: user  importFrom with group 11111 rule 22222 inside, with rule 33333 without group")
def test_import_group_and_dict_by_admin(base_url, page: Page) -> None:

    with allure.step("Create admin"):
        USER_ID_ADMIN, TOKEN_ADMIN, LOGIN_ADMIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with admin"):
        auth(LOGIN_ADMIN, PASSWORD, page)

    with allure.step("Go to user"):
        go_to_user(LOGIN_USER, page)

    with allure.step("Go to dicts"):
        go_to_dicts(page)

    with allure.step("Press (Import dicts) button"):
        page.locator(BUTTON_IMPORTIROVAT_SLOVARI).click()

    with allure.step("Select user ImportFrom in modal window"):
        page.locator('[class*="simpleSelect"]').locator('[role="combobox"]').fill("importFrom")
        page.wait_for_timeout(1000)
        page.get_by_text("importFrom", exact=True).click()
        page.wait_for_timeout(1000)

    with allure.step("Check that search string visible"):
        page.wait_for_selector('[data-testid="markup_dicts_importSearch}"]')

        expect(page.locator('[data-testid="markup_importNav_tags"]')).not_to_be_visible()
        expect(page.locator('[data-testid="markup_importNav_dicts"]')).not_to_be_visible()
        expect(page.locator('[data-testid="markup_dicts_importSearch}"]')).to_be_visible()
        expect(page.locator('[data-testid="markup_importNav_gpt"]')).not_to_be_visible()

    with allure.step("Import dict and group with dict"):
        page.wait_for_timeout(1000)
        #page.locator("(//input[@type='checkbox'])[3]").click()
        page.locator('[class*="CopyMode_copyModeView__popup_"]').locator('[type="checkbox"]').nth(1).click()
        page.get_by_role("button", name="Продолжить").click()
        page.wait_for_timeout(1000)
        page.locator('[class*="CopyMode_copyModeView__popup_"]').locator('[type="checkbox"]').nth(3).click()
        #page.locator("(//input[@type='checkbox'])[6]").click()
        page.wait_for_timeout(1000)
        page.get_by_role("button", name="К новым словарям").click()
        page.wait_for_timeout(2000)

    with allure.step("Check that import successful"):
        expect(page.locator("//p[normalize-space()='44444']")).to_be_visible(timeout=wait_until_visible)
        #expect(page.get_by_text("44444")).to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("55555")).to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("66666")).to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("Неотсортированные")).to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("1 словарь")).to_have_count(count=2, timeout=wait_until_visible)

    with allure.step("Delete imported dicts and groups"):
        page.get_by_text("55555").click()
        page.locator('[width="30"]').click()
        page.get_by_role("button", name="Удалить").click()
        page.locator(BUTTON_KORZINA).first.click()
        page.wait_for_timeout(700)
        page.get_by_text("66666").click()
        page.locator('[width="30"]').click()
        page.get_by_role("button", name="Удалить").click()
        page.locator(BUTTON_KORZINA).first.click()
        page.wait_for_timeout(700)

    with allure.step("Check that deleted"):
        expect(page.locator("//p[normalize-space()='44444']")).not_to_be_visible(timeout=wait_until_visible)
        #expect(page.get_by_text("44444")).not_to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("55555")).not_to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("66666")).not_to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("Неотсортированные")).not_to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN_ADMIN, USER_ID_ADMIN)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)


@pytest.mark.independent
@pytest.mark.dictionaries
@allure.title("test_import_group_and_dict_by_manager")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Precondition: user  importFrom with group 11111 rule 22222 inside, with rule 33333 without group")
def test_import_group_and_dict_by_manager(base_url, page: Page) -> None:

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Create manager"):
        USER_ID_MANAGER, TOKEN_MANAGER, LOGIN_MANAGER = create_user(API_URL, ROLE_MANAGER, PASSWORD)

    with allure.step("give user to manager"):
        give_user_to_manager(API_URL, USER_ID_MANAGER, USER_ID_USER, TOKEN_MANAGER)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with manager"):
        auth(LOGIN_MANAGER, PASSWORD, page)

    with allure.step("Go to user"):
        go_to_user(LOGIN_USER, page)

    with allure.step("Go to dicts"):
        go_to_dicts(page)

    with allure.step("Press (Import dicts) button"):
        page.locator(BUTTON_IMPORTIROVAT_SLOVARI).click()

    with allure.step("Select user ImportFrom in modal window"):
        page.locator('[class*="simpleSelect"]').locator('[role="combobox"]').fill("importFrom")
        page.wait_for_timeout(1000)
        page.get_by_text("importFrom", exact=True).click()
        page.wait_for_timeout(1000)

    with allure.step("Check that search string visible"):
        page.wait_for_selector('[data-testid="markup_dicts_importSearch}"]')

        expect(page.locator('[data-testid="markup_importNav_tags"]')).not_to_be_visible()
        expect(page.locator('[data-testid="markup_importNav_dicts"]')).not_to_be_visible()
        expect(page.locator('[data-testid="markup_dicts_importSearch}"]')).to_be_visible()
        expect(page.locator('[data-testid="markup_importNav_gpt"]')).not_to_be_visible()

    with allure.step("Import dict and group with dict"):
        page.locator('[class*="CopyMode_copyModeView__popup_"]').locator('[type="checkbox"]').nth(1).click()
        page.wait_for_timeout(1000)
        page.get_by_role("button", name="Продолжить").click()
        page.wait_for_timeout(1000)
        page.locator('[class*="CopyMode_copyModeView__popup_"]').locator('[type="checkbox"]').nth(3).click()
        page.wait_for_timeout(1000)
        page.get_by_role("button", name="К новым словарям").click()
        page.wait_for_timeout(2000)

    with allure.step("Check that import successful"):
        expect(page.locator("//p[normalize-space()='44444']")).to_be_visible(timeout=wait_until_visible)
        #expect(page.get_by_text("44444")).to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("55555")).to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("66666")).to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("Неотсортированные")).to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("1 словарь")).to_have_count(count=2, timeout=wait_until_visible)

    with allure.step("Delete imported dicts and groups"):
        page.get_by_text("55555").click()
        page.locator('[width="30"]').click()
        page.get_by_role("button", name="Удалить").click()
        page.locator(BUTTON_KORZINA).first.click()
        page.wait_for_timeout(700)
        page.get_by_text("66666").click()
        page.locator('[width="30"]').click()
        page.get_by_role("button", name="Удалить").click()
        page.locator(BUTTON_KORZINA).first.click()
        page.wait_for_timeout(700)

    with allure.step("Check that deleted"):
        expect(page.locator("//p[normalize-space()='44444']")).not_to_be_visible(timeout=wait_until_visible)
        #expect(page.get_by_text("44444")).not_to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("55555")).not_to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("66666")).not_to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("Неотсортированные")).not_to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete manager"):
        delete_user(API_URL, TOKEN_MANAGER, USER_ID_MANAGER)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)


@pytest.mark.independent
@pytest.mark.dictionaries
@allure.title("test_compare_dicts_by_user")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("User has two dicts with different parameters. when he switch between them, all parameters changing")
def test_compare_dicts_by_user(base_url, page: Page) -> None:

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with user for check comparelogin"):
        auth(USER_FOR_CHECK, PASSWORD, page)

    with allure.step("Go to dicts"):
        go_to_dicts(page)

    with allure.step("Go to first rule"):
        page.get_by_text("firstdict").click()
        page.wait_for_selector(INPUT_SPISOK_SLOV)

    with allure.step("Check filters and other inside rule"):
        expect(page.locator(NAZVANIE_SLOVARYA)).to_have_value("firstdict")
        expect(page.locator(INPUT_SPISOK_SLOV)).to_have_text("few words")
        expect(page.get_by_text("Обычный словарь")).to_have_count(1)

    with allure.step("Change rule"):
        page.get_by_text("seconddict").click()
        page.wait_for_timeout(2000)

    with allure.step("Check filters and other inside rule was changed"):
        expect(page.locator(NAZVANIE_SLOVARYA)).to_have_value("seconddict")
        expect(page.locator(INPUT_SPISOK_SLOV)).to_have_text("some text")
        expect(page.get_by_text("Словарь автозамен")).to_have_count(1)
