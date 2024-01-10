from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.markup import *
from utils.create_delete_user import create_user, delete_user
import pytest

'''Create, rename, delete check-list'''

@pytest.mark.check_list
def test_example(page: Page) -> None:
    USER_ID, BEARER, ACCESS_TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    page.goto("http://192.168.10.101/feature-dev-1638/", timeout=timeout)

    auth(LOGIN, PASSWORD, page)

    create_check_list_with_questions_and_answers("12345","Question1", "Question2", page)

    '''check created'''
    expect(page.get_by_text("12345")).to_be_visible(timeout=wait_until_visible)

    '''rename from title'''
    page.get_by_text("12345").click()
    page.locator('[name="title"]').clear()
    page.locator('[name="title"]').fill("654321")
    page.wait_for_timeout(1000)
    '''save'''
    page.locator(BUTTON_SAVE).click()

    '''rename from left list'''
    page.wait_for_selector(BUTTON_PENCIL)
    page.locator(BUTTON_PENCIL).click()
    page.locator(INPUT_LEFT_CHECK_LIST_NAME).fill("98765")
    page.locator(BUTTON_SAVE_EDITED_NAME).get_by_role("button").first.click()
    page.wait_for_timeout(1000)

    expect(page.get_by_text("98765")).to_be_visible(timeout=wait_until_visible)

    '''delete'''
    delete_check_list(page)

    '''check deleted'''
    page.wait_for_selector(NI4EGO_NE_NAYDENO)
    expect(page.locator(NI4EGO_NE_NAYDENO)).to_be_visible(timeout=wait_until_visible)

    delete_user(API_URL, USER_ID, BEARER, ACCESS_TOKEN)