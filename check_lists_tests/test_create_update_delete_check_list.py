from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.markup import *
from utils.create_delete_user import create_user, delete_user
import pytest
import time

'''Create,delete,update check-list'''

@pytest.mark.check_list
def test_example(page: Page) -> None:
    USER_ID, BEARER, ACCESS_TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    page.goto(URL, timeout=timeout)

    '''login'''
    auth(LOGIN, PASSWORD, page)
    '''create check-list'''
    page.locator(BUTTON_RAZMETKA).click()
    page.locator(BUTTON_CHECK_LIST).click()
    page.wait_for_selector(BUTTON_DOBAVIT_CHECK_LIST)
    page.locator(BUTTON_DOBAVIT_CHECK_LIST).click()
    page.wait_for_selector(INPUT_CHECK_LIST_NAME)
    page.locator(INPUT_CHECK_LIST_NAME).fill("12345")
    page.locator("[name='questions.0.title']").fill("123456")
    page.locator("[name='questions.0.answers.0.answer']").fill("1234567")
    '''save'''
    page.locator(".MuiButton-contained").click()
    '''check created'''
    expect(page.get_by_text("12345")).to_be_visible(timeout=wait_until_visible)
    #expect(page.get_by_text("Чек-лист добавлен")).to_be_visible()

    '''update'''
    page.get_by_text("12345").click()
    page.locator("[name='questions.0.title']").clear()
    page.locator("[name='questions.0.title']").fill("654321")
    '''save'''
    #page.locator("button[type='submit']").click()
    page.locator(".MuiButton-contained").click()
    #'''check updated'''
    #expect(page.get_by_text("Чек-лист обновлен")).to_be_visible()
    '''delete'''
    page.locator("button[aria-label='Удалить']").click()
    #page.locator(BUTTON_KORZINA).click()
    page.get_by_role("button", name="Удалить").click()
    '''check deleted'''
    time.sleep(2)
    #expect(page.get_by_text("Чек-лист удален")).to_be_visible()
    expect(page.locator(NI4EGO_NE_NAYDENO)).to_be_visible(timeout=wait_until_visible)

    delete_user(API_URL, USER_ID, BEARER, ACCESS_TOKEN)