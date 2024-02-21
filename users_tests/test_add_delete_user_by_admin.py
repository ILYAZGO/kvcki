from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.users import *
from utils.create_delete_user import create_user, delete_user
import pytest


@pytest.mark.users
def test_example(page: Page) -> None:
    USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    page.goto(URL, timeout=timeout)

    auth(LOGIN, PASSWORD, page)

    go_to_users(page)

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

    # '''add quota'''
    # page.locator(INPUT_QUOTA).fill("60")

    '''press dobavit'''
    page.locator(BUTTON_DOBAVIT).click()
    page.wait_for_selector(INPUT_NAME)
    '''check'''
    expect(page.locator(INPUT_LOGIN)).to_have_value(NEW_LOGIN, timeout=wait_until_visible)
    expect(page.locator(INPUT_NAME)).to_have_value(NEW_NAME, timeout=wait_until_visible)
    expect(page.locator(INPUT_EMAIL)).to_have_value(EMAIL3, timeout=wait_until_visible)
    page.wait_for_timeout(1400)
    expect(page.get_by_text("Компания")).to_have_count(1, timeout=wait_until_visible)
    expect(page.get_by_text("Недвижимость")).to_have_count(1, timeout=wait_until_visible)
    expect(page.get_by_text("managerIM")).to_have_count(1, timeout=wait_until_visible)



    delete_added_user(page)

    expect(page.locator(INPUT_LOGIN)).to_have_value(LOGIN, timeout=wait_until_visible)

    delete_user(API_URL, TOKEN, USER_ID)