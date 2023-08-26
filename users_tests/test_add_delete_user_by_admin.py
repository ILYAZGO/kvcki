from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.users import *
from utils.create_delete_user import create_user, delete_user
import pytest
import time

@pytest.mark.users
def test_example(page: Page) -> None:
    USER_ID, BEARER, ACCESS_TOKEN, LOGIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    page.goto(URL, timeout=timeout)
    '''login'''
    auth(LOGIN, PASSWORD, page)
    '''go to polzovateli'''
    page.get_by_test_id(BUTTON_POLZOVATELI).click()
    '''button create user'''
    page.get_by_test_id(BUTTON_DOBAVIT_POLZOVATELIA).click()
    '''fill required'''
    page.locator(INPUT_NAME).fill("someName")
    page.locator(INPUT_LOGIN).fill("1createUserByAdmin")
    page.locator(INPUT_PASSWORD).fill(PASSWORD)
    page.locator(INPUT_EMAIL).fill("mail@mail.com")
    page.locator(INPUT_COMMENT).fill("someComment")
    page.locator(CHOOSE_ROLE).fill("Компания")
    '''press enter'''
    page.keyboard.press("Enter")
    #'''stt'''
    #page.locator("//html/body/div[2]/div[3]/div/div/div[2]/form/fieldset[2]/div/div[1]/div[2]/div/div/div[1]/div[2]/input").click()
    #page.get_by_text("Русский").click()
    #'''stt engine'''
    #page.locator("//html/body/div[2]/div[3]/div/div/div[2]/form/fieldset[2]/div/div[2]/div[2]/div/div/div[1]/div[2]/input").click()
    #time.sleep(2)
    #page.get_by_text("Яндекс").click()
    #'''stt model'''
    #page.locator("//html/body/div[2]/div[3]/div/div/div[2]/form/fieldset[2]/div/div[3]/div[2]/div/div/div[1]/div[2]/input").click()
    #page.get_by_text("Обобщённая").click()

    # '''add quota'''
    # page.locator(INPUT_QUOTA).fill("60")

    '''press dobavit'''
    page.get_by_test_id(BUTTON_DOBAVIT).click()
    time.sleep(10)
    '''check quota'''
    #expect(page.get_by_text("60")).to_be_visible()
    '''go to profile'''
    page.locator("//div[contains(text(),'1createUserByAdmin')]").click()
    '''check'''
    expect(page.locator(INPUT_LOGIN)).to_have_value("1createUserByAdmin", timeout=wait_until_visible)
    expect(page.locator(INPUT_NAME)).to_have_value("someName", timeout=wait_until_visible)
    expect(page.locator(INPUT_EMAIL)).to_have_value("mail@mail.com", timeout=wait_until_visible)
    expect(page.get_by_text("Компания")).to_have_count(1, timeout=wait_until_visible)

    '''delete user'''
    page.locator(BUTTON_KORZINA).click()
    page.locator(BUTTON_PODTVERDIT).click()

    expect(page.locator(INPUT_LOGIN)).to_have_value(LOGIN, timeout=wait_until_visible)

    delete_user(API_URL, USER_ID, BEARER, ACCESS_TOKEN)