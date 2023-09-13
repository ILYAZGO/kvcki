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
    '''go to polzovateli'''
    page.locator(BUTTON_POLZOVATELI).click()
    '''button create user'''
    page.locator(BUTTON_DOBAVIT_POLZOVATELIA).click()
    '''fill required'''
    page.locator(INPUT_NAME).fill("newOne")
    page.locator(INPUT_LOGIN).fill("1createUserByManager")
    page.locator(INPUT_PASSWORD).fill(PASSWORD)
    page.locator(INPUT_EMAIL).fill("mail@mail.com")
    page.locator(INPUT_COMMENT).fill("someComment")
    page.locator(SELECT_ROLE).locator("svg").click()
    page.locator(SELECT_ROLE).get_by_text("Компания", exact=True).click()
    '''stt'''
    page.locator(SELECT_LANGUAGE).click()
    page.get_by_text("Русский", exact=True).click()
    '''stt engine'''
    page.locator(SELECT_ENGINE).click()
    page.get_by_text("IMOT.IO", exact=True).click()
    '''stt model'''
    page.locator(SELECT_MODEL).click()
    page.get_by_text("Стандарт", exact=True).click()
    '''press dobavit'''
    page.locator(BUTTON_DOBAVIT).click()
    '''go to profile'''
    page.get_by_text("newOne", exact=True).click(timeout=wait_until_visible)
    ''''''
    expect(page.locator(INPUT_LOGIN)).to_have_value("1createUserByManager", timeout=wait_until_visible)
    expect(page.locator(INPUT_NAME)).to_have_value("newOne", timeout=wait_until_visible)
    expect(page.locator(INPUT_EMAIL)).to_have_value("mail@mail.com", timeout=wait_until_visible)
    expect(page.get_by_text("Компания")).to_have_count(1, timeout=wait_until_visible)

    '''delete user'''
    page.locator(BUTTON_KORZINA).click()
    page.locator(BUTTON_PODTVERDIT).click()

    expect(page.locator(INPUT_LOGIN)).to_have_value("3managerIM", timeout=wait_until_visible)