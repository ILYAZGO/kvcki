from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
import pytest
from utils.create_delete_user import create_user, delete_user


@pytest.mark.independent
@pytest.mark.adminbar
def test_example(page: Page) -> None:

    #  create user
    USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    page.goto(URL, timeout=timeout)

    auth(LOGIN_USER, PASSWORD, page)

    page.wait_for_selector('[class*="Hint_question__title"]', timeout=wait_until_visible)
    page.locator('[class*="styles_langHandler"]').get_by_role("button", name="RU").click()
    page.wait_for_timeout(300)
    page.get_by_role("option", name="EN").click()
    page.wait_for_selector('[class*="Hint_question__title"]', timeout=wait_until_visible)

    expect(page.get_by_text("Additional parameters")).to_be_visible(timeout=wait_until_visible)


    page.locator('[class*="styles_langHandler"]').get_by_role("button", name="EN").click()
    page.wait_for_timeout(300)
    page.get_by_role("option", name="ES").click()
    page.wait_for_selector('[class*="Hint_question__title"]', timeout=wait_until_visible)

    expect(page.get_by_text("Parámetros adicionales")).to_be_visible(timeout=wait_until_visible)


    page.locator('[class*="styles_langHandler"]').get_by_role("button", name="ES").click()
    page.wait_for_timeout(300)
    page.get_by_role("option", name="PT").click()
    page.wait_for_selector('[class*="Hint_question__title"]', timeout=wait_until_visible)

    expect(page.get_by_text("Parâmetros adicionais")).to_be_visible(timeout=wait_until_visible)

    page.locator('[class*="styles_langHandler"]').get_by_role("button", name="PT").click()
    page.wait_for_timeout(300)
    page.get_by_role("option", name="RU").click()
    page.wait_for_selector('[class*="Hint_question__title"]', timeout=wait_until_visible)

    expect(page.get_by_text("Дополнительные параметры")).to_be_visible(timeout=wait_until_visible)

    #  delete user
    delete_user(API_URL, TOKEN_USER, USER_ID_USER)