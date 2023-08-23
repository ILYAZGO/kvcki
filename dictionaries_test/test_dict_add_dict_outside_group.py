from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.markup import *
from utils.create_delete_user import create_user, delete_user
import pytest
import time


@pytest.mark.dictionaries
def test_example(page: Page) -> None:
    USER_ID, BEARER, ACCESS_TOKEN = create_user(API_URL, name6, login6, PASSWORD)

    page.goto(URL, timeout=timeout)
    '''login'''
    auth(login6, PASSWORD, page)
    '''go to razmetka'''
    page.locator(BUTTON_RAZMETKA).click()
    '''go to slovari'''
    page.get_by_test_id(BUTTON_SLOVARI).click()
    time.sleep(2)

    '''create dict outside group'''
    page.get_by_test_id(BUTTON_DOBAVIT_SLOVAR).click()
    page.locator(INPUT_NAZVANIE_SLOVAR).fill("77777")
    page.get_by_role('button', name="Отправить").click()
    '''check created dict outside group'''
    expect(page.locator(NAZVANIE_SLOVARYA)).to_have_value("77777", timeout=wait_until_visible)
    '''check created dict parent'''
    expect(page.get_by_text("Unsorted")).to_have_text("Unsorted")
    page.reload()
    expect(page.get_by_text("Неотсортированные")).to_have_count(count=2, timeout=wait_until_visible)  # проверяем что таких надписей две (слева и внутри словаря)

    '''teardown'''
    page.locator(".css-izdlur").click(timeout=wait_until_visible)
    page.get_by_text("Удалить", exact=True).click(timeout=wait_until_visible)
    page.get_by_role("button", name="Удалить").click(timeout=wait_until_visible)
    page.locator(BUTTON_KORZINA).click(timeout=wait_until_visible)
    '''check teardown'''
    expect(page.get_by_text("Неотсортированные")).not_to_be_visible(timeout=wait_until_visible)

    delete_user(API_URL, USER_ID, BEARER, ACCESS_TOKEN)
