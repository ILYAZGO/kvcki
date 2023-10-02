from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
import pytest

@pytest.mark.login
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    auth(MANAGER, PASSWORD, page)
    page.locator(".css-1moonrh-control > div > .MuiButtonBase-root").click()
    page.get_by_text("Выйти", exact=True).click()
    expect(page.locator("[id='mui-3']")).to_be_visible()