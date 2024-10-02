from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.check_lists import *
from utils.create_delete_user import create_user, delete_user, give_user_to_manager, create_operator
import pytest
import allure


@pytest.mark.independent
@pytest.mark.check_list
@allure.title("test_create_rename_update_delete_check_list")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("create,rename, update,delete check-list")
def test_create_update_delete_check_list(base_url, page: Page) -> None:

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to check-lists"):
        go_to_check_list(page)

    with allure.step("Create check-list with 2 questions and 2 answers"):
        create_check_list_with_questions_and_answers("12345", "Question1", "Question2", page)

    with allure.step("Fill filter"):
        add_filter("По тегам", "auto_rule", page)

    with allure.step("Change sort order"):
        expect(page.locator(INPUT_SORT_ORDER)).to_have_value("0")
        page.locator(INPUT_SORT_ORDER).clear()
        page.locator(INPUT_SORT_ORDER).fill("1000")

    with allure.step("Press button (Save)"):
        page.wait_for_selector('[data-testid="filters_search_by_tags"]', timeout=wait_until_visible)
        press_button_save(page)

    with allure.step("Check created"):
        expect(page.get_by_text("12345")).to_be_visible(timeout=wait_until_visible)
        expect(page.locator('[aria-label="Remove auto_rule"]')).to_have_count(1)
        expect(page.locator(INPUT_SORT_ORDER)).to_have_value("1000")

        #  added block with renaming from other test

    with allure.step("Change title"):
        page.get_by_text("12345").click()
        page.locator(INPUT_CHECK_LIST_NAME).clear()
        page.locator(INPUT_CHECK_LIST_NAME).fill("654321")
        page.wait_for_timeout(500)

    with allure.step("Press button (Save)"):
        page.wait_for_selector('[data-testid="filters_search_by_tags"]', timeout=wait_until_visible)
        press_button_save(page)

    with allure.step("Check that title changed"):
        expect(page.locator(INPUT_CHECK_LIST_NAME)).to_have_value("654321")

    with allure.step("Rename from left list (Pencil)"):
        page.wait_for_selector(BUTTON_PENCIL)
        page.locator(BUTTON_PENCIL).click()
        page.wait_for_timeout(1000)
        page.locator('[class*="styles_titleBlock"]').locator(INPUT_LEFT_CHECK_LIST_NAME).clear()
        page.locator('[class*="styles_titleBlock"]').locator(INPUT_LEFT_CHECK_LIST_NAME).fill("98765")
        page.wait_for_timeout(300)
        page.locator(BUTTON_SAVE_EDITED_NAME).click()
        page.wait_for_timeout(300)

    with allure.step("Check rename was successful"):
        expect(page.get_by_text("98765")).to_be_visible(timeout=wait_until_visible)

        #

    with allure.step("Update check-list (change first question)"):
        page.get_by_text("98765").click()
        page.locator(INPUT_FIRST_QUESTION).clear()
        page.locator(INPUT_FIRST_QUESTION).fill("654321")
        page.wait_for_timeout(500)

    with allure.step("Uncheck autogerenate report checkbox"):
        page.locator('[id="checklistGenerateReport"]').click()

    with allure.step("Press button (Save)"):
        page.wait_for_selector('[data-testid="filters_search_by_tags"]', timeout=wait_until_visible)
        press_button_save(page)

    with allure.step("Reload page and check that update saved"):
        page.reload()
        page.wait_for_selector(INPUT_FIRST_QUESTION)
        expect(page.locator(INPUT_FIRST_QUESTION)).to_have_value("654321")
        expect(page.locator(CHECK_BOX_AUTOGENEREATE_REPORT)).not_to_be_checked()
        expect(page.locator('[aria-label="Remove auto_rule"]')).to_have_count(1)

    with allure.step("Create appriser"):
        create_appriser("Appriser", "5", page)

    with allure.step("Check autogerenate report checkbox"):
        page.locator(CHECK_BOX_AUTOGENEREATE_REPORT).click()

    with allure.step("Press button (Save)"):
        page.wait_for_selector('[data-testid="filters_search_by_tags"]', timeout=wait_until_visible)
        press_button_save(page)

    with allure.step("Check that appriser created"):
        page.reload()
        page.wait_for_selector('[name="appraisers.0.title"]')
        expect(page.locator('[name="appraisers.0.title"]')).to_have_value("Appriser")
        expect(page.locator(CHECK_BOX_AUTOGENEREATE_REPORT)).to_be_checked()

    with allure.step("Delete appriser"):
        delete_appriser(page)

    with allure.step("Press button (Save)"):
        page.wait_for_selector('[data-testid="filters_search_by_tags"]', timeout=wait_until_visible)
        press_button_save(page)

    with allure.step("Check that appriser deleted"):
        page.reload()
        page.wait_for_selector(INPUT_CHECK_LIST_NAME, timeout=wait_until_visible)
        expect(page.locator('[name="appraisers.0.title"]')).not_to_be_visible()

    with allure.step("Delete created check-list"):
        delete_check_list(page)

    with allure.step("Wait for alert and check alert message"):
        page.wait_for_selector(ALERT, timeout=wait_until_visible)
        expect(page.locator(ALERT)).to_contain_text("Чек-лист удален")
        page.wait_for_selector(ALERT, state="hidden", timeout=wait_until_visible)

    with allure.step("Check that deleted"):
        page.wait_for_selector(NI4EGO_NE_NAYDENO, timeout=wait_until_visible)
        expect(page.locator(NI4EGO_NE_NAYDENO)).to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.check_list
