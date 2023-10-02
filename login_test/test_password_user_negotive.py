from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
import pytest

@pytest.mark.login
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    auth(USER, PASSWORD_NEGOTIVE, page)
    expect(page.locator(".MuiAlert-message")).to_be_visible()