from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
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

    set_user("newManager",
             "1createManagerByAdmin",
             PASSWORD,
             "mail@mail.com",
             "someComment",
             "Интегратор",
             page)

    '''press dobavit'''
    page.locator(BUTTON_DOBAVIT).click()
    page.wait_for_selector(INPUT_NAME)
    '''check'''
    expect(page.locator(INPUT_LOGIN)).to_have_value("1createManagerByAdmin", timeout=wait_until_visible)
    expect(page.locator(INPUT_NAME)).to_have_value("newManager", timeout=wait_until_visible)
    expect(page.locator(INPUT_EMAIL)).to_have_value("mail@mail.com", timeout=wait_until_visible)
    expect(page.get_by_text("Интегратор")).to_have_count(2, timeout=wait_until_visible)  #slovalos potomu 4to noviy punkt menu
    page.wait_for_timeout(2000)

    delete_added_user(page)

    expect(page.locator(INPUT_LOGIN)).to_have_value(LOGIN, timeout=wait_until_visible)

    delete_user(API_URL, USER_ID, BEARER, ACCESS_TOKEN)