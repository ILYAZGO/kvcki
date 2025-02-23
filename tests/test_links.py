from playwright.sync_api import Page, expect
from utils.variables import *
from pages.links import *
import pytest
from utils.create_delete_user import create_user, delete_user, give_user_to_manager, create_operator
import allure


@pytest.mark.e2e
@pytest.mark.links
@allure.title("test_send_link_to_admin_not_logged")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("Sending link to admin, that not logged in system")
def test_send_link_to_admin_not_logged(base_url, page) -> None:
    links = Links(page)
    #link = "http://192.168.10.101/feature-dev-2976/ru/6204e7cb599aff4f43f5d3a0/settings/profile"
    link = "https://app.stand.imot.io/ru/6204e7cb599aff4f43f5d3a0/settings/profile"

    with allure.step("Create admin"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    with allure.step("Go to link and get auth page"):
        links.navigate(link)

    with allure.step("Login with admin"):
        links.auth(LOGIN, PASSWORD)

    with allure.step("Check that after login we going directly to link"):
        links.assert_url(link)

    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN, USER_ID)


# need same test for user , manager and operator, but later.
# For now we dont care what will happen https://task.imot.io/browse/DEV-3331