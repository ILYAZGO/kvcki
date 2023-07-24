from playwright.sync_api import Page, expect
from utils.variables import *

def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    page.locator("[id='mui-1']").click()
    page.locator("[id='mui-1']").fill(USER)
    page.locator("[id='mui-2']").click()
    page.locator("[id='mui-2']").fill(PASSWORD_NEGOTIVE)
    page.locator("[id='mui-3']").click()
    expect(page.locator(".MuiAlert-message")).to_be_visible()