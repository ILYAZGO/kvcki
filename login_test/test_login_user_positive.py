from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
import pytest

@pytest.mark.login
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    auth(USER, PASSWORD, page)
    page.wait_for_timeout(4000)
    page.locator('[aria-label="Профиль"]').get_by_role("button").click()
    page.get_by_text("Выйти", exact=True).click()
    expect(page.locator("[id='mui-3']")).to_be_visible()




