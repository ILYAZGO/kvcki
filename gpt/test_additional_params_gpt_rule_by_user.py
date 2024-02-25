from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.markup import *
from utils.create_delete_user import create_user, delete_user
import pytest


@pytest.mark.independent
@pytest.mark.gpt
def test_example(page: Page) -> None:
    USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    page.goto(URL, timeout=timeout)
    '''login'''
    auth(LOGIN, PASSWORD, page)

    go_to_gpt(page)

    create_gpt_rule_with_one("addParams", page)

    expect(page.locator('[tabindex="-1"]')).to_have_count(3)  # check that buttons save and cancel disabled

    # add params
    page.get_by_role("button", name="Добавить настройки").click()
    page.wait_for_timeout(500)

    page.locator('[class=" css-woue3h-menu"]').locator('[class="customStyles_option__raDTJ"]').nth(0).click()
    page.locator('[class=" css-woue3h-menu"]').locator('[class="customStyles_option__raDTJ"]').nth(1).click()
    page.locator('[class=" css-woue3h-menu"]').locator('[class="customStyles_option__raDTJ"]').nth(2).click()
    page.locator('[class=" css-woue3h-menu"]').locator('[class="customStyles_option__raDTJ"]').nth(3).click()
    page.locator('[class=" css-woue3h-menu"]').locator('[class="customStyles_option__raDTJ"]').nth(4).click()

    # tupo click
    page.locator('[class="styles_title__s3M9y undefined"]').nth(0).click()
    page.wait_for_timeout(500)

    expect(page.get_by_text("Движок")).to_have_count(1)
    expect(page.get_by_text("Модель")).to_have_count(1)
    expect(page.get_by_text("Температура")).to_have_count(1)
    expect(page.get_by_text("Вспомогательный текст")).to_have_count(1)
    expect(page.get_by_text("Frequency Penalty")).to_have_count(1)
    expect(page.get_by_text("Presence Penalty")).to_have_count(1)

    # work with params
    page.locator('[name="yandex_gpt_v1"]').click()
    #page.locator('[name="general"]').click()
    page.locator('[placeholder="..."]').fill("SomeText")


    page.locator(BUTTON_GPT_SAVE).click()
    page.wait_for_timeout(1000)

    turn_on_rule(page)

    # tupo click
    page.locator('[class="styles_title__s3M9y undefined"]').nth(0).click()
    page.wait_for_timeout(1000)
    page.locator(BUTTON_KORZINA).click()
    page.wait_for_timeout(1000)


    delete_user(API_URL, TOKEN, USER_ID)