from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.notifications import *
import pytest

@pytest.mark.reports
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    auth(ECOTELECOM, ECOPASS, page)

    page.locator(BUTTON_OPOVESHENIA).click()
    #  add new
    page.locator(".styles_addNewRule__zhZVC").get_by_role("button").click()
    #  click to list
    page.locator('[class="css-8mmkcg"]').first.click()

    page.locator('[class=" css-164zrm5-menu"]').get_by_text("Email", exact=True).click()
