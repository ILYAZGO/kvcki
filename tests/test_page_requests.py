from playwright.sync_api import Page, expect, BrowserContext, sync_playwright, Playwright
from utils.variables import *
from pages.communications import *
from utils.dates import *
from datetime import datetime
from utils.create_delete_user import create_user, delete_user, give_access_right, give_users_to_manager
import os
import pytest
import allure

@pytest.mark.calls
@pytest.mark.e2e
@allure.title("test_experiment")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("test_experiment")
def est_experiment(base_url, page: Page) -> None:
    communications = Communications(page)

    # Intercept and store requests
    captured_requests = []



    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        communications.navigate(base_url)
        page.wait_for_timeout(5000)

    page.on("request", lambda request: (
        captured_requests.append({
            'url': request.url,
            'method': request.method,
            # 'headers': request.headers,
            # 'post_data': request.post_data
        }) if request.resource_type == 'xhr' else None
    ))

    with allure.step("Auth with user"):
        communications.auth(LOGIN, PASSWORD)

    page.wait_for_timeout(5000)
    assert captured_requests == []

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)