from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.settings import *
from utils.create_delete_user import create_user, delete_user, create_operator
import pytest


# check admin can change personal info for operator and save
@pytest.mark.independent
@pytest.mark.settings
def test_example(page: Page) -> None:

    NEW_OPERATOR_NAME = NEW_OPERATOR_LOGIN = f"auto_test_operator_{datetime.now().strftime('%m%d%H%M')}_{datetime.now().microsecond}"
    EMAIL = f"email_{datetime.now().microsecond}{random.randint(100, 999)}@mail.ru"

    USER_ID_ADMIN, TOKEN_ADMIN, LOGIN_ADMIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)
    USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)
    USER_ID_OPERATOR, TOKEN_OPERATOR, LOGIN_OPERATOR = create_operator(API_URL, USER_ID_USER, PASSWORD)

    page.goto(URL, timeout=timeout)

    auth(LOGIN_ADMIN, PASSWORD, page)

    go_to_user(LOGIN_USER, page)

    click_settings(page)

    click_employees(page)

    go_to_operator_from_table(page)

    fill_personal_information_admin_and_manager(NEW_OPERATOR_NAME, EMAIL, "1234567890", "someComment", "Africa/Bamako", page)

    press_save(page)

    click_rights(page)

    click_personal_info(page)

    expect(page.locator('[class*="LeftMenuLayout_content"]')).not_to_contain_text("Редактировать ")
    expect(page.locator(INPUT_NAME)).to_have_value(NEW_OPERATOR_NAME)
    expect(page.locator(INPUT_EMAIL)).to_have_value(EMAIL)
    expect(page.locator(INPUT_PHONE)).to_have_value("1234567890")
    expect(page.locator(INPUT_COMMENT)).to_have_value("someComment")
    expect(page.get_by_text("Africa/Bamako")).to_be_visible()
    expect(page.locator('[data-testid="selectIndustry"]')).not_to_be_visible()
    expect(page.locator('[data-testid="selectPartner"]')).not_to_be_visible()

    page.reload()
    page.wait_for_selector(INPUT_NAME)
    page.wait_for_timeout(300)

    expect(page.locator('[class*="LeftMenuLayout_content"]')).not_to_contain_text("Редактировать ")
    expect(page.locator(INPUT_NAME)).to_have_value(NEW_OPERATOR_NAME)
    expect(page.locator(INPUT_EMAIL)).to_have_value(EMAIL)
    expect(page.locator(INPUT_PHONE)).to_have_value("1234567890")
    expect(page.locator(INPUT_COMMENT)).to_have_value("someComment")
    expect(page.get_by_text("Africa/Bamako")).to_be_visible()
    expect(page.locator('[data-testid="selectIndustry"]')).not_to_be_visible()
    expect(page.locator('[data-testid="selectPartner"]')).not_to_be_visible()

    delete_user(API_URL, TOKEN_ADMIN, USER_ID_ADMIN)
    delete_user(API_URL, TOKEN_USER, USER_ID_USER)
    delete_user(API_URL, TOKEN_OPERATOR, USER_ID_OPERATOR)

