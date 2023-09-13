from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.users import *
from utils.create_delete_user import create_user, delete_user
import pytest


@pytest.mark.users
def test_example(page: Page) -> None:
    USER_ID, BEARER, ACCESS_TOKEN, LOGIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    page.goto(URL, timeout=timeout)
    '''login'''
    auth(LOGIN, PASSWORD, page)
    '''go to polzovateli'''
    page.locator(BUTTON_POLZOVATELI).click()
    '''button create user'''
    page.locator(BUTTON_DOBAVIT_POLZOVATELIA).click()
    '''fill required'''
    page.locator(INPUT_NAME).fill("newManager")
    page.locator(INPUT_LOGIN).fill("1createManagerByAdmin")
    page.locator(INPUT_PASSWORD).fill(PASSWORD)
    page.locator(INPUT_EMAIL).fill("mail@mail.com")
    page.locator(INPUT_COMMENT).fill("someComment")
    page.locator(SELECT_ROLE).locator("svg").click()
    page.locator(SELECT_ROLE).get_by_text("Интегратор", exact=True).click()
    '''press dobavit'''
    page.locator(BUTTON_DOBAVIT).click()
    page.wait_for_timeout(4000)
    '''go to profile'''
    page.get_by_text("newManager", exact=True).click(timeout=wait_until_visible)
    '''check'''
    expect(page.locator(INPUT_LOGIN)).to_have_value("1createManagerByAdmin", timeout=wait_until_visible)
    expect(page.locator(INPUT_NAME)).to_have_value("newManager", timeout=wait_until_visible)
    expect(page.locator(INPUT_EMAIL)).to_have_value("mail@mail.com", timeout=wait_until_visible)
    expect(page.get_by_text("Интегратор")).to_have_count(2, timeout=wait_until_visible)  #slovalos potomu 4to noviy punkt menu
    page.wait_for_timeout(2000)
    '''delete user'''
    page.locator(BUTTON_KORZINA).click()
    page.locator(BUTTON_PODTVERDIT).click()
    expect(page.locator(INPUT_LOGIN)).to_have_value(LOGIN, timeout=wait_until_visible)

    delete_user(API_URL, USER_ID, BEARER, ACCESS_TOKEN)