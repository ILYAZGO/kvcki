from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
import pytest

@pytest.mark.integration
def test_example(page: Page) -> None:
    page.goto("http://192.168.10.101/feature-dev-951/ru", timeout = timeout)
    '''login'''
    auth(ADMIN, PASSWORD, page)
    '''go to polzovateli'''
    page.locator("#root > div > div.AdminBar_root__ieqog > a").click()
    '''button create user'''
    page.locator(".header-left-flex [tabindex]").click()
    '''fill required'''
    page.locator(".MuiInputBase-colorPrimary.MuiInputBase-root.css-upw9vt.input > input[name='name']").fill("usedeskTest")
    page.locator(".MuiInputBase-colorPrimary.MuiInputBase-root.css-upw9vt.input > input[name='login']").fill("usedesk")
    page.locator(".MuiInputBase-colorPrimary.MuiInputBase-root.css-upw9vt.input > input[name='password']").fill(PASSWORD)
    page.locator("//html/body/div[2]/div[3]/div/div/div[2]/form/fieldset/div[1]/div[5]/div[2]/div/div/div[1]/div[2]/input").fill("Пользователь")
    '''press enter'''
    page.keyboard.press("Enter")
    '''press dobavit'''
    page.locator(".users_form__footer__BA3ft [tabindex='0']:nth-of-type(2)").click()
    page.reload()
    '''go to created user'''
    page.locator("#react-select-2-input").fill("usedeskTest")
    page.get_by_text("usedeskTest", exact=True).click()
    '''go to nastroiki'''
    page.locator('//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/button[4]').click()
    '''go to integracii'''
    page.locator("a:nth-of-type(7) > .MuiTypography-body1.MuiTypography-root.css-pd9d9b.styles_menuItemText__rYDh4").click()
    '''podklu4it'''
    page.locator(".styles_goToIntegrationsList__KXaHU").click()
    '''choose usedesk'''
    page.locator('//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[21]/div[2]/button').click()
    '''input token'''
    page.locator('//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/input').fill(USEDESK_TOKEN)
    '''save'''
    page.get_by_test_id("AccessKeysTab_submit").click()
    '''go to parametri'''
    page.locator("div[role='tablist'] > a:nth-of-type(2)").click()





    '''delete user'''
    page.locator(".styles_menu__tIMGQ svg").click() # korzina
    page.locator(".FooterButtons_footer__ZUsFp [tabindex='0']:nth-of-type(2)").click() # podtverdit



