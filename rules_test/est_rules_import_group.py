from playwright.sync_api import Page, expect
from utils.variables import *

def test_example(page: Page) -> None:
    page.goto(URL)
    '''login'''
    page.locator("[id='mui-1']").fill(ADMIN)
    page.locator("[id='mui-2']").fill(PASSWORD)
    page.locator("[id='mui-3']").click()

    page.get_by_role("link", name="Разметка").click()
    page.get_by_role("button", name="Импортировать правила").click()
    