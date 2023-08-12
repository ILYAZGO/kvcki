from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.users import *
import pytest


@pytest.mark.users
def test_example(page: Page) -> None:
    page.goto(URL, timeout = timeout)
    '''login'''
    auth(ADMIN, PASSWORD, page)
    '''go to polzovateli'''
    page.locator(BUTTON_POLZOVATELI).click()
    '''fill search'''
    page.locator(INPUT_POISK).fill("ec")
    '''check'''
    expect(page.get_by_text("ecotelecom")).to_be_visible()
    expect(page.get_by_text("1userIM")).not_to_be_visible()


