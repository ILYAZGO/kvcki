from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.markup import *
import pytest

'''Create tag in group and outside group'''


@pytest.mark.rules
def test_example(page: Page) -> None:
    fill = "QWERTY"
    page.goto(URL, timeout=timeout)
    '''login'''
    auth(ADMIN, PASSWORD, page)
    '''go to razmetka'''
    page.locator(BUTTON_RAZMETKA).click()

    '''pre clean'''
    if page.get_by_text("Неотсортированные").is_visible():
        page.get_by_text("66666").click()
        page.locator(".css-izdlur").click()
        page.get_by_text("Удалить", exact=True).click()
        page.get_by_role("button", name="Удалить").click()
        page.locator(
            "//html/body/div/div/div/div[2]/div/div/div[1]/div[1]/div[3]/div/div/div[2]/div/div[1]/div[2]/div[2]/div/button").click()
    else:
        pass

    '''create group'''
    page.get_by_test_id(BUTTON_DOBAVIT_TEG).click()
    page.get_by_test_id(INPUT_NAZVANIE_GRUPPI).type("66666")
    page.keyboard.press('Enter')  # kostil'
    # page.get_by_test_id("markup_newRuleApply").click() #otpravit
    '''check'''
    expect(page.locator(
        '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[1]/div/div[1]/div/div[2]/div/input')).to_have_value("66666")  # check rule
    # expect(page.get_by_text("Неотсортированные")).to_have_count(count=2)  # po4emu to valitsa
    ''''teardown'''
    page.locator(".css-izdlur").click()
    page.get_by_text("Удалить", exact=True).click()
    page.get_by_role("button", name="Удалить").click()
    page.locator("//html/body/div/div/div/div[2]/div/div/div[1]/div[1]/div[3]/div/div/div[2]/div/div[1]/div[2]/div[2]/div/button").click()
    '''check teardown'''
    expect(page.get_by_text("Неотсортированные")).not_to_be_visible()
