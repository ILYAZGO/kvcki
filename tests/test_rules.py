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
def test_add_rule_inside_group(base_url, page: Page) -> None:

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with user"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to markup"):
        go_to_markup(page)

    with allure.step("Create group"):
        create_group("99999", page)

    with allure.step("Click at new group"):
        page.locator(GROUP_LIST).get_by_text("99999").click()
        page.wait_for_timeout(500)

    with allure.step("Create rule"):
        create_rule("88888", page)

    with allure.step("Check that rule and group created"):
        page.wait_for_selector(NAZVANIE_PRAVILA_TEGIROVANIYA)
        expect(page.locator(NAZVANIE_PRAVILA_TEGIROVANIYA)).to_have_value("88888", timeout=wait_until_visible) #check rule
        #expect(page.locator(GROUP_LIST)).to_have_text("99999", timeout=wait_until_visible) #check parent group

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
def test_add_group_of_rules_edit_name_delete(base_url, page: Page) -> None:

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with user"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to markup"):
        go_to_markup(page)

    #
    with allure.step("Press (Add group) button"):
        page.locator(BUTTON_DOBAVIT_GRUPPU).click()

    with allure.step("Press (Cancel) button"):
        page.locator(BUTTON_OTMENA).click()

    with allure.step("Check cancelled"):
        expect(page.locator('[aria-label="Вкл/Выкл"]')).to_have_count(2, timeout=wait_until_visible)
        #expect(page.locator(NI4EGO_NE_NAYDENO)).to_be_visible(timeout=wait_until_visible)  # надпись Ничего не найдено

    with allure.step("Press (Add group) button"):
        page.locator(BUTTON_DOBAVIT_GRUPPU).click()

    with allure.step("Press (X) button"):
        page.locator(BUTTON_KRESTIK).click()

    with allure.step("Check cancelled"):
        expect(page.locator('[aria-label="Вкл/Выкл"]')).to_have_count(2, timeout=wait_until_visible)
        #expect(page.locator(NI4EGO_NE_NAYDENO)).to_be_visible(timeout=wait_until_visible)  # надпись Ничего не найдено
    #

    with allure.step("Create group"):
        create_group("12345", page)

    with allure.step("Click at new group"):
        page.locator(GROUP_LIST).get_by_text("12345").click()
        page.wait_for_timeout(500)

    with allure.step("Rename group"):
        page.wait_for_selector(BUTTON_PENCIL)
        page.locator(ACTIVE_GROUP).locator(BUTTON_PENCIL).click()
        page.locator(INPUT_EDIT_GROUP_NAME).fill("54321")
        page.locator(ACTIVE_GROUP).locator(BUTTON_SAVE_EDITED_NAME).get_by_role("button").first.click()

    with allure.step("Check group created and have edited name"):
        expect(page.get_by_text("54321")).to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete group"):
        page.locator(ACTIVE_GROUP).locator(BUTTON_KORZINA).click()

    with allure.step("Check group deleted"):
        expect(page.locator(GROUP_LIST).get_by_text("54321")).not_to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.rules
