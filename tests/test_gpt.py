from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.gpt import *
from utils.create_delete_user import create_user, delete_user, give_user_to_manager
import pytest
import allure


@pytest.mark.independent
@pytest.mark.gpt
@allure.title("test_create_rename_delete_gpt_rule_by_user")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_create_rename_delete_gpt_rule_by_user")
def test_create_rename_delete_gpt_rule_by_user(base_url, page: Page) -> None:

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to GPT"):
        go_to_gpt(page)

    with allure.step("Create GPT rule with 2 questions"):
        create_gpt_rule_with_two("GPTrule", page)

    with allure.step("add filter"):
        add_filter("По тегам", "auto_rule", page)

    with allure.step("Press (Save) button"):
        press_save_in_gpt(page)

    with allure.step("Wait for alert and check alert message"):
        page.locator(SNACKBAR).wait_for(state="visible", timeout=wait_until_visible)
        expect(page.locator(SNACKBAR)).to_contain_text("Правило сохранено")
        page.locator(SNACKBAR).wait_for(state="hidden", timeout=wait_until_visible)

    with allure.step("Check that created and have 2 questions"):
        expect(page.locator(BUTTON_GPT_SAVE)).to_be_disabled(timeout=wait_until_visible)
        expect(page.locator(BUTTON_GPT_CANCEL)).to_be_disabled(timeout=wait_until_visible)
        expect(page.get_by_text("Вопрос 2")).to_have_count(1)
        expect(page.locator('[aria-label="Remove auto_rule"]')).to_have_count(1)

    with allure.step("Turn on rule"):
        turn_on_rule(page)

    with allure.step("Delete 1 question"):
        page.get_by_role("button", name="Удалить вопрос").nth(1).click()

    with allure.step("Press (Save) button"):
        press_save_in_gpt(page)

    with allure.step("Wait for alert and check alert message"):
        page.locator(SNACKBAR).wait_for(state="visible", timeout=wait_until_visible)
        expect(page.locator(SNACKBAR)).to_contain_text("Правило сохранено")
        page.locator(SNACKBAR).wait_for(state="hidden", timeout=wait_until_visible)

    with allure.step("Check that question deleted"):
        expect(page.locator('[tabindex="-1"]')).to_have_count(3)  # check that buttons save and cancel disabled
        expect(page.get_by_text("Вопрос 2")).to_have_count(0)

    with allure.step("Rename GPT rule"):
        page.locator(BUTTON_PENCIL).click()
        page.locator('[class*="styles_dpBothBox"]').locator('[value="GPTrule"]').fill("ruleGPT")
        page.locator(BUTTON_SAVE_EDITED_NAME).get_by_role("button").first.click()

    with allure.step("Check that GPT rule was renamed"):
        expect(page.get_by_text("ruleGPT")).to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete rule"):
        delete_rule(page)

    with allure.step("Wait for alert and check alert message"):
        page.locator(SNACKBAR).wait_for(state="visible", timeout=wait_until_visible)
        expect(page.locator(SNACKBAR)).to_contain_text("Правило GPT удалено")
        page.locator(SNACKBAR).wait_for(state="hidden", timeout=wait_until_visible)

    with allure.step("Check that rule was deleted"):
        expect(page.get_by_text("ruleGPT")).not_to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.gpt
