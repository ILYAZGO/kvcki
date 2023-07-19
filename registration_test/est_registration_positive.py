from playwright.sync_api import Page, expect
from utils.variables import *


def test_example(page: Page) -> None:
    page.goto(URL)
    page.locator(".MuiButton-outlined").click()
    page.get_by_label("Ваше имя").fill(REGISTRATION_NAME)
    page.get_by_label("Email").fill(REGISTRATION_EMAIL)
    page.locator("input[type=\"tel\"]").fill(REGISTRATION_PHONE)
    page.get_by_role("button", name="Отправить").click()
    expect(page.get_by_text("Вы успешно зарегистрировались")).to_be_visible()