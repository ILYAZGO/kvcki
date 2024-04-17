from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.check_lists import *
from utils.create_delete_user import create_user, delete_user
import pytest
import allure


@pytest.mark.independent
@pytest.mark.check_list
@allure.title("test_create_rename_delete_check_list")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_rename_delete_check_list(page: Page) -> None:

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)

    with allure.step("Auth"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to check-lists"):
        go_to_check_list(page)

    with allure.step("Create check-list with 2 questions and 2 answers"):
        create_check_list_with_questions_and_answers("12345", "Question1", "Question2", page)

    with allure.step("Press button (Save)"):
        press_button_save(page)

    with allure.step("Check created"):
        expect(page.get_by_text("12345")).to_be_visible(timeout=wait_until_visible)

    with allure.step("Change title"):
        page.get_by_text("12345").click()
        page.locator(INPUT_CHECK_LIST_NAME).clear()
        page.locator(INPUT_CHECK_LIST_NAME).fill("654321")
        page.wait_for_timeout(500)

    with allure.step("Press button (Save)"):
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

    with allure.step("Delete created check-list"):
        delete_check_list(page)

    with allure.step("Check that deleted"):
        page.wait_for_selector(NI4EGO_NE_NAYDENO)
        expect(page.locator(NI4EGO_NE_NAYDENO)).to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.check_list
@allure.title("test_create_update_delete_check_list")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_update_delete_check_list(page: Page) -> None:

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)

    with allure.step("Auth"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to check-lists"):
        go_to_check_list(page)

    with allure.step("Create check-list with 2 questions and 2 answers"):
        create_check_list_with_questions_and_answers("12345", "Question1", "Question2", page)

    with allure.step("Press button (Save)"):
        press_button_save(page)

    with allure.step("Check created"):
        expect(page.get_by_text("12345")).to_be_visible(timeout=wait_until_visible)

    with allure.step("Update check-list (change first question)"):
        page.get_by_text("12345").click()
        page.locator(INPUT_FIRST_QUESTION).clear()
        page.locator(INPUT_FIRST_QUESTION).fill("654321")

    with allure.step("Press button (Save)"):
        press_button_save(page)

    with allure.step("Reload page and check that update saved"):
        page.reload()
        page.wait_for_selector(INPUT_FIRST_QUESTION)
        expect(page.locator(INPUT_FIRST_QUESTION)).to_have_value("654321")

    with allure.step("Create appriser"):
        create_appriser("Appriser", "5", page)

    with allure.step("Press button (Save)"):
        press_button_save(page)

    with allure.step("Check that appriser created"):
        page.reload()
        page.wait_for_selector('[name="appraisers.0.title"]')
        expect(page.locator('[name="appraisers.0.title"]')).to_have_value("Appriser")

    with allure.step("Delete appriser"):
        delete_appriser(page)

    with allure.step("Press button (Save)"):
        press_button_save(page)

    with allure.step("Check that appriser deleted"):
        page.reload()
        page.wait_for_selector(INPUT_CHECK_LIST_NAME)
        expect(page.locator('[name="appraisers.0.title"]')).not_to_be_visible()

    with allure.step("Delete created check-list"):
        delete_check_list(page)

    with allure.step("Check that deleted"):
        page.wait_for_timeout(1000)
        page.wait_for_selector(NI4EGO_NE_NAYDENO, timeout=wait_until_visible)
        expect(page.locator(NI4EGO_NE_NAYDENO)).to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.check_list
@allure.title("test_check_old_check_list")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check old checklist from ecotelecom")
def test_check_old_check_list(page: Page) -> None:

    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)

    with allure.step("Auth like Ecotelecom"):
        auth(ECOTELECOM, ECOPASS, page)

    with allure.step("Go to check-lists"):
        go_to_check_list(page)

    with allure.step("Select first available check-list"):
        page.locator('[class*=groupItem]').first.click()
        page.wait_for_selector(INPUT_CHECK_LIST_NAME)

    with allure.step("Check that first available check-list have appriser (seems strange, but works)"):
        expect(page.locator('[name="appraisers.0.title"]')).to_be_visible()