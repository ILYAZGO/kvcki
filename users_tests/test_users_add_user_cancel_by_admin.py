from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
import pytest


@pytest.mark.users
def test_example(page: Page) -> None:
    page.goto("http://192.168.10.101/feature-dev-951/ru", timeout = timeout)
    '''login'''
    auth(ADMIN, PASSWORD, page)
    '''go to polzovateli'''
    page.locator("#root > div > div.AdminBar_root__ieqog > a").click()
    '''button create user'''
    page.locator(".header-left-flex [tabindex]").click()
    '''cancel by button CANCEL'''
    page.locator(".users_form__footer__BA3ft [tabindex='0']:nth-of-type(1)").click()
    '''check'''
    expect(page.get_by_text("Пароль")).not_to_be_visible()
    '''button create user'''
    page.locator(".header-left-flex [tabindex]").click()
    '''cancel by button KRESTIK'''
    page.get_by_test_id("CloseIcon").click()
    '''check'''
    expect(page.get_by_text("Пароль")).not_to_be_visible()