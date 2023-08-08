from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
import pytest
import time

@pytest.mark.users
def test_example(page: Page) -> None:
    page.goto("http://192.168.10.101/feature-dev-951/ru", timeout = timeout)
    '''login'''
    auth(ADMIN, PASSWORD, page)
    '''go to polzovateli'''
    page.locator("#root > div > div.AdminBar_root__ieqog > a").click()
    '''fill search'''
    page.locator("input[name='searchString']").fill("ec")
    '''check'''
    expect(page.get_by_text("ecotelecom"))
    expect(page.get_by_text("eco_op1"))
    expect(page.get_by_text("eco_op2"))

