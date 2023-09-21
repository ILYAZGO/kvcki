from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
import pytest

@pytest.mark.adminbar
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    auth(MANAGER, PASSWORD, page)
    '''check name have count 2 '''
    expect(page.get_by_text("managerIM")).to_have_count(2, timeout=wait_until_visible)
    '''go to user'''
    page.locator('//*[@id="react-select-2-input"]').fill("userIM")
    page.wait_for_timeout(2000)
    page.get_by_text("userIM", exact=True).click()
    '''check name have count 1 and user have count 1'''
    expect(page.get_by_text("managerIM")).to_have_count(1, timeout=wait_until_visible)
    expect(page.get_by_text("userIM")).to_have_count(1, timeout=wait_until_visible)
    expect(page.get_by_text("Пользователи")).to_have_count(1, timeout=wait_until_visible)
    '''go back'''
    page.locator('[data-testid="adminBar"]').get_by_role("button").click()
    '''check name have count 2'''
    expect(page.get_by_text("managerIM")).to_have_count(2, timeout=wait_until_visible)


