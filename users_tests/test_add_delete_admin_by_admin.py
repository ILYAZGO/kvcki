from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
import pytest
import time

@pytest.mark.users
def test_example(page: Page) -> None:
    page.goto("http://192.168.10.101/feature-dev-951/ru", timeout = timeout)
    '''login'''
    auth(ADMIN, PASSWORD, page)
    '''go to polzovateli'''
    page.locator("#root > div > div.AdminBar_root__ieqog > a").click()
    '''button create user'''
    page.locator(".header-left-flex [tabindex]").click()
    '''fill required'''
    page.locator(".MuiInputBase-colorPrimary.MuiInputBase-root.css-upw9vt.input > input[name='name']").fill("someName")
    page.locator(".MuiInputBase-colorPrimary.MuiInputBase-root.css-upw9vt.input > input[name='login']").fill("1createAdminByAdmin")
    page.locator(".MuiInputBase-colorPrimary.MuiInputBase-root.css-upw9vt.input > input[name='password']").fill(PASSWORD)
    page.locator(".MuiInputBase-colorPrimary.MuiInputBase-root.css-upw9vt.input > input[name='email']").fill("mail@mail.com")
    page.locator("textarea[name='comment']").fill("someComment")
    page.locator("//html/body/div[2]/div[3]/div/div/div[2]/form/fieldset/div[1]/div[5]/div[2]/div/div/div[1]/div[2]/input").fill("Администратор")
    '''press enter'''
    page.keyboard.press("Enter")
    '''press dobavit'''
    page.locator(".users_form__footer__BA3ft [tabindex='0']:nth-of-type(2)").click()
    '''go to profile'''
    page.get_by_text("1createAdminByAdmin").click()
    time.sleep(2)
    ''''''
    expect(page.locator(".MuiInputBase-colorPrimary.MuiInputBase-root.css-upw9vt.input > input[name='login']")).to_have_value("1createAdminByAdmin")
    expect(page.locator(".MuiInputBase-colorPrimary.MuiInputBase-root.css-upw9vt.input > input[name='name']")).to_have_value("someName")
    expect(page.locator(".MuiInputBase-colorPrimary.MuiInputBase-root.css-upw9vt.input > input[name='email']")).to_have_value("mail@mail.com")
    expect(page.locator('//*[@id="root"]/div/div[2]/div[2]/div/div[1]/div/div[1]/p[1]')).to_have_text("someName")
    expect(page.locator('//*[@id="root"]/div/div[2]/div[2]/div/div[1]/div/div[1]/p[2]')).to_have_text("1createAdminByAdmin")
    expect(page.get_by_text("Администратор")).to_have_count(1)



    '''delete user'''
    page.locator(".styles_menu__tIMGQ svg").click()  # korzina
    page.locator(".FooterButtons_footer__ZUsFp [tabindex='0']:nth-of-type(2)").click()  # podtverdit

    expect(page.locator(".MuiInputBase-colorPrimary.MuiInputBase-root.css-upw9vt.input > input[name='login']")).to_have_value("4adminIM")