from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.check_lists import *
import pytest

'''Check old checklist from ecotelecom'''

@pytest.mark.check_list
def test_example(page: Page) -> None:

    page.goto(URL, timeout=timeout)

    auth(ECOTELECOM, ECOPASS, page)

    go_to_check_list(page)

    page.locator('[class*=groupItem]').first.click()

    page.wait_for_selector(INPUT_CHECK_LIST_NAME)

    expect(page.locator('[name="appraisers.0.title"]')).to_be_visible()

