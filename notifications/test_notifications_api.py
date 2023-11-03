from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.notifications import *
import pytest

@pytest.mark.reports
def test_example(page: Page) -> None:

    page.goto(URL, timeout=timeout)

    auth(USER_FOR_IMPORT, PASSWORD, page)

    add_notification("API", page)

    set_notification_name("auto-test-api", page)

    set_url_and_headers(URL, "someHeaders", page)

    #  send again when rull changed
    page.locator('[type="checkbox"]').nth(0).click()

    add_filter("По тегам", "22222", page)

    fill_message("someText ", page)


    page.locator('[class="styles_buttonsGroup__aLY1I"]').get_by_role("button").nth(0).click()

    page.wait_for_selector(BUTTON_KORZINA)

    page.locator('[type="checkbox"]').nth(0).click()

    page.locator(BUTTON_KORZINA).click()

    page.locator('[class="styles_buttonsGroup__D0bLG"]').get_by_role("button").nth(1).click()

    expect(page.locator(BUTTON_KORZINA)).not_to_be_visible()
