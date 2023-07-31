from playwright.sync_api import Page, expect
from utils.variables import *
from utils.dates import *
from utils.auth import *
import pytest

@pytest.mark.dictionaries
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    auth(ECOTELECOM, ECOPASS, page)
    '''go to razmetka'''
    page.locator('//*[@id="root"]/div/div/div[1]/div/div[1]/div[2]/button[3]/a').click()
    '''go to dictionaries'''
    page.get_by_test_id("markup_nav_dicts").click()
    '''search (should not depend on register)'''
    page.locator('//html/body/div/div/div/div[2]/div/div/div[1]/div[2]/div[1]/form/div/div[1]/div[1]/div/input').fill("seat")
    page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[1]/div[2]/div[1]/form/div/div[1]/div[2]/button').click()
    '''check'''
    expect(page.get_by_text("Seat")).to_have_count(1)