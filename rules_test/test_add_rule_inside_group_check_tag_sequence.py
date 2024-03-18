from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.markup import *
from utils.create_delete_user import create_user, delete_user
import pytest

'''Create rule inside group, check rule for fragments'''


@pytest.mark.independent
@pytest.mark.rules
def test_example(page: Page) -> None:
    USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    page.goto("http://192.168.10.101/feature-dev-2013/", timeout=timeout)

    auth(LOGIN, PASSWORD, page)

    go_to_markup(page)

    create_group("99999", page)

    '''click group'''
    page.wait_for_selector(CLICK_NEW_GROUP)
    page.locator(CLICK_NEW_GROUP).click()
    page.wait_for_timeout(1900)

    create_rule("tag_seq", page)

    '''check'''
    page.wait_for_selector(NAZVANIE_PRAVILA_TEGIROVANIYA)
    expect(page.locator(NAZVANIE_PRAVILA_TEGIROVANIYA)).to_have_value("tag_seq", timeout=wait_until_visible) #check rule

    # add 2 rules for tag sequence and delete one
    page.locator(BUTTON_ADD_SEQUENCE).click()

    page.locator(BUTTON_ADD_SEQUENCE).click()
    page.locator(BUTTON_DELETE_SEQUENCE).nth(0).click()

    expect(page.locator(BUTTON_DELETE_SEQUENCE)).to_have_count(1)

    page.locator(LIST_PRESENCE_ONE_OF_TAGS).click()
    page.locator(LIST_PRESENCE_ONE_OF_TAGS).get_by_text("tag_seq", exact=True).click()
    page.locator('[class*="styles_ruleItemHeader"]').click()

    page.locator(INPUT_INTERVAL_BETWEEN_TAGS).locator('[type="text"]').fill("1234567890")

    page.locator(CHECK_BOX_ABSENCE_OF_TAGS).click()
    page.locator(CHECK_BOX_REVERSE_LOGIC).click()

    expect(page.locator(CHECK_BOX_ABSENCE_OF_TAGS)).to_be_checked()
    expect(page.locator(CHECK_BOX_REVERSE_LOGIC)).to_be_checked()

    page.locator(LIST_PRESENCE_ONE_OF_TAGS_IN_INTERVAL_AFTER).click()
    page.locator(LIST_PRESENCE_ONE_OF_TAGS_IN_INTERVAL_AFTER).get_by_text("tag_seq", exact=True).click()

    page.get_by_role("button", name="Сохранить").click()
    page.wait_for_timeout(1000)

    page.locator(BUTTON_DELETE_SEQUENCE).click()
    page.reload()
    page.wait_for_selector('[data-testid="TagSequenceItem"]', timeout=wait_until_visible)

    expect(page.locator(CHECK_BOX_ABSENCE_OF_TAGS)).to_be_checked()
    expect(page.locator(CHECK_BOX_REVERSE_LOGIC)).to_be_checked()
    expect(page.locator(INPUT_INTERVAL_BETWEEN_TAGS).locator('[type="text"]')).to_have_value("1234567890")
    expect(page.locator('[data-testid="TagSequenceItem"]').get_by_text("tag_seq")).to_have_count(2)

    delete_group_and_rule_or_dict(page)

    '''check teardown'''
    expect(page.get_by_text("99999")).not_to_be_visible(timeout=wait_until_visible) #check no parent group

    delete_user(API_URL, TOKEN, USER_ID)






