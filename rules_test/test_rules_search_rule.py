from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.markup import *
import pytest

@pytest.mark.rules
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    auth(ECOTELECOM, ECOPASS, page)
    '''go to razmetka'''
    page.locator(BUTTON_RAZMETKA).click()
    '''search (should not depend on register)'''
    page.locator(INPUT_POISK).nth(1).fill("mercury")
    #page.locator("form").get_by_role("button").click()
    '''check'''
    expect(page.get_by_text("Mercury")).to_have_count(1, timeout=wait_until_visible)
