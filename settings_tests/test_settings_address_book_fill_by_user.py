from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.settings import *
from utils.create_delete_user import create_user, delete_user
import pytest


# input text to address-book, save, check that text saved
@pytest.mark.settings
def test_example(page: Page) -> None:
    USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    page.goto(URL, timeout=timeout)

    auth(LOGIN, PASSWORD, page)

    click_settings(page)

    fill_address_book_and_save("Телефон;Должность;ФИО\n12345;IVAN;BOSS", page)

    expect(page.locator(INPUT_ADDRESS_BOOK)).to_contain_text(["Телефон;Должность;ФИО\n12345;IVAN;BOSS"])

    delete_user(API_URL, TOKEN, USER_ID)

