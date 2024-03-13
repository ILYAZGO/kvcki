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

    page.goto("http://192.168.10.101/feature-dev-1933", timeout=timeout)

    auth(LOGIN, PASSWORD, page)

    add_notification("API", page)

    set_notification_name("auto-test-api_method_change", page)

    set_url_and_headers("https://www.google.com/", "someHeaders", page)

    fill_message("someText ", page)
    # change method to GET
    page.get_by_text("POST").click()
    page.get_by_text("GET", exact=True).click()

    save_rule(page)
    go_back_in_rule_after_save("auto-test-api_method_change", page)

    page.reload()
    page.wait_for_selector(BlOCK_API)

    expect(page.locator(BlOCK_API)).to_have_text("API*GET")

    # change method to PUT

    page.locator(BlOCK_API).get_by_text("GET").click()
    page.get_by_text("PUT", exact=True).click()

    save_rule(page)

    go_back_in_rule_after_save("auto-test-api_method_change", page)

    page.reload()
    page.wait_for_selector(BlOCK_API)

    expect(page.locator(BlOCK_API)).to_have_text("API*PUT")

    # change method to PUT
    page.locator(BlOCK_API).get_by_text("PUT").click()
    page.get_by_text("PATCH", exact=True).click()

    save_rule(page)
    go_back_in_rule_after_save("auto-test-api_method_change", page)

    page.reload()
    page.wait_for_selector(BlOCK_API)

    expect(page.locator(BlOCK_API)).to_have_text("API*PATCH")

    # change method to POST
    page.locator(BlOCK_API).get_by_text("PATCH").click()
    page.get_by_text("POST", exact=True).click()

    save_rule(page)
    go_back_in_rule_after_save("auto-test-api_method_change", page)

    page.reload()
    page.wait_for_selector(BlOCK_API)

    expect(page.locator(BlOCK_API)).to_have_text("API*POST")

    delete_rule(page)

    expect(page.locator(BUTTON_KORZINA)).not_to_be_visible()

    delete_user(API_URL, TOKEN, USER_ID)
