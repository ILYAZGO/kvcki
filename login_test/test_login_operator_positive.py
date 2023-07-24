from playwright.sync_api import Page, expect
from utils.variables import *
import pytest

@pytest.mark.login
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    page.locator("[id='mui-1']").click()
    page.locator("[id='mui-1']").fill(OPERATOR)
    page.locator("[id='mui-2']").click()
    page.locator("[id='mui-2']").fill(PASSWORD)
    page.locator("[id='mui-3']").click()
    page.locator(".css-1moonrh-control > div > .MuiButtonBase-root").click()
    page.get_by_text("Выйти", exact=True).click()
    expect(page.locator("[id='mui-3']")).to_be_visible()
