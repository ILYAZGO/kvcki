from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.notifications import *
from utils.create_delete_user import create_user, delete_user
import pytest


@pytest.mark.independent
@pytest.mark.notifications
def test_example(page: Page) -> None:
    USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    page.goto(URL, timeout=timeout)

    auth(LOGIN, PASSWORD, page)

    choose_block(0, page)

    expect(page.get_by_text("Telegram", exact=True)).to_have_count(1)

    choose_block(1, page)

    expect(page.get_by_text("Email", exact=True)).to_have_count(1)

    choose_block(2, page)

    expect(page.get_by_text("API", exact=True)).to_have_count(1)

    delete_user(API_URL, TOKEN, USER_ID)