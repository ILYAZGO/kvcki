from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.markup import *
from utils.create_delete_user import create_user, delete_user
import pytest

@pytest.mark.gpt
def test_example(page: Page) -> None:
    USER_ID, BEARER, ACCESS_TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    page.goto(URL, timeout=timeout)
    '''login'''
    auth(LOGIN, PASSWORD, page)

    go_to_gpt(page)

    page.locator(BUTTON_GPT_CREATE_RULE).click()
    page.locator(INPUT_GPT_RULE_NAME).fill("GPTrule")
    page.locator(INPUT_GPT_TEG_NAME).fill("GPTteg1")
    page.locator(INPUT_GPT_QUESTION).fill("GPTquestion1")
    page.get_by_role("button", name="Добавить вопрос").click()
    page.locator(INPUT_GPT_TEG_NAME).nth(1).fill("GPTteg2")
    page.locator(INPUT_GPT_QUESTION).nth(1).fill("GPTquestion2")

    page.locator(BUTTON_GPT_SAVE).click()

    expect(page.locator('[tabindex="-1"]')).to_have_count(3)  # check that buttons save and cancel disabled
    expect(page.get_by_text("Вопрос 2")).to_have_count(1)

    page.locator('[aria-label="Вкл/Выкл"]').locator('[type="checkbox"]').click()  # turn on the rule
    page.wait_for_timeout(1500)

    page.get_by_role("button", name="Удалить вопрос").nth(1).click()

    page.locator(BUTTON_GPT_SAVE).click()

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