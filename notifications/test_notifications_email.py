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

    add_notification("Email", page)

    set_notification_name("auto-test-email", page)

    #  send again when rull changed
    page.locator('[class*="mainArea"]').locator('[type="checkbox"]').click()

    #  expect(page.locator('[class*="mainArea"]').locator('[type="checkbox"]')).to_be_checked()  OPEN AFTER DEV_1888 fix

    #  add_filter("По тегам", "22222", "0", page)

    fill_message("someText ", page)

    fill_attr_for_email('letterTheme', 'mail@.mail.com', page)

    save_or_cancel_rule("0", page)

    go_back_in_rule_after_save("auto-test-email", page)

    expect(page.locator('[class*="mainArea"]').locator('[type="checkbox"]')).to_be_checked()
    expect(page.locator('[class*="sidebar"]').locator('[type="checkbox"]')).to_be_checked()
    expect(page.locator(INPUT_COMMENT)).to_have_text("someText {{call_id}}")
    expect(page.locator(INPUT_NOTIFICATION_NAME)).to_have_value("auto-test-email")
    expect(page.locator(INPUT_LETTER_THEME)).to_have_value("letterTheme")
    expect(page.locator(INPUT_EMAIL)).to_have_value("mail@.mail.com")

    delete_rule(page)

    expect(page.locator(BUTTON_KORZINA)).not_to_be_visible()

    delete_user(API_URL, TOKEN, USER_ID)
