from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.markup import *
from utils.create_delete_user import create_user, delete_user, give_user_to_manager
import pytest
import allure


@pytest.mark.independent
@pytest.mark.dictionaries
@allure.title("test_add_dict_inside_group")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Create dict inside group by user")
def test_add_dict_inside_group(page: Page) -> None:

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)

    with allure.step("Auth with user"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to dicts"):
        go_to_dicts(page)

    with allure.step("Create group"):
        create_group("12345", page)

    with allure.step("Click on group"):
        page.locator(CLICK_ON_GROUP).click()

    with allure.step("Create dict"):
        create_dict("98765", page)

    with allure.step("Check that dict created"):
        expect(page.locator(NAZVANIE_SLOVARYA)).to_have_value("98765")

    with allure.step("Check that dict belongs to parent group"):
        expect(page.get_by_text("12345").nth(1)).to_have_text("12345")
        page.wait_for_timeout(300)

    with allure.step("Rename dict"):
        page.locator(NAZVANIE_SLOVARYA).clear()
        page.locator(NAZVANIE_SLOVARYA).fill("newName")
        page.get_by_role("button", name="Сохранить").click()
        page.wait_for_timeout(1000)

    with allure.step("Check that name changed"):
        expect(page.locator(NAZVANIE_SLOVARYA)).to_have_value("newName")
        expect(page.locator('[data-testid="test"]')).to_have_text("newName")

    with allure.step("Delete dict and group"):
        delete_group_and_rule_or_dict(page)

    with allure.step("Check that group deleted (group will not be delete if you didnt delete dict)"):
        expect(page.get_by_text("12345")).not_to_be_visible()

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


