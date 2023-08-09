from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.users import *
import pytest


@pytest.mark.users
def test_example(page: Page) -> None:
    page.goto("http://192.168.10.101/feature-dev-951/ru", timeout = timeout)
    '''login'''
    auth(ADMIN, PASSWORD, page)
    '''go to polzovateli'''
    page.locator(BUTTON_POLZOVATELI).click()
    '''fill search'''
    page.locator(INPUT_POISK).fill("ec")
    '''check'''
    expect(page.get_by_text("ecotelecom"))
    expect(page.get_by_text("eco_op1"))
    expect(page.get_by_text("eco_op2"))

