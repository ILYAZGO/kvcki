#from playwright.sync_api import Page, expect, BrowserContext, sync_playwright, Playwright, Route
from utils.variables import *
from pages.deals import *
import pytest
from utils.dates import today
from utils.create_delete_user import create_user, delete_user, give_users_to_manager, create_operator, give_access_right
import allure


@pytest.mark.e2e
@pytest.mark.deals
@allure.title("test_deal")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_deal")
def test_deal(base_url, page: Page, context: BrowserContext) -> None:
    deals = Deals(page)

    with allure.step("Create admin"):
        USER_ID_ADMIN, TOKEN_ADMIN, LOGIN_ADMIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD, upload_call=True, deal_check_list=True)

    with allure.step("Go to url"):
        deals.navigate("http://192.168.10.101/feature-dev-3474/")

    with allure.step("Auth with admin"):
        deals.auth(LOGIN_ADMIN, PASSWORD)

    with allure.step("Go to user"):
        deals.go_to_user(LOGIN_USER)

    with allure.step("Go to deals"):
        deals.click_deals()

    with allure.step("Check deal in list"):
        expect(deals.deals_found).to_have_text("Найдено сделок 1 из 1")
        expect(page.get_by_text("0987654321")).to_have_count(1)
        expect(deals.deal_date).to_contain_text(today.strftime("%d.%m.%Y"))
        expect(deals.communications_count).to_have_text("1")
        expect(deals.score_percent).to_have_text("90%")
        expect(deals.deal_score).to_have_text("90 баллов")

    with allure.step("Open new tab"):
        with context.expect_page() as new_tab_event:
            deals.button_share_call.click()
            new_tab=new_tab_event.value

    with allure.step("Check"):
        new_tab.wait_for_timeout(2000)
        new_tab.wait_for_selector('[alt="Imot.io loader"]', state="hidden")
        new_tab.wait_for_timeout(2000)
        new_tab_deal = Deals(new_tab)

        # expect(new_tab_deal.deal_date).to_contain_text(today.strftime("%d.%m.%Y"))
        # expect(new_tab_deal.communications_count).to_have_text("1")
        # expect(new_tab_deal.score_percent).to_have_text("90%")
        # expect(new_tab_deal.deal_score).to_have_text("90 баллов")
        expect(new_tab.locator('[aria-label="Перетегировать"]')).to_have_count(1)
        expect(new_tab_deal.button_calls_list_download).to_have_count(1)

    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN_ADMIN, USER_ID_ADMIN)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)