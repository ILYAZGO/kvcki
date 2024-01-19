from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.users import *
from utils.create_delete_user import create_user, delete_user
import pytest


@pytest.mark.users
def test_example(page: Page) -> None:
    USER_ID, BEARER, ACCESS_TOKEN, LOGIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    page.goto(URL, timeout=timeout)
    '''login'''
    auth(LOGIN, PASSWORD, page)

    go_to_users(page)

    set_user(NEW_NAME,
             NEW_LOGIN,
             PASSWORD,
             EMAIL,
             "someComment",
             "Интегратор",
             page)

    '''press dobavit'''
    page.locator(BUTTON_DOBAVIT).click()

    '''check'''
    page.wait_for_selector(INPUT_NAME)
    expect(page.locator(INPUT_LOGIN)).to_have_value(NEW_LOGIN, timeout=wait_until_visible)
    expect(page.locator(INPUT_NAME)).to_have_value(NEW_NAME, timeout=wait_until_visible)
    expect(page.locator(INPUT_EMAIL)).to_have_value(EMAIL, timeout=wait_until_visible)
    page.wait_for_timeout(1500)
    expect(page.get_by_text("Интегратор")).to_have_count(2, timeout=wait_until_visible)  #slovalos potomu 4to noviy punkt menu
    page.wait_for_timeout(3000)

    delete_added_user(page)

    expect(page.locator(INPUT_LOGIN)).to_have_value(LOGIN, timeout=wait_until_visible)

    delete_user(API_URL, USER_ID, BEARER, ACCESS_TOKEN)