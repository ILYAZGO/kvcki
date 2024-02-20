from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.notifications import *
from utils.create_delete_user import create_user, delete_user
import pytest

@pytest.mark.notifications
def test_example(page: Page) -> None:
    USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    page.goto(URL, timeout=timeout)

    auth(LOGIN, PASSWORD, page)

    add_notification("Email", page)

    set_notification_name("auto-test-email", page)

    #add_filter("По тегам", "22222", "0", page)

    fill_message("someText ", page)

    fill_attr_for_email('letterTheme', 'mail@.mail.com', page)

    save_or_cancel_rule("0", page)

    delete_rule(page)

    expect(page.locator(BUTTON_KORZINA)).not_to_be_visible()

    delete_user(API_URL, TOKEN, USER_ID)
