from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.notifications import *
from utils.create_delete_user import create_user, delete_user
import pytest

@pytest.mark.notifications
def test_example(page: Page) -> None:
    USER_ID, BEARER, ACCESS_TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    page.goto("http://192.168.10.101/feature-dev-1644", timeout=timeout)

    auth(LOGIN, PASSWORD, page)

    add_notification("API", page)

    set_notification_name("auto-test-api", page)

    set_url_and_headers(URL, "someHeaders", page)

    #  send again when rull changed
    page.locator('[type="checkbox"]').nth(0).click()

    #add_filter("По тегам", "22222", "0", page)  uncomment later

    fill_message("someText ", page)

    save_or_cancel_rule("0", page)

    delete_rule(page)

    expect(page.locator(BUTTON_KORZINA)).not_to_be_visible()

    delete_user(API_URL, USER_ID, BEARER, ACCESS_TOKEN)
