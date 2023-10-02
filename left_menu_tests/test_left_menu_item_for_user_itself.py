from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.left_menu import *
from utils.create_delete_user import create_user, delete_user
import pytest


@pytest.mark.left_menu
def test_example(page: Page) -> None:
    USER_ID, BEARER, ACCESS_TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    page.goto(URL, timeout=timeout)

    auth(LOGIN, PASSWORD, page)

    click_settings(page)

    expect(page.locator(BLOCK_LEFT_MENU)).to_contain_text(['Персональная информацияСотрудникиДействия с коммуникациямиОбработка текстаКвотыАдресная книгаИнтеграции'])
    expect(page.locator(LEFT_MENU_ITEM)).to_have_count(7)

    delete_user(API_URL, USER_ID, BEARER, ACCESS_TOKEN)

