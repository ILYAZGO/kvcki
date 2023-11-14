from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.markup import *
from utils.create_delete_user import create_user, delete_user
import pytest


@pytest.mark.dictionaries
def test_example(page: Page) -> None:
    USER_ID, BEARER, ACCESS_TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    page.goto(URL, timeout=timeout)

    auth(LOGIN, PASSWORD, page)

    go_to_dicts(page)

    create_dict("77777", page)

    '''check created dict outside group'''
    expect(page.locator(NAZVANIE_SLOVARYA)).to_have_value("77777", timeout=wait_until_visible)

    page.reload()

    expect(page.get_by_text("Неотсортированные")).to_have_count(count=2, timeout=wait_until_visible)  # проверяем что таких надписей две (слева и внутри словаря)

    delete_group_and_rule_or_dict(page)

    expect(page.get_by_text("Неотсортированные")).not_to_be_visible(timeout=wait_until_visible)

    delete_user(API_URL, USER_ID, BEARER, ACCESS_TOKEN)
