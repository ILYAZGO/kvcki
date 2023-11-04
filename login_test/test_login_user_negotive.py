from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.login import *
import pytest

@pytest.mark.login
def test_example(page: Page) -> None:

    page.goto(URL, timeout=timeout)

    auth(LOGIN_NEGOTIVE, PASSWORD, page)

    expect(page.locator(ALERT_MESSAGE)).to_be_visible()