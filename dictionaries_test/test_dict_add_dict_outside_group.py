from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.markup import *
import pytest


@pytest.mark.dictionaries
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    auth(ADMIN, PASSWORD, page)
    '''create dict outside group'''
    page.locator(BUTTON_RAZMETKA).click()
    page.get_by_test_id(BUTTON_SLOVARI).click()
    page.locator("//html/body/div/div/div/div[2]/div/div/div[1]/div[1]/div[3]/div/div/div[1]").click()
    page.locator("//html/body/div/div/div/div[2]/div/div/div[1]/div[2]/div[1]/div/button").click()
    page.locator(INPUT_NEW_GROUP_NAME).fill("77777")
    page.get_by_role('button', name="Отправить").click()
    '''check created dict outside group'''
    expect(page.locator(
        '//*[@id="root"]/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/div/input')).to_have_value("77777")
    '''check created dict parent'''
    expect(page.get_by_text("Unsorted")).to_have_text("Unsorted")
    page.reload()
    expect(page.get_by_text("Неотсортированные")).to_have_count(
        count=2)  # проверяем что таких надписей две (слева и внутри словаря)

    '''teardown'''
    page.locator(".css-izdlur").click()
    page.get_by_text("Удалить", exact=True).click()
    page.get_by_role("button", name="Удалить").click()
    page.locator(
        "//html/body/div/div/div/div[2]/div/div/div[1]/div[1]/div[3]/div/div/div[2]/div/div[1]/div[2]/div[2]/div/button").click()
    '''check teardown'''
    expect(page.get_by_text("Неотсортированные")).not_to_be_visible()
