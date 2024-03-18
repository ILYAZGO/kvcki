from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.settings import *
from utils.create_delete_user import create_user, delete_user, create_operator
import pytest


# check admin can change rights for user and operator
@pytest.mark.independent
@pytest.mark.settings
def test_example(page: Page) -> None:
    USER_ID_ADMIN, TOKEN_ADMIN, LOGIN_ADMIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)
    USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)
    USER_ID_OPERATOR, TOKEN_OPERATOR, LOGIN_OPERATOR = create_operator(API_URL, USER_ID_USER, PASSWORD)

    page.goto(URL, timeout=timeout)

    auth(LOGIN_ADMIN, PASSWORD, page)

    # change rights for user
    go_to_user(LOGIN_USER, page)

    click_settings(page)

    click_rights(page)

    expect(page.locator(BLOCK_ONE_RIGHT)).to_have_count(3)

    click_all_checkboxes_on_page(page)

    press_save_in_rights(page)

    page.reload()
    page.wait_for_selector(BUTTON_SAVE_IN_RIGHTS)

    all_checkboxes_to_be_checked(page)

    assert all_checkboxes_to_be_checked(page) == True

    # change rights for operator

    click_employees(page)

    go_to_operator_from_table(page)

    click_rights(page)

    expect(page.locator(BLOCK_ONE_RIGHT)).to_have_count(22)

    click_all_checkboxes_on_page(page)

    press_save_in_rights(page)

    page.reload()
    page.wait_for_selector(BUTTON_SAVE_IN_RIGHTS)

    all_checkboxes_to_be_checked(page)

    assert all_checkboxes_to_be_checked(page) == True

    delete_user(API_URL, TOKEN_ADMIN, USER_ID_ADMIN)
    delete_user(API_URL, TOKEN_USER, USER_ID_USER)
    delete_user(API_URL, TOKEN_OPERATOR, USER_ID_OPERATOR)
