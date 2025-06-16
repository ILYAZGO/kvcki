from utils.variables import *
from pages.deals import *
import pytest
from utils.create_delete_user import create_user, delete_user, give_users_to_manager, create_operator, give_access_right
import allure


@pytest.mark.e2e
@pytest.mark.deals
@allure.title("test_deal")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_deal")
def test_deal(base_url, page: Page) -> None:
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
        #expect(deals.deal_id_block).to_contain_text("0987654321")




    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN_ADMIN, USER_ID_ADMIN)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)