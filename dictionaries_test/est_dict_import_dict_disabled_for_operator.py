from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.markup import *
from utils.create_delete_user import create_user, delete_user, create_operator
import pytest

#  now for default operator no such access right
@pytest.mark.dictionaries
def test_example(page: Page) -> None:

    USER_ID_USER, BEARER_USER, ACCESS_TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)
    USER_ID_OPERATOR, BEARER_OPERATOR, ACCESS_TOKEN_OPERATOR, LOGIN_OPERATOR = create_operator(API_URL, USER_ID_USER,
                                                                                               PASSWORD)

    page.goto(URL, timeout=timeout)

    auth(LOGIN_OPERATOR, PASSWORD, page)

    go_to_dicts(page)

    '''check '''
    #page.wait_for_timeout(1500)
    expect(page.locator(BUTTON_IMPORTIROVAT_SLOVARI)).to_be_visible()

    delete_user(API_URL, USER_ID_USER, BEARER_USER, ACCESS_TOKEN_USER)
    delete_user(API_URL, USER_ID_OPERATOR, BEARER_OPERATOR, ACCESS_TOKEN_OPERATOR)
