from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.users import *
from utils.create_delete_user import create_user, delete_user
import pytest


@pytest.mark.independent
@pytest.mark.users
def test_example(page: Page) -> None:
    USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    page.goto(URL, timeout=timeout)

    auth(LOGIN, PASSWORD, page)

    go_to_users(page)

    press_button_add_user(page)

    set_user(NEW_NAME,
             NEW_LOGIN,
             PASSWORD,
             EMAIL3,
             "someComment",
             "Компания",
             page)

    set_industry_and_partner("Недвижимость",
                             "managerIM",
                             page)

    set_stt("Русский",
            "Deepgram",
            "whisper",
            page)

    press_button_add_in_modal(page)

    '''check'''
    expect(page.locator(INPUT_LOGIN)).to_have_value(NEW_LOGIN, timeout=wait_until_visible)
    expect(page.locator(INPUT_NAME)).to_have_value(NEW_NAME, timeout=wait_until_visible)
    expect(page.locator(INPUT_EMAIL)).to_have_value(EMAIL3, timeout=wait_until_visible)
    #page.wait_for_timeout(2300)
    expect(page.locator(INPUT_COMMENT)).to_have_text("someComment", timeout=wait_until_visible)
    expect(page.locator(SELECT_ROLE)).to_have_text("Компания", timeout=wait_until_visible)
    expect(page.locator(SELECT_INDUSTRY)).to_have_text("Недвижимость", timeout=wait_until_visible)
    expect(page.locator(SELECT_PARTNER)).to_have_text("managerIM", timeout=wait_until_visible)
    expect(page.locator(INPUT_PHONE)).to_be_visible(timeout=wait_until_visible)
    expect(page.locator(INPUT_NEW_PASSWORD)).to_be_visible(timeout=wait_until_visible)
    expect(page.locator(INPUT_NEW_PASSWORD_REPEAT)).to_be_visible(timeout=wait_until_visible)

    delete_added_user(page)

    expect(page.locator(INPUT_LOGIN)).to_have_value(LOGIN, timeout=wait_until_visible)

    delete_user(API_URL, TOKEN, USER_ID)