@allure.title("test_add_rule_outside_group_disabled")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Creating rule outside group should be disabled")
def test_add_rule_outside_group_disabled(base_url, page: Page) -> None:

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

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
@allure.title("test_check_old_rule")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("DEV-1784   check old rule from Ecotelecom")
def test_check_old_rule(base_url, page: Page) -> None:

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

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
def test_search_rule(base_url, page: Page) -> None:

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

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
def test_add_rule_inside_group_check_fragment_rule(base_url, page: Page) -> None:

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with user"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to markup"):
        go_to_markup(page)

    with allure.step("Create group"):
        create_group("99999", page)

    with allure.step("Click at group"):
        page.locator(GROUP_LIST).get_by_text("99999").click()
        page.wait_for_timeout(500)

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

    with allure.step("Check (merge fragments) have value 0,11"):
        expect(page.locator('[data-testid="secondsMergeFragmentsText"]').locator('[type="text"]')).to_have_value("0.11")

    with allure.step("Add all additional terms and click checkboxes in additional params"):
        Additional_terms = ["Искать с начала разговора", "Тегировать только первое совпадение", "Молчание до", "Молчание после", "Время разговора перед фрагментом",
                            "Время разговора после фрагмента", "Длительность перебивания", "Кол-во фрагментов перед этим фрагментом",
                            "Кол-во фрагментов после этого фрагмента", "Время разговора до предыдущего правила", "Кол-во фрагментов до предыдущего правила",
                            "Альтернативный поиск"]   # "Связывать фрагменты" changed in https://task.imot.io/browse/DEV-2599

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
        page.locator('[data-testid="fragmentRuleBlock"]').locator('[autocorrect="off"]').nth(1).type("againSomeText", delay=100)
        page.keyboard.press("Enter", delay=100)
        page.wait_for_timeout(500)

    with allure.step("Press (Save) button"):
        page.get_by_role("button", name="Сохранить").click()
        page.wait_for_timeout(1000)

    with allure.step("Page reload"):
        page.reload()
        page.wait_for_selector('[data-testid="fragmentRuleBlock"]')

    with allure.step("Check that all saved"):
        expect(page.locator('[data-testid="fragmentRuleBlock"]').get_by_text("Любой сказал")).to_have_count(2)
        expect(page.locator('[data-testid="fragmentRuleBlock"]').get_by_text("Искать с начала разговора")).to_have_count(1)
        expect(page.locator('[data-testid="fragmentRuleBlock"]').get_by_text("Тегировать только первое совпадение")).to_have_count(1)

    with allure.step("Delete rule and group"):
        delete_group_and_rule_or_dict(page)

    with allure.step("Check that deleted"):
        expect(page.get_by_text("99999")).not_to_be_visible(timeout=wait_until_visible) #check no parent group

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.rules
@allure.title("test_add_rule_inside_group_check_set_tag_block")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Create rule inside group, check tag block")
def test_add_rule_inside_group_check_set_tag_block(base_url, page: Page) -> None:

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with user"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to markup"):
        go_to_markup(page)

    with allure.step("Create group"):
        create_group("99999", page)

    with allure.step("Click at group"):
        page.locator(GROUP_LIST).get_by_text("99999").click()
        page.wait_for_timeout(500)

    with allure.step("Create rule"):
        create_rule("set_tags", page)

    with allure.step("Check rule name and tag name. Need be the same"):
        page.wait_for_selector(NAZVANIE_PRAVILA_TEGIROVANIYA)
        expect(page.locator(NAZVANIE_PRAVILA_TEGIROVANIYA)).to_have_value("set_tags", timeout=wait_until_visible) #check rule
        expect(page.locator('[data-testid="setTagsItem_name"]').locator('[name="name"]')).to_have_value("set_tags", timeout=wait_until_visible) #check tag

    with allure.step("Press button (Add teg)"):
        page.locator('[data-testid="setTagsAddTagButton"]').click()

    with allure.step("Check that teg was added"):
        expect(page.locator('[data-testid="setTagsItem_name"]')).to_have_count(2, timeout=wait_until_visible)
        expect(page.locator('[data-testid="setTagsBlock"]').locator('[aria-label="Добавить значение тега"]')).to_have_count(2, timeout=wait_until_visible)
        expect(page.locator('[data-testid="setTagsDeleteTagButton"]')).to_have_count(2, timeout=wait_until_visible)
        expect(page.locator('[data-testid="setTagsItem_name"]').nth(1).locator('[name="name"]')).to_have_value("set_tags", timeout=wait_until_visible)

    with allure.step("Delete added tag"):
        page.locator('[data-testid="setTagsDeleteTagButton"]').nth(1).click()

    with allure.step("Check that teg deleted"):
        expect(page.locator('[data-testid="setTagsItem_name"]')).to_have_count(1, timeout=wait_until_visible)
        expect(page.locator('[data-testid="setTagsBlock"]').locator('[aria-label="Добавить значение тега"]')).to_have_count(1, timeout=wait_until_visible)
        expect(page.locator('[data-testid="setTagsDeleteTagButton"]')).to_have_count(1, timeout=wait_until_visible)

    with allure.step("Add additional params (tag value)"):
        page.locator('[data-testid="setTagsBlock"]').locator('[aria-label="Добавить значение тега"]').click()
        page.get_by_text("Значение тега", exact=True).click()

    with allure.step("Check that tag value added"):
        expect(page.locator('[name="value"]')).to_have_count(1, timeout=wait_until_visible)

    with allure.step("Fill tag value"):
        page.locator('[name="value"]').fill("tagValue")

    with allure.step("Press (save) button"):
        page.get_by_role("button", name="Сохранить").click()
        page.wait_for_timeout(1500)

    with allure.step("Page reload"):
        page.reload()
        page.wait_for_selector('[name="value"]')

    with allure.step("Check tag value still exists and have value"):
        expect(page.locator('[name="value"]')).to_have_value("tagValue")
        expect(page.locator('[data-testid="setTagsBlock"]').locator('[aria-label="Убрать значение тега"]')).to_have_count(1, timeout=wait_until_visible)
        expect(page.locator('[data-testid="setTagsDeleteTagButton"]')).to_have_count(1, timeout=wait_until_visible)

    with allure.step("Delete group and rule"):
        delete_group_and_rule_or_dict(page)

    with allure.step("Check that deleted"):
        expect(page.get_by_text("99999")).not_to_be_visible(timeout=wait_until_visible) #check no parent group

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.rules
@allure.title("test_add_rule_inside_group_check_tag_sequence")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_add_rule_inside_group_check_tag_sequence")
def test_add_rule_inside_group_check_tag_sequence(base_url, page: Page) -> None:

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with user"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to markup"):
        go_to_markup(page)

    with allure.step("Create_group"):
        create_group("99999", page)

    with allure.step("Click at group"):
        page.locator(GROUP_LIST).get_by_text("99999").click()
        page.wait_for_timeout(600)

    with allure.step("Create rule"):
        create_rule("tag_seq", page)

    with allure.step("Check that rule created"):
        page.wait_for_selector(NAZVANIE_PRAVILA_TEGIROVANIYA)
        expect(page.locator(NAZVANIE_PRAVILA_TEGIROVANIYA)).to_have_value("tag_seq", timeout=wait_until_visible) #check rule

    with allure.step("Add 2 rules for tag sequence and delete one"):
        page.locator(BUTTON_ADD_SEQUENCE).click()

        page.locator(BUTTON_ADD_SEQUENCE).click()
        page.locator(BUTTON_DELETE_SEQUENCE).nth(0).click()

    with allure.step("Check that tag sequence just one"):
        expect(page.locator(BUTTON_DELETE_SEQUENCE)).to_have_count(1)

    with allure.step("Fill (Presence of one of the tags)"):
        page.locator(LIST_PRESENCE_ONE_OF_TAGS).click()
        page.locator(LIST_PRESENCE_ONE_OF_TAGS).get_by_text("tag_seq", exact=True).click()
        page.locator('[class*="styles_ruleItemHeader"]').click()

    with allure.step("Fill (Interval between tags)"):
        page.locator(INPUT_INTERVAL_BETWEEN_TAGS).locator('[type="text"]').fill("1234567890")

    with allure.step("Click on 2 checkboxes"):
        page.locator(CHECK_BOX_ABSENCE_OF_TAGS).click()
        page.locator(CHECK_BOX_REVERSE_LOGIC).click()

    with allure.step("Check that checkboxes checked"):
        expect(page.locator(CHECK_BOX_ABSENCE_OF_TAGS)).to_be_checked()
        expect(page.locator(CHECK_BOX_REVERSE_LOGIC)).to_be_checked()

    with allure.step("Fill (The presence of one of the tags in the specified interval after)"):
        page.locator(LIST_PRESENCE_ONE_OF_TAGS_IN_INTERVAL_AFTER).click()
        page.locator(LIST_PRESENCE_ONE_OF_TAGS_IN_INTERVAL_AFTER).get_by_text("tag_seq", exact=True).click()

    with allure.step("Press (Save) button"):
        page.get_by_role("button", name="Сохранить").click()
        page.wait_for_timeout(1000)

    with allure.step("Delete tag sequence"):
        page.locator(BUTTON_DELETE_SEQUENCE).click()

    with allure.step("Page reload"):
        page.reload()
        page.wait_for_selector('[data-testid="TagSequenceItem"]', timeout=wait_until_visible)

    with allure.step("Check"):
        expect(page.locator(CHECK_BOX_ABSENCE_OF_TAGS)).to_be_checked()
        expect(page.locator(CHECK_BOX_REVERSE_LOGIC)).to_be_checked()
        expect(page.locator(INPUT_INTERVAL_BETWEEN_TAGS).locator('[type="text"]')).to_have_value("1234567890")
        expect(page.locator('[data-testid="TagSequenceItem"]').get_by_text("tag_seq")).to_have_count(2)

    with allure.step("Delete group and rule"):
        delete_group_and_rule_or_dict(page)

    with allure.step("Check that deleted"):
        expect(page.get_by_text("99999")).not_to_be_visible(timeout=wait_until_visible) #check no parent group

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.rules
@allure.title("test_import_group_and_rule_by_admin")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Precondition: user  importFrom with group 11111 rule 22222 inside with rule 33333 without group")
def test_import_group_and_rule_by_admin(base_url, page: Page) -> None:

    with allure.step("Create admin"):
        USER_ID_ADMIN, TOKEN_ADMIN, LOGIN_ADMIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with admin"):
        auth(LOGIN_ADMIN, PASSWORD, page)

    with allure.step("Go to user"):
        go_to_user(LOGIN_USER, page)

    with allure.step("Go to markup"):
        go_to_markup(page)

    with allure.step("Press (Import rules) button"):
        page.wait_for_selector(BUTTON_IMPORTIROVAT_PRAVILA)
        page.locator(BUTTON_IMPORTIROVAT_PRAVILA).click()

    with allure.step("Select user ImportFrom in modal window"):
        page.locator('[class*="simpleSelect"]').locator('[role="combobox"]').type("importFrom", delay=40)
        page.get_by_text("importFrom", exact=True).click()
        page.wait_for_timeout(1000)

    with allure.step("Check that search string visible"):
        page.wait_for_selector('[data-testid="markup_tags_importSearch}"]')

        expect(page.locator('[data-testid="markup_importNav_tags"]')).not_to_be_visible()
        expect(page.locator('[data-testid="markup_importNav_dicts"]')).not_to_be_visible()
        expect(page.locator('[data-testid="markup_tags_importSearch}"]')).to_be_visible()
        expect(page.locator('[data-testid="markup_importNav_gpt"]')).not_to_be_visible()

    with allure.step("Import group with rule"):
        page.locator('[class*="CopyMode_copyModeView__popup_"]').locator('[type="checkbox"]').nth(1).click()
        page.wait_for_timeout(1000)
        page.get_by_role("button", name="Продолжить").click()
        page.wait_for_timeout(2000)

    with allure.step("Import rule"):

        page.locator('[class*="CopyMode_copyModeView__popup_"]').locator('[type="checkbox"]').nth(3).click()
        page.wait_for_timeout(1000)
        page.get_by_role("button", name="К новым правилам").click()
        page.wait_for_timeout(2000)

    with allure.step("Check that import was successful"):
        expect(page.get_by_text("11111")).to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("22222")).to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("33333")).to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("44444")).to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("1 тег")).to_have_count(count=3, timeout=wait_until_visible)

    with allure.step("Delete groups and rules"):
        page.get_by_text("22222").click()
        page.locator('[width="30"]').click()
        page.wait_for_selector(MODAL_WINDOW)
        page.locator(MODAL_WINDOW).get_by_role("button", name="Удалить").click()
        page.wait_for_selector(MODAL_WINDOW, state="hidden")
        page.locator(BUTTON_KORZINA).first.click()
        page.wait_for_selector(ALERT, timeout=wait_until_visible)
        expect(page.locator(ALERT)).to_contain_text("Правило удалено")
        page.wait_for_selector(ALERT, state="hidden", timeout=wait_until_visible)

        page.get_by_text("44444").click()
        page.locator('[width="30"]').click()
        page.wait_for_selector(MODAL_WINDOW)
        page.locator(MODAL_WINDOW).get_by_role("button", name="Удалить").click()
        page.wait_for_selector(MODAL_WINDOW, state="hidden")
        page.locator(BUTTON_KORZINA).first.click()
        page.wait_for_selector(ALERT, timeout=wait_until_visible)
        expect(page.locator(ALERT)).to_contain_text("Правило удалено")
        page.wait_for_selector(ALERT, state="hidden", timeout=wait_until_visible)

    with allure.step("Check that deleted"):
        expect(page.get_by_text("11111")).not_to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("22222")).not_to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("33333")).not_to_be_visible(timeout=wait_until_visible)
        #page.wait_for_timeout(2600)
        expect(page.get_by_text("44444")).not_to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN_ADMIN, USER_ID_ADMIN)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)


