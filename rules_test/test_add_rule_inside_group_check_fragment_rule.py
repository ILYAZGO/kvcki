from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.markup import *
from utils.create_delete_user import create_user, delete_user
import pytest

'''Create rule inside group, check rule for fragments'''

# REMINDER add test about alternative search

@pytest.mark.rules
def test_example(page: Page) -> None:
    USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    page.goto(URL, timeout=timeout)

    auth(LOGIN, PASSWORD, page)

    go_to_markup(page)

    create_group("99999", page)

    '''click group'''
    page.wait_for_selector(CLICK_NEW_GROUP)
    page.locator(CLICK_NEW_GROUP).click()
    page.wait_for_timeout(2000)

    create_rule("88888", page)

    '''check'''
    page.wait_for_selector(NAZVANIE_PRAVILA_TEGIROVANIYA)
    expect(page.locator(NAZVANIE_PRAVILA_TEGIROVANIYA)).to_have_value("88888", timeout=wait_until_visible) #check rule

    # switch "who said?"

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
    # finally need be first
    expect(page.locator('[data-testid="fragmentRuleWhoSaid"]')).to_contain_text("Любой сказал")

    fill_what_said("someText",page)

    # add all additional terms
    Additional_terms = ["Искать с начала разговора", "Тегировать только первое совпадение", "Молчание до", "Молчание после", "Время разговора перед фрагментом",
                        "Время разговора после фрагмента", "Длительность перебивания", "Кол-во фрагментов перед этим фрагментом",
                        "Кол-во фрагментов после этого фрагмента", "Время разговора до предыдущего правила", "Кол-во фрагментов до предыдущего правила",
                        "Альтернативный поиск", "Связывать фрагменты"]

    add_additional_terms(Additional_terms, page)
    # check boxes
    page.locator('[data-testid="fragmentRuleaddFragment"]').click()
    page.locator('[data-testid="fragmentRuleDeleteButton"]').nth(1).click()


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

    page.locator('[data-testid="fragmentRuleBlock"]').locator('[autocorrect="off"]').nth(1).fill("againSomeText")
    page.keyboard.press("Enter")

    # save
    page.get_by_role("button", name="Сохранить").click()
    page.wait_for_timeout(1000)

    page.reload()
    expect(page.get_by_text("Любой сказал")).to_have_count(2)
    expect(page.get_by_text("Искать с начала разговора")).to_have_count(1)
    expect(page.get_by_text("Тегировать только первое совпадение")).to_have_count(1)

    delete_group_and_rule_or_dict(page)

    '''check teardown'''
    expect(page.get_by_text("99999")).not_to_be_visible(timeout=wait_until_visible) #check no parent group

    delete_user(API_URL, TOKEN, USER_ID)






