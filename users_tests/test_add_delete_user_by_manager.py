from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.users import *
import pytest

'''Precondition : manager should have access_rights for create and delete user'''


@pytest.mark.independent
@pytest.mark.users
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)

    auth(MANAGER, PASSWORD, page)

    go_to_users(page)

    press_button_add_user(page)

    set_user(NEW_NAME,
             NEW_LOGIN,
             PASSWORD,
             EMAIL2,
             "someComment",
             "Компания",
             page)

    set_industry("Недвижимость", page)

    set_stt("Русский",
            "IMOT.IO",
            "Стандарт",
            page)

    press_button_add_in_modal(page)


    expect(page.locator(INPUT_LOGIN)).to_have_value(NEW_LOGIN, timeout=wait_until_visible)
    expect(page.locator(INPUT_NAME)).to_have_value(NEW_NAME, timeout=wait_until_visible)
    expect(page.locator(INPUT_EMAIL)).to_have_value(EMAIL2, timeout=wait_until_visible)
    page.wait_for_timeout(3500)
    expect(page.get_by_text("Компания")).to_have_count(1, timeout=wait_until_visible)
    expect(page.get_by_text("Недвижимость")).to_have_count(1, timeout=wait_until_visible)
    expect(page.locator(INPUT_PHONE)).to_be_visible(timeout=wait_until_visible)
    expect(page.locator(INPUT_NEW_PASSWORD)).to_be_visible(timeout=wait_until_visible)
    expect(page.locator(INPUT_NEW_PASSWORD_REPEAT)).to_be_visible(timeout=wait_until_visible)

    delete_added_user(page)

    expect(page.locator(INPUT_LOGIN)).to_have_value("3managerIM", timeout=wait_until_visible)