from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.reports import *
import pytest



@pytest.mark.reports
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    auth(ECOTELECOM, ECOPASS, page)
    '''go to reports'''
    page.locator(BUTTON_OT4ETI).click()
    page.locator(INPUT_SEARCH).fill("Ntcn")
    page.locator(BUTTON_LUPA).click()
    expect(page.locator(INPUT_SEARCH)).to_have_value("Ntcn")
    expect(page.get_by_text("Ntcn")).to_have_count(1)

