from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.markup import *
import time
import pytest

'''
Precondition
user  importFrom 
with group 11111 rule 22222 inside
with rule 33333 without group
user  importTo
'''
@pytest.mark.rules
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    auth(MANAGER, PASSWORD, page)

    '''type in users list "import" and choose user "importTo"'''
    page.locator("#react-select-2-input").fill("import")
    time.sleep(2)
    page.get_by_text("importTo", exact=True).click()
    time.sleep(4)


    '''going to Razmetka and click Importirovat Pravila'''
    page.locator(BUTTON_RAZMETKA).click()
    time.sleep(2)
    page.locator(BUTTON_IMPORTIROVAT_PRAVILA).click()
    time.sleep(2)
    '''type in users list "importFrom" and choose user "importFrom"'''
    page.locator(INPUT_CHOOSE_USER_FOR_IMPORT).fill("importFrom")
    time.sleep(4)
    page.get_by_text("importFrom", exact=True).click()
    time.sleep(2)

    '''click to switch button to import group with rule'''
    page.locator("(//input[@type='checkbox'])[3]").click()
    time.sleep(1)
    page.get_by_role("button", name="Продолжить").click()
    time.sleep(1)
    '''click to import rule'''
    page.locator("(//input[@type='checkbox'])[5]").click()
    time.sleep(1)
    page.get_by_role("button", name="К новым правилам").click()
    time.sleep(2)
    '''check that import successful'''
    expect(page.get_by_text("11111")).to_be_visible(timeout=wait_until_visible)
    expect(page.get_by_text("22222")).to_be_visible(timeout=wait_until_visible)
    expect(page.get_by_text("33333")).to_be_visible(timeout=wait_until_visible)
    expect(page.get_by_text("Неотсортированные")).to_be_visible(timeout=wait_until_visible)
    expect(page.get_by_text("1 тег")).to_have_count(count=2, timeout=wait_until_visible)

    '''teardown'''
    page.get_by_text("22222").click()
    page.locator(".css-izdlur").click()
    page.get_by_text("Удалить", exact=True).click()
    page.get_by_role("button", name="Удалить").click()
    page.get_by_text("33333").click()
    page.locator(".css-izdlur").click()
    page.get_by_text("Удалить", exact=True).click()
    page.get_by_role("button", name="Удалить").click()
    page.locator("(//button[@type='button'])[15]").click()
    time.sleep(1)
    page.locator("(//button[@type='button'])[15]").click()

    '''check teardown'''
    expect(page.get_by_text("11111")).not_to_be_visible(timeout=wait_until_visible)
    expect(page.get_by_text("22222")).not_to_be_visible(timeout=wait_until_visible)
    expect(page.get_by_text("33333")).not_to_be_visible(timeout=wait_until_visible)
    time.sleep(1)
    expect(page.get_by_text("Неотсортированные")).not_to_be_visible(timeout=wait_until_visible)