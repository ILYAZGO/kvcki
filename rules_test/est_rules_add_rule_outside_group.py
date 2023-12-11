from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.markup import *
from utils.create_delete_user import create_user, delete_user
import pytest

'''Create rule outside group'''


@pytest.mark.rules
def test_example(page: Page) -> None:
    USER_ID, BEARER, ACCESS_TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    page.goto(URL, timeout=timeout)
    '''login'''
    auth(LOGIN, PASSWORD, page)

    go_to_markup(page)

    create_rule("66666", page)

    '''check'''
    page.wait_for_selector(NAZVANIE_PRAVILA_TEGIROVANIYA)
    expect(page.locator(NAZVANIE_PRAVILA_TEGIROVANIYA)).to_have_value("66666")

    delete_group_and_rule_or_dict(page)

    '''check teardown'''
    expect(page.get_by_text("Неотсортированные")).not_to_be_visible(timeout=wait_until_visible)

    delete_user(API_URL, USER_ID, BEARER, ACCESS_TOKEN)
