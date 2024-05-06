from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.markup import *
from utils.create_delete_user import create_user, delete_user, give_user_to_manager
import pytest
import allure



@pytest.mark.independent
@pytest.mark.rules
@allure.title("test_add_rule_inside_group")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Create rule inside group by user")
def test_add_rule_inside_group(page: Page) -> None:

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)

    with allure.step("Auth with user"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to markup"):
        go_to_markup(page)

    with allure.step("Create group"):
        create_group("99999", page)

    with allure.step("Click at new group"):
        page.wait_for_selector(CLICK_NEW_GROUP)
        page.locator(CLICK_NEW_GROUP).click()
        page.wait_for_timeout(2000)

    with allure.step("Create rule"):
        create_rule("88888", page)

    with allure.step("Check that rule and group created"):
        page.wait_for_selector(NAZVANIE_PRAVILA_TEGIROVANIYA)
        expect(page.locator(NAZVANIE_PRAVILA_TEGIROVANIYA)).to_have_value("88888", timeout=wait_until_visible) #check rule
        #expect(page.get_by_text("99999").nth(1)).to_have_text("99999", timeout=wait_until_visible) #check parent group

    with allure.step("Delete rule and group"):
        delete_group_and_rule_or_dict(page)

    with allure.step("Check that deleted"):
        expect(page.get_by_text("99999")).not_to_be_visible(timeout=wait_until_visible) #check no parent group

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.rules
@allure.title("test_add_group_of_rules_edit_name_delete")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Create, rename and delete group of rules")
def test_add_group_of_rules_edit_name_delete(page: Page) -> None:

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)

    with allure.step("Auth with user"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to markup"):
        go_to_markup(page)

    with allure.step("Create group"):
        create_group("12345", page)

    with allure.step("Rename group"):
        page.wait_for_selector(BUTTON_PENCIL)
        page.locator(BUTTON_PENCIL).click()
        page.locator(INPUT_EDIT_GROUP_NAME).fill("54321")
        page.locator(BUTTON_SAVE_EDITED_NAME).get_by_role("button").first.click()

    with allure.step("Check group created and have edited name"):
        expect(page.get_by_text("54321")).to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete group"):
        page.locator(BUTTON_KORZINA).click()

    with allure.step("Check group deleted"):
        expect(page.get_by_text("54321")).not_to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.rules
@allure.title("test_add_rule_outside_group_disabled")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Creating rule outside group should be disabled")
def test_add_rule_outside_group_disabled(page: Page) -> None:

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)

    with allure.step("Auth with user"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to markup"):
        go_to_markup(page)

    with allure.step("Check that creating rule - disabled and alert exists"):
        expect(page.locator('[aria-label="Чтобы добвить тег, выберите или добавьте группу."]')).to_be_visible()

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.rules
@allure.title("test_add_rule_group_cancel")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Create and cancel group of rules")
def test_add_rule_group_cancel(page: Page) -> None:

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)

    with allure.step("Auth with user"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to markup"):
        go_to_markup(page)

    with allure.step("Press (Add group) button"):
        page.locator(BUTTON_DOBAVIT_GRUPPU).click()

    with allure.step("Press (Cancel) button"):
        page.locator(BUTTON_OTMENA).click()

    with allure.step("Check cancelled"):
        expect(page.locator(NI4EGO_NE_NAYDENO)).to_be_visible(timeout=wait_until_visible)  # надпись Ничего не найдено

    with allure.step("Press (Add group) button"):
        page.locator(BUTTON_DOBAVIT_GRUPPU).click()

    with allure.step("Press (X) button"):
        page.locator(BUTTON_KRESTIK).click()

    with allure.step("Check cancelled"):
        expect(page.locator(NI4EGO_NE_NAYDENO)).to_be_visible(timeout=wait_until_visible)  # надпись Ничего не найдено

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.rules
@allure.title("test_check_old_rule")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("DEV-1784   check old rule from Ecotelecom")
def test_check_old_rule(page: Page) -> None:

    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)

    with allure.step("Auth with Ecotelecom"):
        auth(ECOTELECOM, ECOPASS, page)

    with allure.step("Go to markup"):
        go_to_markup(page)

    with allure.step("Click at first group"):
        page.wait_for_selector('[href*="/dictionaries?group"]')
        page.locator('[data-testid="test"]').first.click()

    with allure.step("Check that rule opened"):
        page.wait_for_selector(NAZVANIE_PRAVILA_TEGIROVANIYA)
        expect(page.locator('[data-testid="fragmentRuleWhoSaid"]')).to_be_visible(timeout=wait_until_visible)


@pytest.mark.independent
@pytest.mark.rules
@allure.title("test_search_rule")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_search_rule for Ecotelecom")
def test_search_rule(page: Page) -> None:

    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)

    with allure.step("Auth with Ecotelecom"):
        auth(ECOTELECOM, ECOPASS, page)

    with allure.step("Go to markup"):
        go_to_markup(page)

    with allure.step("Search (should not depend on register)"):
        page.wait_for_selector('[href*="/dictionaries?group"]')
        page.locator(INPUT_POISK).nth(1).fill("coope")
        #page.locator("form").get_by_role("button").click()

    with allure.step("Check that found"):
        expect(page.get_by_text("Cooper")).to_have_count(1, timeout=wait_until_visible)


