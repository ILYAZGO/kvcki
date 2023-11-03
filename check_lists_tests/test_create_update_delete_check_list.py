from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.markup import *
from utils.create_delete_user import create_user, delete_user
import pytest

'''Create,delete,update check-list'''

@pytest.mark.check_list
def test_example(page: Page) -> None:
    USER_ID, BEARER, ACCESS_TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    page.goto(URL, timeout=timeout)

    '''login'''
    auth(LOGIN, PASSWORD, page)
    '''create check-list'''
    page.wait_for_selector(BUTTON_RAZMETKA)
    page.locator(BUTTON_RAZMETKA).click()
    page.locator(BUTTON_CHECK_LIST).click()
    page.wait_for_selector(BUTTON_DOBAVIT_CHECK_LIST)
    page.locator(BUTTON_DOBAVIT_CHECK_LIST).click()


    page.wait_for_selector(INPUT_CHECK_LIST_NAME)
    page.locator(INPUT_CHECK_LIST_NAME).fill("12345")

    create_questions_and_answers("Question1", "Question2", page)

    '''save'''
    page.locator(BUTTON_SAVE).click()
    '''check created'''
    expect(page.get_by_text("12345")).to_be_visible(timeout=wait_until_visible)

    '''update'''
    page.get_by_text("12345").click()
    page.locator(INPUT_FIRST_QUESTION).clear()
    page.locator(INPUT_FIRST_QUESTION).fill("654321")

    '''save'''
    page.locator(BUTTON_SAVE).click()

    create_delete_appriser("Appriser", page)

    '''save'''
    page.locator(BUTTON_SAVE).click()

    '''delete'''
    delete_check_list(page)

    '''check deleted'''
    page.wait_for_selector(NI4EGO_NE_NAYDENO)
    expect(page.locator(NI4EGO_NE_NAYDENO)).to_be_visible(timeout=wait_until_visible)

    delete_user(API_URL, USER_ID, BEARER, ACCESS_TOKEN)