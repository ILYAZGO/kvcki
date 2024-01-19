from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.markup import *
import pytest

@pytest.mark.rules
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)

    auth(ECOTELECOM, ECOPASS, page)

    go_to_markup(page)


    page.wait_for_selector('[href*="/dictionaries?group"]')
    '''search (should not depend on register)'''
    page.locator(INPUT_POISK).nth(1).fill("coope")
    #page.locator("form").get_by_role("button").click()

    '''check'''
    expect(page.get_by_text("Cooper")).to_have_count(1, timeout=wait_until_visible)