@pytest.mark.independent
@pytest.mark.rules
@allure.title("test_add_rule_inside_group_check_fragment_rule")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Create rule inside group, check rule for fragments")
def test_add_rule_inside_group_check_fragment_rule(page: Page) -> None:

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(URL, timeout=timeout)

    with allure.step("Auth with user"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to markup"):
        go_to_markup(page)

    with allure.step("Create group"):
        create_group("99999", page)

    with allure.step("Click at group"):
        page.wait_for_selector(CLICK_NEW_GROUP)
        page.locator(CLICK_NEW_GROUP).click()
        page.wait_for_timeout(2000)

    with allure.step("Create rule"):
        create_rule("88888", page)

    with allure.step("Check that group created"):
        page.wait_for_selector(NAZVANIE_PRAVILA_TEGIROVANIYA)
        expect(page.locator(NAZVANIE_PRAVILA_TEGIROVANIYA)).to_have_value("88888", timeout=wait_until_visible) #check rule

    # switch "who said?"
    with allure.step("Switch (who said?) from first to last"):
        page.locator('[data-testid="fragmentRuleWhoSaid"]').get_by_text("Любой сказал").click()
        page.locator('[data-testid="fragmentRuleWhoSaid"]').get_by_text("Клиент сказал").click()
        page.locator('[data-testid="fragmentRuleWhoSaid"]').get_by_text("Клиент сказал", exact=True).click()
        page.locator('[data-testid="fragmentRuleWhoSaid"]').get_by_text("Сотрудник сказал").click()
        page.locator('[data-testid="fragmentRuleWhoSaid"]').get_by_text("Сотрудник сказал", exact=True).click()
        page.locator('[data-testid="fragmentRuleWhoSaid"]').get_by_text("Любой не сказал").click()
        page.locator('[data-testid="fragmentRuleWhoSaid"]').get_by_text("Любой не сказал", exact=True).click()
        page.locator('[data-testid="fragmentRuleWhoSaid"]').get_by_text("Клиент не сказал").click()
        page.locator('[data-testid="fragmentRuleWhoSaid"]').get_by_text("Клиент не сказал", exact=True).click()
        page.locator('[data-testid="fragmentRuleWhoSaid"]').get_by_text("Сотрудник не сказал").click()
        page.locator('[data-testid="fragmentRuleWhoSaid"]').get_by_text("Сотрудник не сказал", exact=True).click()
        page.locator('[data-testid="fragmentRuleWhoSaid"]').get_by_text("Любой сказал", exact=True ).click()

    with allure.step("Check that finally became first again"):
        expect(page.locator('[data-testid="fragmentRuleWhoSaid"]')).to_contain_text("Любой сказал")

    with allure.step("Fill (what said)"):
        fill_what_said("someText",page)

    with allure.step("Add all additional terms and click checkboxes in additional params"):
        Additional_terms = ["Искать с начала разговора", "Тегировать только первое совпадение", "Молчание до", "Молчание после", "Время разговора перед фрагментом",
                            "Время разговора после фрагмента", "Длительность перебивания", "Кол-во фрагментов перед этим фрагментом",
                            "Кол-во фрагментов после этого фрагмента", "Время разговора до предыдущего правила", "Кол-во фрагментов до предыдущего правила",
                            "Альтернативный поиск", "Связывать фрагменты"]

        add_additional_terms(Additional_terms, page)

    with allure.step("Add and delete another fragment"):
        page.locator('[data-testid="fragmentRuleaddFragment"]').click()
        page.locator('[data-testid="fragmentRuleDeleteButton"]').nth(1).click()

    with allure.step("Switch alternative search (who said?) from first to last"):
        page.locator('[data-testid="fragmentRuleBlock"]').locator('[class*="singleValue"]').nth(1).get_by_text("Любой сказал").click()
        page.locator('[data-testid="fragmentRuleBlock"]').get_by_text("Клиент сказал").click()
        page.locator('[data-testid="fragmentRuleBlock"]').get_by_text("Клиент сказал", exact=True).click()
        page.locator('[data-testid="fragmentRuleBlock"]').get_by_text("Сотрудник сказал").click()
        page.locator('[data-testid="fragmentRuleBlock"]').get_by_text("Сотрудник сказал", exact=True).click()
        page.locator('[data-testid="fragmentRuleBlock"]').get_by_text("Любой не сказал").click()
        page.locator('[data-testid="fragmentRuleBlock"]').get_by_text("Любой не сказал", exact=True).click()
        page.locator('[data-testid="fragmentRuleBlock"]').get_by_text("Клиент не сказал").click()
        page.locator('[data-testid="fragmentRuleBlock"]').get_by_text("Клиент не сказал", exact=True).click()
        page.locator('[data-testid="fragmentRuleBlock"]').get_by_text("Сотрудник не сказал").click()
        page.locator('[data-testid="fragmentRuleBlock"]').get_by_text("Сотрудник не сказал", exact=True).click()
        page.locator('[data-testid="fragmentRuleBlock"]').get_by_text("Любой сказал", exact=True).nth(1).click()

    with allure.step("Fill alternative search (what said)"):
        page.locator('[data-testid="fragmentRuleBlock"]').locator('[autocorrect="off"]').nth(1).fill("againSomeText")
        page.keyboard.press("Enter")

    with allure.step("Press (Save) button"):
        page.get_by_role("button", name="Сохранить").click()
        page.wait_for_timeout(1000)

    with allure.step("Page reload"):
        page.reload()

    with allure.step("Check that all saved"):
        expect(page.get_by_text("Любой сказал")).to_have_count(2)
        expect(page.get_by_text("Искать с начала разговора")).to_have_count(1)
        expect(page.get_by_text("Тегировать только первое совпадение")).to_have_count(1)

    with allure.step("Delete rule and group"):
        delete_group_and_rule_or_dict(page)

    with allure.step("Check that deleted"):
        expect(page.get_by_text("99999")).not_to_be_visible(timeout=wait_until_visible) #check no parent group

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)