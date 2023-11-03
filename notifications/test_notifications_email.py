from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.notifications import *
import pytest

@pytest.mark.notifications
def test_example(page: Page) -> None:

    page.goto(URL, timeout=timeout)

    auth(USER_FOR_IMPORT, PASSWORD, page)

    add_notification("Email", page)

    set_notification_name("auto-test-email", page)

    add_filter("По тегам", "22222", "0", page)

    fill_message("someText ", page)

    fill_attr_for_email('letterTheme', 'mail@.mail.com', page)

    save_or_cancel_rule("0", page)

    delete_rule(page)

    expect(page.locator(BUTTON_KORZINA)).not_to_be_visible()
