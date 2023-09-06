from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.markup import *
from utils.create_delete_user import create_user, delete_user
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
    USER_ID, BEARER, ACCESS_TOKEN, LOGIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    page.goto(URL, timeout=timeout)
    '''login'''
    auth(LOGIN, PASSWORD, page)

    '''type in users list "import" and choose user "importTo"'''
    page.locator("#react-select-2-input").fill("2import")
    page.get_by_text("2importTo", exact=True).click()
    time.sleep(2)

    '''going to Razmetka/slovari and click Importirovat slovari'''
    page.locator(BUTTON_RAZMETKA).click()
    page.wait_for_timeout(3000)
    page.locator(BUTTON_SLOVARI).click()
    page.locator(BUTTON_IMPORTIROVAT_SLOVARI).click()
    page.wait_for_selector(INPUT_CHOOSE_USER_FOR_IMPORT)
    '''type in users list "importFrom" and choose user "importFrom"'''
    page.locator(INPUT_CHOOSE_USER_FOR_IMPORT).fill("importFrom")
    time.sleep(3)
    page.get_by_text("importFrom", exact=True).click()
    time.sleep(3)

    '''click to switch button to import group of dict and dict'''
    page.locator("(//input[@type='checkbox'])[3]").click()
    time.sleep(1)
    page.get_by_role("button", name="Продолжить").click()
    time.sleep(1)
    page.locator("(//input[@type='checkbox'])[6]").click()
    time.sleep(1)
    page.get_by_role("button", name="К новым правилам").click()
    time.sleep(2)

    '''check that import successful'''
    expect(page.locator("//p[normalize-space()='44444']")).to_be_visible(timeout=wait_until_visible)
    #expect(page.get_by_text("44444")).to_be_visible(timeout=wait_until_visible)
    expect(page.get_by_text("55555")).to_be_visible(timeout=wait_until_visible)
    expect(page.get_by_text("66666")).to_be_visible(timeout=wait_until_visible)
    expect(page.get_by_text("Неотсортированные")).to_be_visible(timeout=wait_until_visible)
    expect(page.get_by_text("1 словарь")).to_have_count(count=2, timeout=wait_until_visible)

    '''teardown'''
    page.get_by_text("55555").click()
    page.locator(".css-izdlur").click()
    page.get_by_text("Удалить", exact=True).click()
    page.get_by_role("button", name="Удалить").click()
    page.get_by_text("66666").click()
    page.locator(".css-izdlur").click()
    page.get_by_text("Удалить", exact=True).click()
    page.get_by_role("button", name="Удалить").click()
    page.locator("(//button[@type='button'])[15]").click()
    time.sleep(1)
    page.locator("(//button[@type='button'])[15]").click()
    '''check teardown'''
    expect(page.locator("//p[normalize-space()='44444']")).not_to_be_visible(timeout=wait_until_visible)
    #expect(page.get_by_text("44444")).not_to_be_visible(timeout=wait_until_visible)
    expect(page.get_by_text("55555")).not_to_be_visible(timeout=wait_until_visible)
    expect(page.get_by_text("66666")).not_to_be_visible(timeout=wait_until_visible)
    expect(page.get_by_text("Неотсортированные")).not_to_be_visible(timeout=wait_until_visible)

    delete_user(API_URL, USER_ID, BEARER, ACCESS_TOKEN)
