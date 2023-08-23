from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.users import *
import pytest
import time

@pytest.mark.users
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    auth(ADMIN, PASSWORD, page)
    '''go to polzovateli'''
    page.get_by_test_id(BUTTON_POLZOVATELI).click()
    '''button create user'''
    page.get_by_test_id(BUTTON_DOBAVIT_POLZOVATELIA).click()
    '''fill required'''
    page.locator(INPUT_NAME).fill("someName")
    page.locator(INPUT_LOGIN).fill("1createManagerByAdmin")
    page.locator(INPUT_PASSWORD).fill(PASSWORD)
    page.locator(INPUT_EMAIL).fill("mail@mail.com")
    page.locator(INPUT_COMMENT).fill("someComment")
    page.locator(CHOOSE_ROLE).fill("Интегратор")
    '''press enter'''
    page.keyboard.press("Enter")
    '''press dobavit'''
    page.get_by_test_id(BUTTON_DOBAVIT).click()
    time.sleep(2)
    '''go to profile'''
    page.get_by_text("someName", exact=True).click(timeout=wait_until_visible)
    '''check'''
    expect(page.locator(INPUT_LOGIN)).to_have_value("1createManagerByAdmin", timeout=wait_until_visible)
    expect(page.locator(INPUT_NAME)).to_have_value("someName", timeout=wait_until_visible)
    expect(page.locator(INPUT_EMAIL)).to_have_value("mail@mail.com", timeout=wait_until_visible)
    expect(page.get_by_text("Интегратор")).to_have_count(2, timeout=wait_until_visible)  #slovalos potomu 4to noviy punkt menu
    time.sleep(2)
    '''delete user'''
    page.locator(BUTTON_KORZINA).click()
    page.locator(BUTTON_PODTVERDIT).click()
    expect(page.locator(INPUT_LOGIN)).to_have_value("4adminIM", timeout=wait_until_visible)
