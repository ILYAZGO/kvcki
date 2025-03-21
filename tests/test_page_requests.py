from playwright.sync_api import Page, expect, BrowserContext, sync_playwright, Playwright
from utils.variables import *
from pages.communications import *
from utils.create_delete_user import create_user, delete_user, give_access_right, give_users_to_manager
import pytest
import allure

@pytest.mark.calls
@pytest.mark.e2e
@allure.title("test_experiment")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("test_experiment")
def test_experiment(base_url, page: Page) -> None:
    communications = Communications(page)

    captured_requests = []

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        communications.navigate(base_url)
        page.wait_for_timeout(2000)

    with allure.step("Request capture start"):
        page.on("request", lambda request: (
            captured_requests.append({
                'url': request.url,
                'method': request.method,
                # 'headers': request.headers,
                # 'post_data': request.post_data
            }) if request.resource_type in ['xhr', 'fetch'] else None
        ))

    with allure.step("Auth with user"):
        communications.auth(LOGIN, PASSWORD)

    with allure.step("Check requests list"):
        page.wait_for_timeout(7000)
        assert len(captured_requests) == 24
        assert sum('/token' in entry.get('url', '') for entry in captured_requests) == 1
        assert sum('/user/me/access_rights' in entry.get('url', '') for entry in captured_requests) == 2
        assert sum('/search_criterias/default_keys' in entry.get('url', '') for entry in captured_requests) == 2
        assert sum('/search_filters/' in entry.get('url', '') for entry in captured_requests) == 2
        assert sum('/user/me?with_quota=true' in entry.get('url', '') for entry in captured_requests) == 3
        assert sum('/reports' in entry.get('url', '') for entry in captured_requests) == 2
        assert sum('/translation/get_all_languages' in entry.get('url', '') for entry in captured_requests) == 1
        assert sum('/get_date_range_by_period?period=today' in entry.get('url', '') for entry in captured_requests) == 1
        assert sum('/users/?with_childs=true' in entry.get('url', '') for entry in captured_requests) == 2
        assert sum('/open_id/list' in entry.get('url', '') for entry in captured_requests) == 1
        assert sum('/user/filter?with_quota=true' in entry.get('url', '') for entry in captured_requests) == 2
        assert sum('/search_criterias/' in entry.get('url', '') for entry in captured_requests) == 4 # 2 here 2 with /default_keys
        assert sum('/search_calls/' in entry.get('url', '') for entry in captured_requests) == 2
        assert sum(f'/user/{USER_ID}?with_quota=true' in entry.get('url', '') for entry in captured_requests) == 1

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)