@allure.title("test_additional_params_gpt_rule_by_user")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_additional_params_gpt_rule_by_user")
def test_additional_params_gpt_rule_by_user(base_url, page: Page) -> None:

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to GPT"):
        go_to_gpt(page)

    with allure.step("Create GPT rule with one question"):
        create_gpt_rule_with_one("addParams", page)

    with allure.step("Press (Save) button"):
        press_save_in_gpt(page)

    with allure.step("Wait for alert and check alert message"):
        page.locator(SNACKBAR).wait_for(state="visible", timeout=wait_until_visible)
        expect(page.locator(SNACKBAR)).to_contain_text("Правило сохранено")
        page.locator(SNACKBAR).wait_for(state="hidden", timeout=wait_until_visible)

    with allure.step("Check that saved"):
        expect(page.locator(BUTTON_GPT_SAVE)).to_be_disabled()
        expect(page.locator(BUTTON_GPT_CANCEL)).to_be_disabled()

    with allure.step("Press (Add settings)"):
        press_add_settings(page)

    with allure.step("Click all parameters"):
        page.locator(MENU).locator('[class="customStyles_option__raDTJ"]').nth(0).click()
        page.locator(MENU).locator('[class="customStyles_option__raDTJ"]').nth(1).click()
        page.locator(MENU).locator('[class="customStyles_option__raDTJ"]').nth(2).click()
        page.locator(MENU).locator('[class="customStyles_option__raDTJ"]').nth(3).click()
        page.locator(MENU).locator('[class="customStyles_option__raDTJ"]').nth(4).click()
        # tupo click
        page.locator('[value="gpt"]').click()
        page.wait_for_timeout(500)

    with allure.step("Check that all parameters visible"):
        expect(page.get_by_text("Движок")).to_have_count(1)
        expect(page.get_by_text("Модель")).to_have_count(1)
        expect(page.get_by_text("Температура")).to_have_count(1)
        expect(page.get_by_text("Вспомогательный текст")).to_have_count(1)
        expect(page.get_by_text("Frequency Penalty")).to_have_count(1)
        expect(page.get_by_text("Presence Penalty")).to_have_count(1)

    with allure.step("Change to yandex and add parameters for yandex"):
        page.wait_for_timeout(1000)
        page.locator('[name="yandex_gpt"]').click()
        page.wait_for_timeout(500)
        page.get_by_role("button", name="Добавить настройки").click()
        page.wait_for_timeout(500)
        page.locator(MENU).locator('[class="customStyles_option__raDTJ"]').nth(1).click()
        page.locator(MENU).locator('[class="customStyles_option__raDTJ"]').nth(2).click()
        page.locator('[placeholder="..."]').fill("SomeText")
        # tupo click
        page.locator('[value="gpt"]').click()
        page.wait_for_timeout(500)

    with allure.step("Press (Save) button"):
        press_save_in_gpt(page)

    with allure.step("Wait for alert and check alert message"):
        page.locator(SNACKBAR).wait_for(state="visible", timeout=wait_until_visible)
        expect(page.locator(SNACKBAR)).to_contain_text("Правило сохранено")
        page.locator(SNACKBAR).wait_for(state="hidden", timeout=wait_until_visible)

    with allure.step("Turn on rule"):
        turn_on_rule(page)
        # tupo click
        page.locator('[value="gpt"]').click()
        page.wait_for_timeout(500)

    with allure.step("Delete rule"):
        delete_rule(page)

    with allure.step("Wait for alert and check alert message"):
        page.locator(SNACKBAR).wait_for(state="visible", timeout=wait_until_visible)
        expect(page.locator(SNACKBAR)).to_contain_text("Правило GPT удалено")
        page.locator(SNACKBAR).wait_for(state="hidden", timeout=wait_until_visible)

    with allure.step("Check deleted"):
        expect(page.locator('[class*="styles_dpBothBox_"]').get_by_text("addParams")).not_to_be_visible()

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.gpt
@allure.title("test_import_gpt_rule_by_admin")
@allure.severity(allure.severity_level.CRITICAL)
def test_import_gpt_rule_by_admin(base_url, page: Page) -> None:

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

    with allure.step("Go to gpt"):
        go_to_gpt(page)

    with allure.step("Press import button"):
        page.locator(BUTTON_IMPORT_GPT).click()
        page.wait_for_selector('[data-testid="closePopupButton"]')

    with allure.step("Fill user for import"):
        page.locator('[class*="CustomSelect_simpleSelect"]').locator('[type="text"]').fill("importFrom")

        page.wait_for_timeout(1000)
        page.get_by_text("importFrom", exact=True).click()
        page.wait_for_timeout(1000)
        page.wait_for_selector('[data-testid="markup_gpt_importSearch}"]')

    with allure.step("Import first"):
        page.locator('[data-testid="test"]').nth(0).locator('[type="checkbox"]').check()

    with allure.step("Press (Go on)"):
        page.wait_for_timeout(1000)
        page.get_by_role("button", name="Продолжить").click()

    with allure.step("Import second"):
        page.locator('[data-testid="test"]').nth(1).locator('[type="checkbox"]').check()

    with allure.step("Go to new gpt rules"):
        page.get_by_role("button", name="К новым правилам GPT").click()
        page.wait_for_timeout(1800)

    with allure.step("Check that gpt rules imported"):
        expect(page.get_by_text("12345")).to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("98765")).to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete first gpt rule"):
        delete_rule(page)

    with allure.step("Wait for alert and check alert message"):
        page.locator(SNACKBAR).wait_for(state="visible", timeout=wait_until_visible)
        expect(page.locator(SNACKBAR)).to_contain_text("Правило GPT удалено")
        page.locator(SNACKBAR).wait_for(state="hidden", timeout=wait_until_visible)

    with allure.step("Check that deleted"):
        expect(page.get_by_text("12345")).not_to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete second gpt rule"):
        delete_rule(page)

    with allure.step("Wait for alert and check alert message"):
        page.locator(SNACKBAR).wait_for(state="visible", timeout=wait_until_visible)
        expect(page.locator(SNACKBAR)).to_contain_text("Правило GPT удалено")
        page.locator(SNACKBAR).wait_for(state="hidden", timeout=wait_until_visible)

    with allure.step("Check that deleted"):
        expect(page.get_by_text("98765")).not_to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN_ADMIN, USER_ID_ADMIN)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)


