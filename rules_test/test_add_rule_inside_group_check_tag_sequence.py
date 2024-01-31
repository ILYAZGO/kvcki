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
    USER_ID, BEARER, ACCESS_TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    page.goto(URL, timeout=timeout)

    auth(LOGIN, PASSWORD, page)

    go_to_markup(page)

    create_group("99999", page)

    '''click group'''
    page.wait_for_selector(CLICK_NEW_GROUP)
    page.locator(CLICK_NEW_GROUP).click()
    page.wait_for_timeout(2000)

    create_rule("tag_seq", page)

    '''check'''
    page.wait_for_selector(NAZVANIE_PRAVILA_TEGIROVANIYA)
    expect(page.locator(NAZVANIE_PRAVILA_TEGIROVANIYA)).to_have_value("tag_seq", timeout=wait_until_visible) #check rule

    # add 2 rules for tag sequence and delete one
    page.locator('[data-testid="addNewTagSequenceItemBtn"]').click()

    page.locator('[data-testid="addNewTagSequenceItemBtn"]').click()
    page.locator('[data-testid="TagSequenceDeleteItem"]').nth(0).click()
    expect(page.locator('[data-testid="TagSequenceDeleteItem"]')).to_have_count(1)

    page.locator('[data-testid="presenceOfOneOfTags"]').click()
    page.locator('[data-testid="presenceOfOneOfTags"]').get_by_text("tag_seq", exact=True).click()
    page.locator('[class*="styles_ruleItemHeader"]').click()

    page.locator('[data-testid="intervalBetweenTags"]').locator('[type="text"]').fill("1234567890")

    page.locator('[data-testid="triggeredInAbsenceOfTags"]').click()

    page.locator('[data-testid="presenceOfOneOfTagsInSpecifiedIntervalAfter"]').click()
    page.locator('[data-testid="presenceOfOneOfTagsInSpecifiedIntervalAfter"]').get_by_text("tag_seq", exact=True).click()

    page.get_by_role("button", name="Сохранить").click()
    page.wait_for_timeout(1000)

    page.locator('[data-testid="TagSequenceDeleteItem"]').click()
    page.reload()
    page.wait_for_selector('[aria-label="Remove tag_seq"]')
    page.wait_for_timeout(500)

    expect(page.locator('[aria-label="Remove tag_seq"]')).to_have_count(2)
    expect(page.locator('[data-testid="intervalBetweenTags"]').locator('[type="text"]')).to_have_value("1234567890")


    delete_group_and_rule_or_dict(page)

    '''check teardown'''
    expect(page.get_by_text("99999")).not_to_be_visible(timeout=wait_until_visible) #check no parent group

    delete_user(API_URL, USER_ID, BEARER, ACCESS_TOKEN)






