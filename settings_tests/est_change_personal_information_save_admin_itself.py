from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.settings import *
from utils.create_delete_user import create_user, delete_user
import pytest


# check changing and saving personal info for admin
@pytest.mark.independent
@pytest.mark.settings
def test_example(page: Page) -> None:
    NEW_NAME = NEW_LOGIN = f"auto_test_user_{datetime.now().strftime('%m%d%H%M')}_{datetime.now().microsecond}"
    EMAIL = f"email_{datetime.now().microsecond}{random.randint(100, 200)}@mail.ru"

    USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    page.goto(URL, timeout=timeout)

    auth(LOGIN, PASSWORD, page)

    click_settings(page)

    change_login(NEW_LOGIN, page)

    press_save(page)

    fill_personal_information_admin_and_manager(NEW_NAME, EMAIL, "1234567890", "someComment", "Africa/Bamako", page)

    press_save(page)

    click_notifications(page)

    click_settings(page)

    expect(page.locator(INPUT_LOGIN)).to_have_value(NEW_LOGIN)
    expect(page.locator(INPUT_EMAIL)).to_have_value(EMAIL)
    expect(page.locator(INPUT_PHONE)).to_have_value("1234567890")
    expect(page.locator(INPUT_COMMENT)).to_have_value("someComment")
    expect(page.get_by_text("Africa/Bamako")).to_be_visible()
    expect(page.locator(SELECT_INDUSTRY)).not_to_be_visible()
    expect(page.locator(SELECT_PARTNER)).not_to_be_visible()


    page.reload()
    page.wait_for_selector(INPUT_EMAIL)
    page.wait_for_timeout(300)

    expect(page.locator(INPUT_LOGIN)).to_have_value(NEW_LOGIN)
    expect(page.locator(INPUT_EMAIL)).to_have_value(EMAIL)
    expect(page.locator(INPUT_PHONE)).to_have_value("1234567890")
    expect(page.locator(INPUT_COMMENT)).to_have_value("someComment")
    expect(page.get_by_text("Africa/Bamako")).to_be_visible()
    expect(page.locator(SELECT_INDUSTRY)).not_to_be_visible()
    expect(page.locator(SELECT_PARTNER)).not_to_be_visible()

    delete_user(API_URL, TOKEN, USER_ID)