@allure.title("test_check_old_check_list")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check old checklist from ecotelecom")
def test_check_old_check_list(base_url, page: Page) -> None:

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth like Ecotelecom"):
        auth(ECOTELECOM, ECOPASS, page)

    with allure.step("Go to check-lists"):
        go_to_check_list(page)

    with allure.step("Select first available check-list"):
        page.locator('[class*=groupItem]').first.click()
        page.wait_for_selector(INPUT_CHECK_LIST_NAME, timeout=wait_until_visible)

    with allure.step("Check that first available check-list have appriser (seems strange, but works)"):
        expect(page.locator('[name="appraisers.0.title"]')).to_be_visible()


@pytest.mark.independent
@pytest.mark.check_list
@allure.title("test_import_check_list_by_admin")
@allure.severity(allure.severity_level.CRITICAL)
def test_import_check_list_by_admin(base_url, page: Page) -> None:

    with allure.step("Create admin"):
        USER_ID_ADMIN, TOKEN_ADMIN, LOGIN_ADMIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth"):
        auth(LOGIN_ADMIN, PASSWORD, page)

    with allure.step("Go to user import to"):
        go_to_user(LOGIN_USER, page)

    with allure.step("Go to check-lists"):
        go_to_check_list(page)

    with allure.step("Press import button"):
        press_import_checklists(page)

    with allure.step("Fill user for import"):
        page.locator('[class*="CustomSelect_simpleSelect"]').locator('[type="text"]').type("importFrom", delay=50)
        page.locator(MENU).get_by_text("importFrom", exact=True).click()
        page.wait_for_selector(SEARCH_IN_IMPORT_MODAL, timeout=wait_until_visible)

    with allure.step("Import first"):
        page.wait_for_timeout(600)
        page.locator('[data-testid="test"]').nth(0).locator('[type="checkbox"]').check()

    with allure.step("Press (Go on)"):
        page.get_by_role("button", name="Продолжить").click()

    with allure.step("Import second"):
        page.locator('[data-testid="test"]').nth(1).locator('[type="checkbox"]').check()

    with allure.step("Go to new chec-lists"):
        page.get_by_role("button", name="К новым чек-листам").click()
        page.wait_for_timeout(1900)

    with allure.step("Check that check-lists imported"):
        expect(page.get_by_text("12345")).to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("98765")).to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete first check-list"):
        delete_check_list(page)

    with allure.step("Wait for alert and check alert message"):
        page.wait_for_selector(ALERT, timeout=wait_until_visible)
        expect(page.locator(ALERT)).to_contain_text("Чек-лист удален")
        page.wait_for_selector(ALERT, state="hidden", timeout=wait_until_visible)

    with allure.step("Check that deleted"):
        expect(page.get_by_text("12345")).not_to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete second check-list"):
        delete_check_list(page)

    with allure.step("Wait for alert and check alert message"):
        page.wait_for_selector(ALERT, timeout=wait_until_visible)
        expect(page.locator(ALERT)).to_contain_text("Чек-лист удален")
        page.wait_for_selector(ALERT, state="hidden", timeout=wait_until_visible)

    with allure.step("Check that deleted"):
        expect(page.get_by_text("98765")).not_to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN_ADMIN, USER_ID_ADMIN)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)


