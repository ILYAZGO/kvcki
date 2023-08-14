from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.users import *
import pytest
import time

@pytest.mark.users
def test_example(page: Page) -> None:
    page.goto(URL, timeout = timeout)
    '''login'''
    auth(ADMIN, PASSWORD, page)
    '''go to polzovateli'''
    page.locator(BUTTON_POLZOVATELI).click()
    '''button create user'''
    page.locator(BUTTON_DOBAVIT_POLZOVATELIA).click()
    '''fill required'''
    page.locator(INPUT_NAME).fill("someName")
    page.locator(INPUT_LOGIN).fill("1createUserByAdmin")
    page.locator(INPUT_PASSWORD).fill(PASSWORD)
    page.locator(INPUT_EMAIL).fill("mail@mail.com")
    page.locator(INPUT_COMMENT).fill("someComment")
    page.locator(CHOOSE_ROLE).fill("Пользователь")
    '''press enter'''
    page.keyboard.press("Enter")
    #'''stt'''
    #page.locator("//html/body/div[2]/div[3]/div/div/div[2]/form/fieldset[2]/div/div[1]/div[2]/div/div/div[1]/div[2]/input").click()
    #page.get_by_text("Русский").click()
    #''''''
    #page.locator("//html/body/div[2]/div[3]/div/div/div[2]/form/fieldset[2]/div/div[2]/div[2]/div/div/div[1]/div[2]/input").click()
    #time.sleep(2)
    #page.get_by_text("Happyscribe").click()
    #''''''
    #page.locator("//html/body/div[2]/div[3]/div/div/div[2]/form/fieldset[2]/div/div[3]/div[2]/div/div/div[1]/div[2]/input").click()
    #page.get_by_text("detail").click()
    '''add quota'''
    page.locator(INPUT_QUOTA).fill("60")

    '''press dobavit'''
    page.locator(BUTTON_DOBAVIT).click()
    time.sleep(1)
    '''check quota'''
    expect(page.get_by_text("00:01:00")).to_be_visible()
    '''go to profile'''
    page.locator("//div[contains(text(),'1createUserByAdmin')]").click()
    time.sleep(5)
    '''check'''
    expect(page.locator(INPUT_LOGIN)).to_have_value("1createUserByAdmin")
    expect(page.locator(INPUT_NAME)).to_have_value("someName")
    expect(page.locator(INPUT_EMAIL)).to_have_value("mail@mail.com")
    expect(page.get_by_text("Пользователь")).to_have_count(1)

    '''delete user'''
    page.locator(BUTTON_KORZINA).click()
    page.locator(BUTTON_PODTVERDIT).click()

    expect(page.locator(INPUT_LOGIN)).to_have_value("4adminIM")