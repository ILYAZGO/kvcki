from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.users import *
from utils.create_delete_user import create_user, delete_user
import pytest


@pytest.mark.independent
@pytest.mark.users
def test_example(page: Page) -> None:
    USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    page.goto(URL, timeout=timeout)

    auth(LOGIN, PASSWORD, page)
    '''go to nastroiki'''
    page.locator(BUTTON_NASTROIKI).click()
    '''go to sotrudniki'''
    page.locator(BUTTON_SOTRUDNIKI).click()

    press_button_add_employee(page)

    set_operator(NEW_OPERATOR_NAME,
                 NEW_OPERATOR_LOGIN,
                 PASSWORD,
                 EMAIL1,
                 EMAIL2,
                 EMAIL3,
                 page)

    press_button_add_in_modal(page)

    expect(page.locator(INPUT_NAME)).to_have_value(NEW_OPERATOR_NAME, timeout=wait_until_visible)
    expect(page.locator(INPUT_LOGIN)).to_have_value(NEW_OPERATOR_LOGIN, timeout=wait_until_visible)
    #expect(page.locator(INPUT_PHONE)).to_have_value(EMAIL1, timeout=wait_until_visible)  open after https://task.imot.io/browse/DEV-1982
    expect(page.locator(INPUT_EMAIL)).to_have_value(EMAIL2, timeout=wait_until_visible)
    expect(page.locator(INPUT_COMMENT)).to_have_text(EMAIL3, timeout=wait_until_visible)
    expect(page.locator(INPUT_PHONE)).to_be_visible(timeout=wait_until_visible)
    expect(page.locator(INPUT_NEW_PASSWORD)).to_be_visible(timeout=wait_until_visible)
    expect(page.locator(INPUT_NEW_PASSWORD_REPEAT)).to_be_visible(timeout=wait_until_visible)

    delete_added_user(page)

    expect(page.locator(BUTTON_DOBAVIT_SOTRUDNIKA)).to_be_visible(timeout=wait_until_visible)
    expect(page.locator(USER_LOGIN_IN_LEFT_MENU)).to_have_text(LOGIN, timeout=wait_until_visible)

    delete_user(API_URL, TOKEN, USER_ID)

