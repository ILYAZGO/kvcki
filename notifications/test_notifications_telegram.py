from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.notifications import *
from utils.create_delete_user import create_user, delete_user
import pytest

@pytest.mark.notifications
def test_example(page: Page) -> None:
    USER_ID, BEARER, ACCESS_TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    page.goto(URL, timeout=timeout)

    auth(LOGIN, PASSWORD, page)

    add_notification("Telegram", page)

    set_notification_name("auto-test-telegram", page)

    #add_filter("По тегам", "22222", "1", page)

    fill_message("someText ", page)

    #  send with call
    page.locator('[type="checkbox"]').nth(0).click()

    save_or_cancel_rule("0", page)

    delete_rule(page)

    expect(page.locator(BUTTON_KORZINA)).not_to_be_visible()

    delete_user(API_URL, USER_ID, BEARER, ACCESS_TOKEN)
