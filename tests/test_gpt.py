from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.gpt import *
from utils.create_delete_user import create_user, delete_user
import pytest
import allure


@pytest.mark.independent
@pytest.mark.gpt
@allure.title("test_create_rename_delete_gpt_rule_by_user")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_create_rename_delete_gpt_rule_by_user")
def test_create_rename_delete_gpt_rule_by_user(page: Page) -> None:

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)

    with allure.step("Auth"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to GPT"):
        go_to_gpt(page)

    with allure.step("Create GPT rule with 2 questions"):
        create_gpt_rule_with_two("GPTrule", page)

    with allure.step("Press (Save) button"):
        press_save_in_gpt(page)

    with allure.step("Check that created and have 2 questions"):
        expect(page.locator('[tabindex="-1"]')).to_have_count(3)  # check that buttons save and cancel disabled
        expect(page.get_by_text("Вопрос 2")).to_have_count(1)

    with allure.step("Turn on rule"):
        turn_on_rule(page)

    with allure.step("Delete 1 question"):
        page.get_by_role("button", name="Удалить вопрос").nth(1).click()

    with allure.step("Press (Save) button"):
        press_save_in_gpt(page)

    with allure.step("Check that question deleted"):
        expect(page.locator('[tabindex="-1"]')).to_have_count(3)  # check that buttons save and cancel disabled
        expect(page.get_by_text("Вопрос 2")).to_have_count(0)

    with allure.step("Rename GPT rule"):
        page.locator(BUTTON_PENCIL).click()
        page.locator('[class*="styles_dpBothBox"]').locator('[value="GPTrule"]').fill("ruleGPT")
        page.locator(BUTTON_SAVE_EDITED_NAME).get_by_role("button").first.click()
        page.wait_for_timeout(1000)

    with allure.step("Check that GPT rule was renamed"):
        expect(page.get_by_text("ruleGPT")).to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete rule"):
        page.locator(BUTTON_KORZINA).click()
        page.wait_for_timeout(1000)

    with allure.step("Check that rule was deleted"):
        expect(page.get_by_text("ruleGPT")).not_to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.gpt
@allure.title("test_additional_params_gpt_rule_by_user")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_additional_params_gpt_rule_by_user")
def test_additional_params_gpt_rule_by_user(page: Page) -> None:

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)

    with allure.step("Auth"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to GPT"):
        go_to_gpt(page)

    with allure.step("Create GPT rule with one question"):
        create_gpt_rule_with_one("addParams", page)

    with allure.step("Press (Save) button"):
        press_save_in_gpt(page)
        page.wait_for_timeout(2500)

    with allure.step("Check that saved"):
        expect(page.locator('[tabindex="-1"]')).to_have_count(3)  # check that buttons save and cancel disabled

    with allure.step("Press (Add settings)"):
        page.get_by_role("button", name="Добавить настройки").click()
        page.wait_for_selector('[class=" css-woue3h-menu"]')

    with allure.step("Click all parameters"):
        page.locator('[class=" css-woue3h-menu"]').locator('[class="customStyles_option__raDTJ"]').nth(0).click()
        page.locator('[class=" css-woue3h-menu"]').locator('[class="customStyles_option__raDTJ"]').nth(1).click()
        page.locator('[class=" css-woue3h-menu"]').locator('[class="customStyles_option__raDTJ"]').nth(2).click()
        page.locator('[class=" css-woue3h-menu"]').locator('[class="customStyles_option__raDTJ"]').nth(3).click()
        page.locator('[class=" css-woue3h-menu"]').locator('[class="customStyles_option__raDTJ"]').nth(4).click()
        # tupo click
        page.locator('[value="gpt"]').click()
        page.wait_for_timeout(300)

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
        page.wait_for_timeout(400)
        page.get_by_role("button", name="Добавить настройки").click()
        page.wait_for_timeout(500)
        page.locator('[class*="-menu"]').locator('[class="customStyles_option__raDTJ"]').nth(1).click()
        page.locator('[class*="-menu"]').locator('[class="customStyles_option__raDTJ"]').nth(2).click()
        page.locator('[placeholder="..."]').fill("SomeText")
        # tupo click
        page.locator('[value="gpt"]').click()
        page.wait_for_timeout(500)

    with allure.step("Press (Save) button"):
        press_save_in_gpt(page)

    with allure.step("Turn on rule"):
        turn_on_rule(page)
        # tupo click
        page.locator('[value="gpt"]').click()
        page.wait_for_timeout(500)

    with allure.step("Delete rule"):
        page.locator(BUTTON_KORZINA).click()
        page.wait_for_timeout(1000)

    with allure.step("Check deleted"):
        expect(page.locator('[class*="styles_dpBothBox_"]').get_by_text("addParams")).not_to_be_visible()

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)