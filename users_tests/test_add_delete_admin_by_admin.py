from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.users import *
from utils.create_delete_user import create_user, delete_user
import pytest
import time

@pytest.mark.users
def test_example(page: Page) -> None:
    USER_ID, BEARER, ACCESS_TOKEN, LOGIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    page.goto(URL, timeout=timeout)
    '''login'''
    auth(LOGIN, PASSWORD, page)
    '''go to polzovateli'''
    page.get_by_test_id(BUTTON_POLZOVATELI).click()
    '''button create user'''
    page.get_by_test_id(BUTTON_DOBAVIT_POLZOVATELIA).click()
    '''fill required'''
    page.locator(INPUT_NAME).fill("newAdmin")
    page.locator(INPUT_LOGIN).fill("1createAdminByAdmin")
    page.locator(INPUT_PASSWORD).fill(PASSWORD)
    page.locator(INPUT_EMAIL).fill("mail@mail.com")
    page.get_by_test_id(INPUT_COMMENT).fill("someComment")
    page.locator(CHOOSE_ROLE).fill("Администратор")
    '''press enter'''
    page.keyboard.press("Enter")
    '''press dobavit'''
    page.get_by_test_id(BUTTON_DOBAVIT).click()
    time.sleep(2)
    '''go to profile'''
    page.get_by_text("newAdmin", exact=True).click()
    '''check'''
    expect(page.locator(INPUT_NAME)).to_have_value("newAdmin", timeout=wait_until_visible)
    expect(page.locator(INPUT_LOGIN)).to_have_value("1createAdminByAdmin", timeout=wait_until_visible)
    expect(page.locator(INPUT_EMAIL)).to_have_value("mail@mail.com", timeout=wait_until_visible)
    expect(page.get_by_text("Администратор")).to_have_count(1, timeout=wait_until_visible)
    time.sleep(2)
    '''delete user'''
    page.locator(BUTTON_KORZINA).click()
    page.locator(BUTTON_PODTVERDIT).click()

    expect(page.locator(INPUT_LOGIN)).to_have_value(LOGIN, timeout=wait_until_visible)

    delete_user(API_URL, USER_ID, BEARER, ACCESS_TOKEN)