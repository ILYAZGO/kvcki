from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.users import *
import pytest

'''Precondition : manager should have access_rights for create and delete user'''
@pytest.mark.users
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    auth(MANAGER, PASSWORD, page)

    go_to_users(page)

    set_user("newOne",
             "1createUserByManager",
             PASSWORD,
             "mail@mail.com",
             "someComment",
             "Компания",
             page)

    set_stt("Русский",
            "IMOT.IO",
            "Стандарт",
            page)

    '''press dobavit'''
    page.locator(BUTTON_DOBAVIT).click()
    page.wait_for_selector(INPUT_NAME)
    #'''go to profile'''
    #page.get_by_text("newOne", exact=True).click(timeout=wait_until_visible)
    ''''''
    expect(page.locator(INPUT_LOGIN)).to_have_value("1createUserByManager", timeout=wait_until_visible)
    expect(page.locator(INPUT_NAME)).to_have_value("newOne", timeout=wait_until_visible)
    expect(page.locator(INPUT_EMAIL)).to_have_value("mail@mail.com", timeout=wait_until_visible)
    expect(page.get_by_text("Компания")).to_have_count(1, timeout=wait_until_visible)

    delete_added_user(page)

    expect(page.locator(INPUT_LOGIN)).to_have_value("3managerIM", timeout=wait_until_visible)