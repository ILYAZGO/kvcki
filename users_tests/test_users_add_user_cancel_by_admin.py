from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.users import *
import pytest


@pytest.mark.users
def test_example(page: Page) -> None:
    page.goto("http://192.168.10.101/feature-dev-1644", timeout=timeout)
    '''login'''
    auth(ADMIN, PASSWORD, page)

    go_to_users(page)

    '''button create user'''
    page.wait_for_selector(BUTTON_DOBAVIT_POLZOVATELIA)
    page.locator(BUTTON_DOBAVIT_POLZOVATELIA).click()
    '''cancel by button CANCEL'''
    page.locator(BUTTON_OTMENA).click()
    '''check'''
    expect(page.get_by_text("Пароль")).not_to_be_visible()
    '''button create user'''
    page.locator(BUTTON_DOBAVIT_POLZOVATELIA).click()
    '''cancel by button KRESTIK'''
    page.locator(BUTTON_KRESTIK).click()
    '''check'''
    expect(page.get_by_text("Пароль")).not_to_be_visible()