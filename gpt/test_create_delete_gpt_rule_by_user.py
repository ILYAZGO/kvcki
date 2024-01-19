from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.markup import *
from utils.create_delete_user import create_user, delete_user
import pytest

@pytest.mark.gpt
def test_example(page: Page) -> None:
    USER_ID, BEARER, ACCESS_TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    page.goto("http://192.168.10.101/feature-dev-1674", timeout=timeout)

    auth(LOGIN, PASSWORD, page)

    go_to_gpt(page)

    create_gpt_rule_with_two("GPTrule", page)

    expect(page.locator('[tabindex="-1"]')).to_have_count(3)  # check that buttons save and cancel disabled
    expect(page.get_by_text("Вопрос 2")).to_have_count(1)

    turn_on_rule(page)

    page.get_by_role("button", name="Удалить вопрос").nth(1).click()
    page.locator(BUTTON_GPT_SAVE).click(force=True)

    expect(page.locator('[tabindex="-1"]')).to_have_count(3)  # check that buttons save and cancel disabled
    expect(page.get_by_text("Вопрос 2")).to_have_count(0)

    page.locator(BUTTON_PENCIL).click()
    page.locator('[class*="styles_dpBothBox"]').locator('[value="GPTrule"]').fill("ruleGPT")
    page.locator(BUTTON_SAVE_EDITED_NAME).get_by_role("button").first.click()
    page.wait_for_timeout(1000)

    expect(page.get_by_text("ruleGPT")).to_be_visible(timeout=wait_until_visible)

    page.locator(BUTTON_KORZINA).click()
    page.wait_for_timeout(1000)

    expect(page.get_by_text("ruleGPT")).not_to_be_visible(timeout=wait_until_visible)

    delete_user(API_URL, USER_ID, BEARER, ACCESS_TOKEN)