from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.markup import *
import pytest
import time


@pytest.mark.dictionaries
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    auth(ADMIN, PASSWORD, page)
    '''go to razmetka'''
    page.locator(BUTTON_RAZMETKA).click()
    '''go to slovari'''
    page.get_by_test_id(BUTTON_SLOVARI).click()
    time.sleep(2)
    '''pre clean'''
    if page.get_by_text("Неотсортированные").is_visible():
        page.get_by_text("77777").click()
        page.locator(".css-izdlur").click()
        page.get_by_text("Удалить", exact=True).click()
        page.get_by_role("button", name="Удалить").click()
        page.locator(BUTTON_KORZINA).click()
    else:
        pass

    '''create dict outside group'''
    page.get_by_test_id(BUTTON_DOBAVIT_SLOVAR).click()
    page.locator(INPUT_NAZVANIE_SLOVAR).fill("77777")
    page.get_by_role('button', name="Отправить").click()
    '''check created dict outside group'''
    expect(page.locator(NAZVANIE_SLOVARYA)).to_have_value("77777")
    '''check created dict parent'''
    expect(page.get_by_text("Unsorted")).to_have_text("Unsorted")
    page.reload()
    expect(page.get_by_text("Неотсортированные")).to_have_count(count=2)  # проверяем что таких надписей две (слева и внутри словаря)

    '''teardown'''
    page.locator(".css-izdlur").click()
    page.get_by_text("Удалить", exact=True).click()
    page.get_by_role("button", name="Удалить").click()
    page.locator(BUTTON_KORZINA).click()
    '''check teardown'''
    expect(page.get_by_text("Неотсортированные")).not_to_be_visible()
