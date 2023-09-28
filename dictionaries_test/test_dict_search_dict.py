from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.markup import *
import pytest

@pytest.mark.dictionaries
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    auth(ECOTELECOM, ECOPASS, page)
    '''go to razmetka'''
    page.wait_for_selector(BUTTON_RAZMETKA)
    page.locator(BUTTON_RAZMETKA).click()
    '''go to dictionaries'''
    page.locator(BUTTON_SLOVARI).click()
    '''search (should not depend on register)'''
    page.locator(INPUT_POISK).nth(1).fill("seat")
    #page.locator("form").get_by_role("button").click()
    '''check'''
    expect(page.get_by_text("Seat")).to_have_count(1, timeout=wait_until_visible)