@pytest.mark.independent
@pytest.mark.rules
@allure.title("test_import_group_and_rule_by_manager")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Precondition: user  importFrom with group 11111 rule 22222 inside with rule 33333 without group")
def test_import_group_and_rule_by_manager(base_url, page: Page) -> None:

    with allure.step("Create user"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Create manager"):
        USER_ID_MANAGER, TOKEN_MANAGER, LOGIN_MANAGER = create_user(API_URL, ROLE_MANAGER, PASSWORD)

    with allure.step("Give user to manager"):
        give_user_to_manager(API_URL, USER_ID_MANAGER, USER_ID_USER, TOKEN_MANAGER)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with manager"):
        auth(LOGIN_MANAGER, PASSWORD, page)

    with allure.step("Go to user"):
        go_to_user(LOGIN_USER, page)

    with allure.step("Go to markup"):
        go_to_markup(page)

    with allure.step("Press (Import rules) button"):
        page.wait_for_selector(BUTTON_IMPORTIROVAT_PRAVILA)
        page.locator(BUTTON_IMPORTIROVAT_PRAVILA).click()

    with allure.step("Select user ImportFrom in modal window"):
        page.locator('[class*="simpleSelect"]').locator('[role="combobox"]').type("importFrom", delay=40)
        page.get_by_text("importFrom", exact=True).click()
        page.wait_for_timeout(1000)

    with allure.step("Check that search string visible"):
        page.wait_for_selector('[data-testid="markup_tags_importSearch}"]')

        expect(page.locator('[data-testid="markup_importNav_tags"]')).not_to_be_visible()
        expect(page.locator('[data-testid="markup_importNav_dicts"]')).not_to_be_visible()
        expect(page.locator('[data-testid="markup_tags_importSearch}"]')).to_be_visible()
        expect(page.locator('[data-testid="markup_importNav_gpt"]')).not_to_be_visible()

    with allure.step("Import group with rule"):
        page.locator('[class*="CopyMode_copyModeView__popup_"]').locator('[type="checkbox"]').nth(1).click()
        page.wait_for_timeout(1000)
        page.get_by_role("button", name="Продолжить").click()
        page.wait_for_timeout(2000)

    with allure.step("Import rule"):
        page.locator('[class*="CopyMode_copyModeView__popup_"]').locator('[type="checkbox"]').nth(3).click()
        page.wait_for_timeout(1000)
        page.get_by_role("button", name="К новым правилам").click()
        page.wait_for_timeout(2000)

    with allure.step("Check that import was successful"):
        expect(page.get_by_text("11111")).to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("22222")).to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("33333")).to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("44444")).to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("1 тег")).to_have_count(count=3, timeout=wait_until_visible)

    with allure.step("Delete groups and rules"):
        page.get_by_text("22222").click()
        page.locator('[width="30"]').click()
        page.wait_for_selector(MODAL_WINDOW)
        page.locator(MODAL_WINDOW).get_by_role("button", name="Удалить").click()
        page.wait_for_selector(MODAL_WINDOW, state="hidden")
        page.locator(BUTTON_KORZINA).first.click()
        page.wait_for_selector(ALERT, timeout=wait_until_visible)
        expect(page.locator(ALERT)).to_contain_text("Правило удалено")
        page.wait_for_selector(ALERT, state="hidden", timeout=wait_until_visible)

        page.get_by_text("44444").click()
        page.locator('[width="30"]').click()
        page.wait_for_selector(MODAL_WINDOW)
        page.locator(MODAL_WINDOW).get_by_role("button", name="Удалить").click()
        page.wait_for_selector(MODAL_WINDOW, state="hidden")
        page.locator(BUTTON_KORZINA).first.click()
        page.wait_for_selector(ALERT, timeout=wait_until_visible)
        expect(page.locator(ALERT)).to_contain_text("Правило удалено")
        page.wait_for_selector(ALERT, state="hidden", timeout=wait_until_visible)

    with allure.step("Check that deleted"):
        expect(page.get_by_text("11111")).not_to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("22222")).not_to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("33333")).not_to_be_visible(timeout=wait_until_visible)
        #page.wait_for_timeout(2600)
        expect(page.get_by_text("44444")).not_to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete manager"):
        delete_user(API_URL, TOKEN_MANAGER, USER_ID_MANAGER)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)


