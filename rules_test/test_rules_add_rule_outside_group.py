from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.markup import *
from utils.create_delete_user import create_user, delete_user
import pytest
import time

'''Create tag in group and outside group'''


@pytest.mark.rules
def test_example(page: Page) -> None:
    USER_ID, BEARER, ACCESS_TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    page.goto(URL, timeout=timeout)
    '''login'''
    auth(LOGIN, PASSWORD, page)
    '''go to razmetka'''
    page.locator(BUTTON_RAZMETKA).click()
    time.sleep(2)

    '''create group'''
    page.get_by_test_id(BUTTON_DOBAVIT_TEG).click()
    page.get_by_test_id(INPUT_NAZVANIE_TEGA).type("66666", timeout=wait_until_visible)
    page.keyboard.press('Enter')  # kostil'

    time.sleep(5)
    # page.get_by_test_id("markup_newRuleApply").click() #otpravit
    '''check'''
    expect(page.locator(NAZVANIE_PRAVILA_TEGIROVANIYA)).to_have_value("66666")  # check rule
    time.sleep(3)
    # expect(page.get_by_text("Неотсортированные")).to_have_count(count=2)  # po4emu to valitsa
    ''''teardown'''
    page.locator(".css-izdlur").click(timeout=wait_until_visible)
    page.get_by_text("Удалить", exact=True).click(timeout=wait_until_visible)
    page.get_by_role("button", name="Удалить").click(timeout=wait_until_visible)
    page.get_by_label("Удалить").get_by_role("button").click()
    #page.locator(BUTTON_KORZINA).click()
    '''check teardown'''
    expect(page.get_by_text("Неотсортированные")).not_to_be_visible(timeout=wait_until_visible)

    delete_user(API_URL, USER_ID, BEARER, ACCESS_TOKEN)
