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

    page.goto(URL, timeout=timeout)

    auth(LOGIN, PASSWORD, page)

    go_to_markup(page)

    create_group("99999", page)

    '''click group'''
    page.wait_for_selector(CLICK_NEW_GROUP)
    page.locator(CLICK_NEW_GROUP).click()
    page.wait_for_timeout(1600)

    create_rule("set_tags", page)

    '''check'''
    page.wait_for_selector(NAZVANIE_PRAVILA_TEGIROVANIYA)
    expect(page.locator(NAZVANIE_PRAVILA_TEGIROVANIYA)).to_have_value("set_tags", timeout=wait_until_visible) #check rule
    expect(page.locator('[data-testid="setTagsItem_name"]').locator('[name="name"]')).to_have_value("set_tags", timeout=wait_until_visible) #check tag

    # add another tag
    page.locator('[data-testid="setTagsAddTagButton"]').click()

    expect(page.locator('[data-testid="setTagsItem_name"]')).to_have_count(2, timeout=wait_until_visible)
    expect(page.locator('[data-testid="setTagsBlock"]').locator('[aria-label="Дополнительные условия"]')).to_have_count(2, timeout=wait_until_visible)
    expect(page.locator('[data-testid="setTagsDeleteTagButton"]')).to_have_count(2, timeout=wait_until_visible)
    expect(page.locator('[data-testid="setTagsItem_name"]').nth(1).locator('[name="name"]')).to_have_value("set_tags", timeout=wait_until_visible)

    # delete added tag
    page.locator('[data-testid="setTagsDeleteTagButton"]').nth(1).click()

    expect(page.locator('[data-testid="setTagsItem_name"]')).to_have_count(1, timeout=wait_until_visible)
    expect(page.locator('[data-testid="setTagsBlock"]').locator('[aria-label="Дополнительные условия"]')).to_have_count(1, timeout=wait_until_visible)
    expect(page.locator('[data-testid="setTagsDeleteTagButton"]')).to_have_count(1, timeout=wait_until_visible)

    # add additional params
    page.locator('[data-testid="setTagsBlock"]').locator('[aria-label="Дополнительные условия"]').click()
    page.get_by_text("Значение тега", exact=True).click()
    page.get_by_text("Видимость тега", exact=True).click()
    page.locator('[data-testid="setTagsBlock"]').locator('[aria-label="Дополнительные условия"]').click()

    expect(page.locator('[name="value"]')).to_have_count(1, timeout=wait_until_visible)
    expect(page.locator('[name="visible"]')).to_have_count(1, timeout=wait_until_visible)
    expect(page.locator('[name="visible"]')).not_to_be_checked()

    # fill additional params
    page.locator('[name="value"]').fill("tagValue")
    page.locator('[name="visible"]').click()

    # save
    page.get_by_role("button", name="Сохранить").click()
    page.wait_for_timeout(1500)

    page.reload()
    page.wait_for_selector('[name="value"]')

    expect(page.locator('[name="value"]')).to_have_value("tagValue")
    expect(page.locator('[name="visible"]')).to_be_checked()
    expect(page.locator('[data-testid="setTagsBlock"]').locator('[aria-label="Дополнительные условия"]')).to_have_count(1, timeout=wait_until_visible)
    expect(page.locator('[data-testid="setTagsDeleteTagButton"]')).to_have_count(1, timeout=wait_until_visible)


    delete_group_and_rule_or_dict(page)

    '''check teardown'''
    expect(page.get_by_text("99999")).not_to_be_visible(timeout=wait_until_visible) #check no parent group

    delete_user(API_URL, TOKEN, USER_ID)