@pytest.mark.independent
@pytest.mark.gpt
@allure.title("test_import_gpt_rule_by_manager")
@allure.severity(allure.severity_level.CRITICAL)
def test_import_gpt_rule_by_manager(base_url, page: Page) -> None:

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

    with allure.step("Go to gpt"):
        go_to_gpt(page)

    with allure.step("Press import button"):
        page.locator(BUTTON_IMPORT_GPT).click()
        page.wait_for_selector('[data-testid="closePopupButton"]')

    with allure.step("Fill user for import"):
        page.locator('[class*="CustomSelect_simpleSelect"]').locator('[type="text"]').fill("importFrom")

        page.wait_for_timeout(1000)
        page.get_by_text("importFrom", exact=True).click()
        page.wait_for_timeout(1000)
        page.wait_for_selector('[data-testid="markup_gpt_importSearch}"]')

    with allure.step("Import first"):
        page.locator('[data-testid="test"]').nth(0).locator('[type="checkbox"]').check()

    with allure.step("Press (Go on)"):
        page.wait_for_timeout(1000)
        page.get_by_role("button", name="Продолжить").click()

    with allure.step("Import second"):
        page.locator('[data-testid="test"]').nth(1).locator('[type="checkbox"]').check()

    with allure.step("Go to new gpt rules"):
        page.get_by_role("button", name="К новым правилам GPT").click()
        page.wait_for_timeout(2000)

    with allure.step("Check that gpt rules imported"):
        expect(page.get_by_text("12345")).to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("98765")).to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete first gpt rule"):
        delete_rule(page)

    with allure.step("Wait for alert and check alert message"):
        page.locator(SNACKBAR).wait_for(state="visible", timeout=wait_until_visible)
        expect(page.locator(SNACKBAR)).to_contain_text("Правило GPT удалено")
        page.locator(SNACKBAR).wait_for(state="hidden", timeout=wait_until_visible)

    with allure.step("Check that deleted"):
        expect(page.get_by_text("12345")).not_to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete second gpt rule"):
        delete_rule(page)

    with allure.step("Wait for alert and check alert message"):
        page.locator(SNACKBAR).wait_for(state="visible", timeout=wait_until_visible)
        expect(page.locator(SNACKBAR)).to_contain_text("Правило GPT удалено")
        page.locator(SNACKBAR).wait_for(state="hidden", timeout=wait_until_visible)

    with allure.step("Check that deleted"):
        expect(page.get_by_text("98765")).not_to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete manager"):
        delete_user(API_URL, TOKEN_MANAGER, USER_ID_MANAGER)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)


