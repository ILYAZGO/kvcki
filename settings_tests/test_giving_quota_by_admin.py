from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.settings import *
from utils.create_delete_user import create_user, delete_user
import pytest


# every auto_test_user gets 777 min quota by default. test check that we can add more
@pytest.mark.independent
@pytest.mark.settings
def test_example(page: Page) -> None:
    # create admin
    USER_ID_ADMIN, TOKEN_ADMIN, LOGIN_ADMIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)
    # create user
    USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    page.goto(URL, timeout=timeout)

    auth(LOGIN_ADMIN, PASSWORD, page)

    go_to_user(LOGIN_USER, page)

    click_settings(page)

    click_quota(page)

    press_add_in_quotas(page)

    expect(page.locator(INPUT_QUOTA_TIME)).to_have_value("777")

    # checkbox
    page.locator('[type="checkbox"]').click()

    expect(page.locator('[type="checkbox"]')).to_be_checked()

    # check that dates disabled
    expect(page.locator('[class*="ant-picker-disabled"]')).to_be_visible()

    fill_quota_time("100", page)

    press_add_in_quotas(page)

    #wait
    page.wait_for_selector('[aria-rowindex="2"]')

    page.reload()

    page.wait_for_selector('[aria-rowindex="2"]')

    page.wait_for_timeout(2000)

    expect(page.locator('[role="gridcell"]')).to_have_count(12)

    expect(page.locator('[aria-rowindex="2"]').locator('[aria-colindex="4"]')).to_have_text("Бессрочно")

    page.locator('[fill="#FF4D4F"]').click()

    page.wait_for_timeout(3500)

    expect(page.locator('[fill="#FF4D4F"]')).not_to_be_visible(timeout=wait_until_visible)

    #expect(page.locator('[class="rs-table-body-info"]')).to_have_text("Информация отсутствует")

    press_add_in_quotas(page)

    expect(page.locator(INPUT_QUOTA_TIME)).to_have_value("100")

    choose_preiod_date("30/12/2024", "31/12/2024", page)

    fill_quota_time("100", page)

    press_add_in_quotas(page)

    page.wait_for_selector('[aria-rowindex="2"]')

    page.reload()

    page.wait_for_selector('[aria-rowindex="2"]')

    page.wait_for_timeout(1500)

    expect(page.locator('[role="gridcell"]')).to_have_count(18)
    expect(page.locator('[aria-rowindex="2"]').locator('[aria-colindex="4"]')).to_have_text("2024-12-30 - 2024-12-31")
    page.locator('[fill="#FF4D4F"]').click()

    page.wait_for_timeout(500)

    expect(page.locator('[fill="#FF4D4F"]')).not_to_be_visible()


    # delete admin
    delete_user(API_URL, TOKEN_ADMIN, USER_ID_ADMIN)
    # delete user
    delete_user(API_URL, TOKEN_USER, USER_ID_USER)
