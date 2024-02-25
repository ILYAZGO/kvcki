from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.settings import *
from utils.create_delete_user import create_user, delete_user
import pytest


# input text to address-book, save, check that text saved
@pytest.mark.settings
def test_example(page: Page) -> None:
    # create admin
    USER_ID_ADMIN, TOKEN_ADMIN, LOGIN_ADMIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)
    # create user for import
    USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    page.goto(URL, timeout=timeout)

    auth(LOGIN_ADMIN, PASSWORD, page)

    '''go to the user to import'''
    page.locator(USERS_LIST).fill(LOGIN_USER)
    page.wait_for_timeout(2000)
    page.get_by_text(LOGIN_USER, exact=True).click()
    page.wait_for_timeout(6000)

    click_settings(page)


    page.locator('[href*="settings/quotas"]').click()
    page.get_by_role("button", name="Добавить").click()
    page.locator('[aria-label="Checkbox demo"]').click()
    page.locator('[name="time"]').clear()
    page.locator('[name="time"]').fill("100")
    page.get_by_role("button", name="Добавить", exact=True).click()

    page.wait_for_selector('[aria-rowindex="2"]')

    expect(page.locator('[role="gridcell"]')).to_have_count(6)
    expect(page.locator('[aria-rowindex="2"]').locator('[aria-colindex="4"]')).to_have_text("Бессрочно")

    page.locator('[fill="#FF4D4F"]').click()

    expect(page.locator('[class="rs-table-body-info"]')).to_have_text("Информация отсутствует")

    page.locator('[href*="settings/profile"]').click()
    page.locator('[href*="settings/quotas"]').click()

    page.get_by_role("button", name="Добавить").click()

    choose_preiod_date("30/12/2024", "31/12/2024", page)

    page.locator('[name="time"]').clear()
    page.locator('[name="time"]').fill("100")

    page.get_by_role("button", name="Добавить", exact=True).click()

    page.wait_for_selector('[aria-rowindex="2"]')

    expect(page.locator('[role="gridcell"]')).to_have_count(6)
    expect(page.locator('[aria-rowindex="2"]').locator('[aria-colindex="4"]')).to_have_text("2024-12-30 - 2024-12-31")


    # delete admin
    delete_user(API_URL, TOKEN_ADMIN, USER_ID_ADMIN)
    # delete user
    delete_user(API_URL, TOKEN_USER, USER_ID_USER)