@pytest.mark.independent
@pytest.mark.gpt
@allure.title("test_import_gpt_rules_disabled_for_user")
@allure.severity(allure.severity_level.NORMAL)
def test_import_gpt_rules_disabled_for_user(base_url, page: Page) -> None:

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth"):
        auth(LOGIN_USER, PASSWORD, page)

    with allure.step("Go to gpt"):
        go_to_gpt(page)

    with allure.step("Check that for user gpt rules import disabled"):
        expect(page.locator('[data-testid="markup_importDicts"]')).not_to_be_visible()

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)


@pytest.mark.independent
@pytest.mark.gpt
@allure.title("test_check_old_gpt_rule")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Check first old gpt rule for ecotelecom")
def test_check_old_gpt_rule(base_url, page: Page) -> None:

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth to ecotelecom"):
        auth(ECOTELECOM, ECOPASS, page)

    with allure.step("Go to GPT"):
        page.wait_for_selector(BUTTON_RAZMETKA)
        page.locator(BUTTON_RAZMETKA).click()
        page.wait_for_selector(BUTTON_GPT)
        page.locator(BUTTON_GPT).click()
        page.wait_for_selector(INPUT_GPT_RULE_NAME)
        page.wait_for_timeout(3000)

    with allure.step("Check that rule opened"):

        expect(page.locator(INPUT_GPT_RULE_NAME)).to_be_visible()
        expect(page.get_by_text("Вопрос 1")).to_have_count(1)
        #expect(page.locator(INPUT_GPT_TEG_NAME)).to_be_visible()
        #expect(page.locator(INPUT_GPT_QUESTION)).to_be_visible()


@pytest.mark.independent
@pytest.mark.gpt
@allure.title("test_compare_gpt_rules_by_user")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("User has two gpt rules with different parameters. when he switch between them, all parameters changing")
def test_compare_gpt_rules_by_user(base_url, page: Page) -> None:

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with user for check comparelogin"):
        auth(USER_FOR_CHECK, PASSWORD, page)

    with allure.step("Go to GPT"):
        page.wait_for_selector(BUTTON_RAZMETKA, timeout=wait_until_visible)
        page.locator(BUTTON_RAZMETKA).click()
        page.wait_for_selector(BUTTON_GPT, timeout=wait_until_visible)
        page.locator(BUTTON_GPT).click()
        page.wait_for_selector(INPUT_GPT_RULE_NAME, timeout=wait_until_visible)
        page.wait_for_timeout(3000)

    with allure.step("Check parameters"):
        expect(page.locator(INPUT_GPT_RULE_NAME)).to_have_value("firstgptrule")
        expect(page.locator('[class*="styles_entityType"]')).to_have_text("Тип правилаКоммуникация")
        expect(page.locator('[aria-label="Remove firstrule"]')).to_have_count(1, timeout=wait_until_visible)
        expect(page.locator(INPUT_GPT_TEG_NAME).nth(0)).to_have_value("firsttag")
        expect(page.locator(INPUT_GPT_QUESTION).nth(0)).to_have_value("firstquestion")
        expect(page.locator(INPUT_GPT_TEG_NAME).nth(1)).to_have_value("secondtag")
        expect(page.locator(INPUT_GPT_QUESTION).nth(1)).to_have_value("secondquestion")

    with allure.step("Change gpt rule"):
        page.get_by_text("secondgptrule").click()
        page.wait_for_timeout(3000)

    with allure.step("Check that parameters changed"):
        expect(page.locator(INPUT_GPT_RULE_NAME)).to_have_value("secondgptrule")
        expect(page.locator('[class*="styles_entityType"]')).to_have_text("Тип правилаСделка")
        expect(page.locator('[aria-label="Remove >100"]')).to_have_count(1)
        expect(page.locator(INPUT_GPT_TEG_NAME).nth(0)).to_have_value("sadecesoru")
        expect(page.locator(INPUT_GPT_QUESTION).nth(0)).to_have_value("nasilsin")

    with allure.step("Check all checkboxes to be checked (include on/off rules)"):
        all_checkboxes_to_be_checked(page)

        assert all_checkboxes_to_be_checked(page) == True

