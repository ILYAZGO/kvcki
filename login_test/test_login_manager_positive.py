from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.login import *
import pytest

@pytest.mark.login
def test_example(page: Page) -> None:

    page.goto(URL, timeout=timeout)

    auth(MANAGER, PASSWORD, page)

    quit_from_profile(page)

    expect(page.locator(BUTTON_VOITI)).to_be_visible()