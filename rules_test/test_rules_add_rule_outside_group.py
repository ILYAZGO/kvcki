from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.markup import *
from utils.create_delete_user import create_user, delete_user
import pytest

'''Create tag in group and outside group'''


@pytest.mark.rules
def test_example(page: Page) -> None:
    USER_ID, BEARER, ACCESS_TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    page.goto(URL, timeout=timeout)
    '''login'''
    auth(LOGIN, PASSWORD, page)
    '''go to razmetka'''
    page.locator(BUTTON_RAZMETKA).click()
    page.wait_for_timeout(1000)
    page.wait_for_selector(BUTTON_DOBAVIT_TEG)

    '''create group'''
    page.locator(BUTTON_DOBAVIT_TEG).click()
    page.wait_for_selector(INPUT_NAZVANIE_TEGA)
    page.locator(INPUT_NAZVANIE_TEGA).type("66666", timeout=wait_until_visible)
    page.keyboard.press('Enter')  # kostil'
    page.wait_for_timeout(2000)
    #page.get_by_role("button", name="Отправить").click() #otpravit

    '''check'''
    page.wait_for_selector(NAZVANIE_PRAVILA_TEGIROVANIYA)
    expect(page.locator(NAZVANIE_PRAVILA_TEGIROVANIYA)).to_have_value("66666")

    ''''teardown'''
    page.locator(".css-izdlur").click(timeout=wait_until_visible)
    page.get_by_text("Удалить", exact=True).click(timeout=wait_until_visible)
    page.get_by_role("button", name="Удалить").click(timeout=wait_until_visible)
    page.wait_for_timeout(1000)
    page.locator('[aria-label="Удалить"]').first.click()
    #page.locator(BUTTON_KORZINA).click()

    '''check teardown'''
    expect(page.get_by_text("Неотсортированные")).not_to_be_visible(timeout=wait_until_visible)

    delete_user(API_URL, USER_ID, BEARER, ACCESS_TOKEN)
