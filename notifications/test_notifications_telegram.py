from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.notifications import *
import pytest

@pytest.mark.notifications
def test_example(page: Page) -> None:

    page.goto(URL, timeout=timeout)

    auth(USER_FOR_IMPORT, PASSWORD, page)

    add_notification("Telegram", page)

    set_notification_name("auto-test-telegram", page)

    add_filter("По тегам", "22222", "1", page)

    fill_message("someText ", page)

    #  send with call
    page.locator('[type="checkbox"]').nth(0).click()

    save_or_cancel_rule("0", page)

    delete_rule(page)

    expect(page.locator(BUTTON_KORZINA)).not_to_be_visible()