@pytest.mark.independent
@pytest.mark.check_list
@allure.title("test_import_check_list_by_manager")
@allure.severity(allure.severity_level.CRITICAL)
def test_import_check_list_by_manager(base_url, page: Page) -> None:

    with allure.step("Create manager"):
        USER_ID_MANAGER, TOKEN_MANAGER, LOGIN_MANAGER = create_user(API_URL, ROLE_MANAGER, PASSWORD)

    with allure.step("Create user for import"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Give user for import to manager"):
        give_user_to_manager(API_URL, USER_ID_MANAGER, USER_ID_USER, TOKEN_MANAGER)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth"):
        auth(LOGIN_MANAGER, PASSWORD, page)

    with allure.step("Go to user import to"):
        go_to_user(LOGIN_USER, page)

    with allure.step("Go to check-lists"):
        go_to_check_list(page)

    with allure.step("Press import button"):
        press_import_checklists(page)

    with allure.step("Fill user for import"):
        page.locator('[class*="CustomSelect_simpleSelect"]').locator('[type="text"]').fill("importFrom")
        page.locator(MENU).get_by_text("importFrom", exact=True).click()
        page.wait_for_selector(SEARCH_IN_IMPORT_MODAL, timeout=wait_until_visible)

    with allure.step("Import first"):
        page.locator('[data-testid="test"]').nth(0).locator('[type="checkbox"]').check()

    with allure.step("Press (Go on)"):
        page.get_by_role("button", name="Продолжить").click()

    with allure.step("Import second"):
        page.locator('[data-testid="test"]').nth(1).locator('[type="checkbox"]').check()

    with allure.step("Go to new chec-lists"):
        page.get_by_role("button", name="К новым чек-листам").click()
        page.wait_for_timeout(2000)

    with allure.step("Check that check-lists imported"):
        expect(page.get_by_text("12345")).to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("98765")).to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete first check-list"):
        delete_check_list(page)

    with allure.step("Wait for alert and check alert message"):
        page.wait_for_selector(ALERT, timeout=wait_until_visible)
        expect(page.locator(ALERT)).to_contain_text("Чек-лист удален")
        page.wait_for_selector(ALERT, state="hidden", timeout=wait_until_visible)

    with allure.step("Check that deleted"):
        expect(page.get_by_text("12345")).not_to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete second check-list"):
        delete_check_list(page)

    with allure.step("Wait for alert and check alert message"):
        page.wait_for_selector(ALERT, timeout=wait_until_visible)
        expect(page.locator(ALERT)).to_contain_text("Чек-лист удален")
        page.wait_for_selector(ALERT, state="hidden", timeout=wait_until_visible)

    with allure.step("Check that deleted"):
        expect(page.get_by_text("98765")).not_to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete manager"):
        delete_user(API_URL, TOKEN_MANAGER, USER_ID_MANAGER)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)


@pytest.mark.independent
@pytest.mark.check_list
@allure.title("test_import_check_list_disabled_for_user")
@allure.severity(allure.severity_level.NORMAL)
def test_import_check_list_disabled_for_user(base_url, page: Page) -> None:

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth"):
        auth(LOGIN_USER, PASSWORD, page)

    with allure.step("Go to check-lists"):
        go_to_check_list(page)

    with allure.step("Check that for user check-list import disabled"):
        expect(page.locator('[data-testid="markup_importDicts"]')).not_to_be_visible()

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)


@pytest.mark.independent
@pytest.mark.check_list
@allure.title("test_compare_check_lists_by_user")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("User has two check lists with different parameters. when he switch between them, all parameters changing")
def test_compare_check_lists_by_user(base_url, page: Page) -> None:

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with user for check comparelogin"):
        auth(USER_FOR_CHECK, PASSWORD, page)

    with allure.step("Go to check-lists"):
        go_to_check_list(page)

    with allure.step("Select first available check-list"):
        page.locator('[class*="styles_dpBothBox_"]').get_by_text("firstchecklist").click()
        page.wait_for_selector(INPUT_CHECK_LIST_NAME, timeout=wait_until_visible)

    with allure.step("Check parameters for first check list"):
        expect(page.locator(INPUT_CHECK_LIST_NAME)).to_have_value("firstchecklist")
        expect(page.locator('[value="CALL"]')).to_have_count(1)
        expect(page.locator('[aria-label="Remove firstrule"]')).to_have_count(1)
        expect(page.locator('[aria-label="Remove secondrule"]')).to_have_count(2)
        expect(page.locator('[name="appraisers.0.title"]')).to_have_value("mark1")
        expect(page.locator('[name="appraisers.0.points"]')).to_have_value("1")
        expect(page.locator('[name="questions.0.title"]')).to_have_value("question1")
        expect(page.locator('[name="questions.0.answers.0.answer"]')).to_have_value("answer1")
        expect(page.locator('[name="questions.0.answers.0.point"]')).to_have_value("2")

    with allure.step("Switch to second check-list"):
        page.locator('[class*="styles_dpBothBox_"]').get_by_text("secondchecklist").click()

    with allure.step("Check that parameters changed"):
        expect(page.locator(INPUT_CHECK_LIST_NAME)).to_have_value("secondchecklist")
        expect(page.locator('[value="DEAL"]')).to_have_count(1)
        expect(page.locator('[aria-label="Remove firstrule"]')).to_have_count(2)
        expect(page.locator('[aria-label="Remove >100"]')).to_have_count(1)
        expect(page.locator('[name="appraisers.0.title"]')).to_have_value("mark2")
        expect(page.locator('[name="appraisers.0.points"]')).to_have_value("7")
        expect(page.locator('[name="questions.0.title"]')).to_have_value("question2")
        expect(page.locator('[name="questions.0.answers.0.answer"]')).to_have_value("answer2")
        expect(page.locator('[name="questions.0.answers.0.point"]')).to_have_value("9")