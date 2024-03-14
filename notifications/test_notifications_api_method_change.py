from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.notifications import *
from utils.create_delete_user import create_user, delete_user
import pytest


@pytest.mark.independent
@pytest.mark.notifications
def test_example(page: Page) -> None:
    USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    page.goto(URL, timeout=timeout)

    auth(LOGIN, PASSWORD, page)

    go_to_notifications_page(page)

    add_notification("API", page)

    set_notification_name("auto-test-api_method_change", page)

    set_url_and_headers("https://www.google.com/", "someHeaders", page)

    fill_message("someText ", page)

    change_api_method("POST", "GET", page)

    save_rule(page)

    go_back_in_rule_after_save("auto-test-api_method_change", page)

    page.reload()
    page.wait_for_selector(BlOCK_API)

    expect(page.locator(BlOCK_API)).to_have_text("API*GET")

    change_api_method("GET", "PUT", page)

    save_rule(page)

    go_back_in_rule_after_save("auto-test-api_method_change", page)

    page.reload()

    page.wait_for_selector(BlOCK_API)
    expect(page.locator(BlOCK_API)).to_have_text("API*PUT")

    change_api_method("PUT", "PATCH", page)

    save_rule(page)
    go_back_in_rule_after_save("auto-test-api_method_change", page)

    page.reload()

    page.wait_for_selector(BlOCK_API)
    expect(page.locator(BlOCK_API)).to_have_text("API*PATCH")

    change_api_method("PATCH", "POST", page)

    save_rule(page)
    go_back_in_rule_after_save("auto-test-api_method_change", page)

    page.reload()

    page.wait_for_selector(BlOCK_API)
    expect(page.locator(BlOCK_API)).to_have_text("API*POST")

    delete_rule(page)

    expect(page.locator(BUTTON_KORZINA)).not_to_be_visible()

    delete_user(API_URL, TOKEN, USER_ID)