@pytest.mark.independent
@pytest.mark.rules
@allure.title("test_import_rule_disabled_for_user")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_import_rule_disabled_for_user")
def test_import_rule_disabled_for_user(base_url, page: Page) -> None:

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with user"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to markup"):
        go_to_markup(page)

    with allure.step("Check that button for import not visible"):
        expect(page.locator(BUTTON_IMPORTIROVAT_PRAVILA)).not_to_be_visible()

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.rules
@allure.title("test_compare_rules_by_user")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("User has three rules with different parameters. when he switch between them, all parameters changing")
def test_compare_rules_by_user(base_url, page: Page) -> None:

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with user for check comparelogin"):
        auth(USER_FOR_CHECK, PASSWORD, page)

    with allure.step("Go to markup"):
        go_to_markup(page)

    with allure.step("Go to first rule"):
        page.get_by_text("firstrule").click()
        page.wait_for_selector('[data-testid="fragmentRuleBlock"]')

    with allure.step("Check filters and other inside rule"):
        expect(page.locator('[aria-label="Remove >100"]')).to_be_visible(timeout=wait_until_visible)
        expect(page.locator('[aria-label="Remove Словарь: firstdict"]')).to_be_visible()
        expect(page.locator('[data-testid="TagSequenceItem"]').locator('[aria-label="Remove firstrule"]')).to_have_count(2)
        expect(page.locator('[data-testid="intervalBetweenTags"]').locator('[value=">100"]')).to_have_count(1)
        expect(page.locator('[data-testid="setTagsBlock"]').locator('[name="name"]')).to_have_value("firstrule")
        expect(page.locator('[data-testid="setTagsBlock"]').locator('[name="value"]')).to_have_value("firstrulevalue")

    with allure.step("Change rule"):
        page.get_by_text("secondrule").click()
        page.wait_for_timeout(2000)

    with allure.step("Check filters and other inside rule was changed"):
        expect(page.locator('[aria-label="Remove >2222"]')).to_be_visible()
        expect(page.locator('[aria-label="Remove Словарь: seconddict"]')).to_be_visible()
        expect(page.locator('[data-testid="TagSequenceItem"]').locator('[aria-label="Remove secondrule"]')).to_have_count(2)
        expect(page.locator('[data-testid="intervalBetweenTags"]').locator('[value=">2222"]')).to_have_count(1)
        expect(page.locator('[data-testid="setTagsBlock"]').locator('[name="name"]')).to_have_value("secondrule")
        expect(page.locator('[data-testid="setTagsBlock"]').locator('[name="value"]')).to_have_value("secondrulevalue")

    with allure.step("Change rule"):
        page.get_by_text("thirdrule").click()
        page.wait_for_timeout(2000)

    with allure.step("Check that tagname still the same, but tagvalue changed"):
        expect(page.locator('[aria-label="Remove firstrule: firstrulevalue"]')).to_be_visible()
        expect(page.locator('[aria-label="Remove word"]')).to_be_visible()
        expect(page.locator('[data-testid="setTagsBlock"]').locator('[name="name"]')).to_have_value("secondrule")
        expect(page.locator('[data-testid="setTagsBlock"]').locator('[name="value"]')).to_have_value("thirdrulevalue")