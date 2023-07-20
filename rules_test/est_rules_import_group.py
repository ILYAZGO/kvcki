from playwright.sync_api import Page, expect
from utils.variables import *

'''
1 login admin
2 choose user in bar
3 go to rules
4 click import rules
5 choose user
6 choose rules
7'''
def test_example(page: Page) -> None:
    page.goto(URL)
    '''login'''
    page.locator("[id='mui-1']").fill(ADMIN)
    page.locator("[id='mui-2']").fill(PASSWORD)
    page.locator("[id='mui-3']").click()

    page.get_by_role("link", name="Разметка").click()
    page.locator("#react-select-2-input").fill("import")

    #page.get_by_role("button", name="Импортировать правила").click()
    