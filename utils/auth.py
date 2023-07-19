from playwright.sync_api import Page, expect
from utils.variables import *

def auth(page: Page) -> None:
    page.locator("[id='mui-1']").fill(OPERATOR)
    page.locator("[id='mui-2']").fill(PASSWORD)
    page.locator("[id='mui-3']").click()