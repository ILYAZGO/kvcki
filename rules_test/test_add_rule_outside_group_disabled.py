from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.markup import *
from utils.create_delete_user import create_user, delete_user
import pytest

'''Create rule outside group should be disabled'''


@pytest.mark.rules
def test_example(page: Page) -> None:
    USER_ID, BEARER, ACCESS_TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    page.goto(URL, timeout=timeout)
    '''login'''
    auth(LOGIN, PASSWORD, page)

    go_to_markup(page)

    '''check'''
    expect(page.locator('[aria-label="Чтобы добвить тег, выберите или добавьте группу."]')).to_be_visible()

    delete_user(API_URL, USER_ID, BEARER, ACCESS_TOKEN)
