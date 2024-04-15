from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.settings import *
from utils.create_delete_user import create_user, delete_user
import pytest


# check changing and saving personal info for user
@pytest.mark.independent
@pytest.mark.settings
def test_example(page: Page) -> None:
    USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    page.goto(URL, timeout=timeout)

    auth(LOGIN, PASSWORD, page)

    click_settings(page)

    fill_personal_information_user_and_operator("someName", EMAIL3, "1234567890", "Africa/Bamako", page)

    press_save(page)

    click_notifications(page)

    click_settings(page)

    expect(page.locator(INPUT_LOGIN)).to_be_disabled()
    expect(page.locator(INPUT_EMAIL)).to_have_value(EMAIL3)
    expect(page.locator(INPUT_PHONE)).to_have_value("1234567890")
    expect(page.locator(INPUT_COMMENT)).not_to_be_visible()
    expect(page.get_by_text("Africa/Bamako")).to_be_visible()
    expect(page.locator(SELECT_INDUSTRY)).not_to_be_visible()
    expect(page.locator(SELECT_PARTNER)).not_to_be_visible()

    page.reload()
    page.wait_for_selector(INPUT_EMAIL)
    page.wait_for_timeout(300)

    expect(page.locator(INPUT_LOGIN)).to_be_disabled()
    expect(page.locator(INPUT_EMAIL)).to_have_value(EMAIL3)
    expect(page.locator(INPUT_PHONE)).to_have_value("1234567890")
    expect(page.locator(INPUT_COMMENT)).not_to_be_visible()
    expect(page.get_by_text("Africa/Bamako")).to_be_visible()
    expect(page.locator(SELECT_INDUSTRY)).not_to_be_visible()
    expect(page.locator(SELECT_PARTNER)).not_to_be_visible()

    delete_user(API_URL, TOKEN, USER_ID)

