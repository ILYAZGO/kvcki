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
@pytest.mark.dictionaries
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    auth(ADMIN, PASSWORD, page)

    '''type in users list "import" and choose user "importTo"'''
    page.locator("#react-select-2-input").fill("import")
    page.get_by_text("importTo", exact=True).click()

    '''going to Razmetka/slovari and click Importirovat slovari'''
    page.locator(BUTTON_RAZMETKA).click()
    page.get_by_test_id(BUTTON_SLOVARI).click()
    page.get_by_test_id(BUTTON_IMPORTIROVAT_SLOVARI).click()

    '''type in users list "importFrom" and choose user "importFrom"'''
    page.locator("//html/body/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div/div/div/div[1]/div[2]/input").fill("importFrom")
    page.get_by_text("importFrom", exact=True).click()

    '''click to switch button to import group of dict and dict'''
    page.locator("//html/body/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div/div/span/input").click()
    page.get_by_role("button", name="Продолжить").click()
    page.locator("//html/body/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div/span/input").click()
    time.sleep(1)
    page.get_by_role("button", name="К новым правилам").click()

    '''check that import successful'''
    expect(page.get_by_text("44444")).to_be_visible()
    expect(page.get_by_text("55555")).to_be_visible()
    expect(page.get_by_text("66666")).to_be_visible()
    expect(page.get_by_text("Неотсортированные")).to_be_visible()
    expect(page.get_by_text("1 словарь")).to_have_count(count=2)

    '''teardown'''
    page.get_by_text("55555").click()
    page.locator(".css-izdlur").click()
    page.get_by_text("Удалить", exact=True).click()
    page.get_by_role("button", name="Удалить").click()
    page.get_by_text("66666").click()
    page.locator(".css-izdlur").click()
    page.get_by_text("Удалить", exact=True).click()
    page.get_by_role("button", name="Удалить").click()
    page.locator('//*[@id="root"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/button').click()
    page.locator('//*[@id="root"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[3]/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/button').click()

    '''check teardown'''
    expect(page.get_by_text("44444")).not_to_be_visible()
    expect(page.get_by_text("55555")).not_to_be_visible()
    expect(page.get_by_text("66666")).not_to_be_visible()
    expect(page.get_by_text("Неотсортированные")).not_to_be_visible()