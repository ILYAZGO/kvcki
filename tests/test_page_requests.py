from playwright.sync_api import Page, expect, BrowserContext, sync_playwright, Playwright
from utils.variables import *
from pages.page_requests import *
from utils.create_delete_user import create_user, delete_user, give_access_right, give_users_to_manager
import pytest
import allure

@pytest.mark.page_requests
@pytest.mark.e2e
@allure.title("test_communications_requests")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("test_communications_requests")
def est_communications_requests(base_url, page: Page) -> None:
    page_requests = PageRequests(page)

    communications_requests = []

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        page_requests.navigate(base_url)
        page.wait_for_timeout(2000)

    with allure.step("Request capture start"):
        page.on("request", lambda request: (
            communications_requests.append({
                'url': request.url,
                'method': request.method,
                # 'headers': request.headers,
                # 'post_data': request.post_data
            }) if request.resource_type in ['xhr', 'fetch'] else None
        ))

    with allure.step("Auth with user"):
        page_requests.auth(LOGIN, PASSWORD)

    with allure.step("Check requests list"):
        page.wait_for_timeout(7000)
        assert len(communications_requests) == 24
        assert sum('/token' in entry.get('url', '') for entry in communications_requests) == 1
        assert sum('/user/me/access_rights' in entry.get('url', '') for entry in communications_requests) == 2
        assert sum('/search_criterias/default_keys' in entry.get('url', '') for entry in communications_requests) == 2
        assert sum('/search_filters/' in entry.get('url', '') for entry in communications_requests) == 2
        assert sum('/user/me?with_quota=true' in entry.get('url', '') for entry in communications_requests) == 3
        assert sum('/reports' in entry.get('url', '') for entry in communications_requests) == 2
        assert sum('/translation/get_all_languages' in entry.get('url', '') for entry in communications_requests) == 1
        assert sum('/get_date_range_by_period?period=today' in entry.get('url', '') for entry in communications_requests) == 1
        assert sum('/users/?with_childs=true' in entry.get('url', '') for entry in communications_requests) == 2
        assert sum('/open_id/list' in entry.get('url', '') for entry in communications_requests) == 1
        assert sum('/user/filter?with_quota=true' in entry.get('url', '') for entry in communications_requests) == 2
        assert sum('/search_criterias/' in entry.get('url', '') for entry in communications_requests) == 4 # 2 here 2 with /default_keys
        assert sum('/search_calls/' in entry.get('url', '') for entry in communications_requests) == 2
        assert sum(f'/user/{USER_ID}?with_quota=true' in entry.get('url', '') for entry in communications_requests) == 1

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.page_requests
@pytest.mark.e2e
@allure.title("test_markup_requests_by_user")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("test_markup_requests. rules, dicts, checklists, gpt")
def test_markup_requests_by_user(base_url, page: Page) -> None:
    page_requests = PageRequests(page)

    rules_requests = []
    dicts_requests = []
    checklists_requests = []
    gpt_requests = []

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        page_requests.navigate(base_url)

    with allure.step("Auth with user"):
        page_requests.auth(LOGIN, PASSWORD)
        page.wait_for_timeout(14000)

    with allure.step("Request capture start"):
        page.on("request", lambda request: (
            rules_requests.append({
                'url': request.url,
                'method': request.method
            }) if request.resource_type in ['xhr', 'fetch'] else None
        ))

    with allure.step("Go to markup"):
        page_requests.click_markup()

    with allure.step("Check requests list"):
        page.wait_for_timeout(7000)
        assert len(rules_requests) == 5
        assert sum('/users/?with_childs=false&filter_only_users=true' in entry.get('url', '') for entry in rules_requests) == 1
        assert sum('/search_criterias/' in entry.get('url', '') for entry in rules_requests) == 1
        assert sum('/tag_rule_groups/' in entry.get('url', '') for entry in rules_requests) == 1
        assert sum('/tag_rules/?sort=update_time&sort_desc=true&show_disabled=true' in entry.get('url', '') for entry in rules_requests) == 1
        assert sum('/active_dicts/' in entry.get('url', '') for entry in rules_requests) == 1

    with allure.step("Request capture start"):
        page.on("request", lambda request: (
            dicts_requests.append({
                'url': request.url,
                'method': request.method
            }) if request.resource_type in ['xhr', 'fetch'] else None
        ))

    with allure.step("Click dicts"):
        page_requests.click_dicts()

    with allure.step("Check requests list"):
        page.wait_for_timeout(7000)
        assert len(dicts_requests) == 5
        assert sum('/users/?with_childs=false&filter_only_users=true' in entry.get('url', '') for entry in dicts_requests) == 1
        assert sum('/search_criterias/' in entry.get('url', '') for entry in dicts_requests) == 1
        assert sum('/dict_groups/' in entry.get('url', '') for entry in dicts_requests) == 1
        assert sum('/dicts/?sort=title&sort_desc=false&show_disabled=true' in entry.get('url', '') for entry in dicts_requests) == 1
        assert sum('/active_dicts/' in entry.get('url', '') for entry in dicts_requests) == 1


    with allure.step("Request capture start"):
        page.on("request", lambda request: (
            checklists_requests.append({
                'url': request.url,
                'method': request.method
            }) if request.resource_type in ['xhr', 'fetch'] else None
        ))

    with allure.step("Click dicts"):
        page_requests.click_check_list()

    with allure.step("Check requests list"):
        page.wait_for_timeout(7000)
        assert len(checklists_requests) == 4
        assert sum('/users/?with_childs=false&filter_only_users=true' in entry.get('url', '') for entry in checklists_requests) == 1
        assert sum('/search_criterias/' in entry.get('url', '') for entry in checklists_requests) == 1
        assert sum('/checklists/' in entry.get('url', '') for entry in checklists_requests) == 2

    with allure.step("Request capture start"):
        page.on("request", lambda request: (
            gpt_requests.append({
                'url': request.url,
                'method': request.method
            }) if request.resource_type in ['xhr', 'fetch'] else None
        ))

    with allure.step("Click dicts"):
        page_requests.click_gpt()

    with allure.step("Check requests list"):
        page.wait_for_timeout(7000)
        # if no any gpt rules
        assert len(gpt_requests) == 3
        assert sum('/users/?with_childs=false&filter_only_users=true' in entry.get('url', '') for entry in gpt_requests) == 1
        assert sum('/search_criterias/' in entry.get('url', '') for entry in gpt_requests) == 1
        assert sum('/gpt/' in entry.get('url', '') for entry in gpt_requests) == 1

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.page_requests
@pytest.mark.e2e
@allure.title("test_notifications_requests_by_user")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("test_notifications_requests_by_user")
def test_notifications_requests_by_user(base_url, page: Page) -> None:
    page_requests = PageRequests(page)

    notifications_requests = []

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        page_requests.navigate(base_url)

    with allure.step("Auth with user"):
        page_requests.auth(LOGIN, PASSWORD)
        page.wait_for_timeout(14000)

    with allure.step("Request capture start"):
        page.on("request", lambda request: (
            notifications_requests.append({
                'url': request.url,
                'method': request.method
            }) if request.resource_type in ['xhr', 'fetch'] else None
        ))

    with allure.step("Go to notifications"):
        page_requests.click_notifications()

    with allure.step("Check requests list"):
        page.wait_for_timeout(7000)
        assert len(notifications_requests) == 6
        assert sum('/notify_rules/' in entry.get('url', '') for entry in notifications_requests) == 6 # 2 directly 4 in others
        assert sum('/notify_rules/available_directions' in entry.get('url', '') for entry in notifications_requests) == 1
        assert sum('/notify_rules/amo_fillable_custom_fields' in entry.get('url', '') for entry in notifications_requests) == 1
        assert sum('/notify_rules/bitrix_fillable_custom_fields' in entry.get('url', '') for entry in notifications_requests) == 1
        assert sum('/notify_rules/notify_rule_variables' in entry.get('url', '') for entry in notifications_requests) == 1

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)



@pytest.mark.page_requests
@pytest.mark.e2e
@allure.title("test_settings_requests_by_user")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("test_settings_requests_by_user")
def test_settings_requests_by_user(base_url, page: Page) -> None:
    page_requests = PageRequests(page)

    settings_requests = []

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        page_requests.navigate(base_url)

    with allure.step("Auth with user"):
        page_requests.auth(LOGIN, PASSWORD)
        page.wait_for_timeout(10000)

    with allure.step("Request capture start"):
        page.on("request", lambda request: (
            settings_requests.append({
                'url': request.url,
                'method': request.method
            }) if request.resource_type in ['xhr', 'fetch'] else None
        ))

    with allure.step("Go to settings"):
        page_requests.click_settings()

    with allure.step("Check requests list"):
        page.wait_for_timeout(7000)
        assert len(settings_requests) == 4
        assert sum('/industries' in entry.get('url', '') for entry in settings_requests) == 1
        assert sum('/users/?filter_only_managers=true' in entry.get('url', '') for entry in settings_requests) == 1
        assert sum('/all_timezones' in entry.get('url', '') for entry in settings_requests) == 1
        assert sum(f'/user/{USER_ID}?with_quota=true' in entry.get('url', '') for entry in settings_requests) == 1

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.page_requests
@pytest.mark.e2e
@allure.title("test_users_list_requests_by_admin")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("test_users_list_requests_by_admin")
def test_users_list_requests_by_admin(base_url, page: Page) -> None:
    page_requests = PageRequests(page)

    users_list_requests = []

    with allure.step("Create admin"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    with allure.step("Go to url"):
        page_requests.navigate(base_url)

    with allure.step("Auth with admin"):
        page_requests.auth(LOGIN, PASSWORD)
        page.wait_for_timeout(10000)

    with allure.step("Request capture start"):
        page.on("request", lambda request: (
            users_list_requests.append({
                'url': request.url,
                'method': request.method
            }) if request.resource_type in ['xhr', 'fetch'] else None
        ))

    with allure.step("Go to users list"):
        page_requests.go_to_users_list()

    with allure.step("Check requests list"):
        page.wait_for_timeout(7000)
        assert len(users_list_requests) == 4
        assert sum('/industries' in entry.get('url', '') for entry in users_list_requests) == 1
        assert sum('/users/?filter_only_managers=true' in entry.get('url', '') for entry in users_list_requests) == 1
        assert sum('/stt/get_all_languages' in entry.get('url', '') for entry in users_list_requests) == 1
        assert sum('/users/?with_childs=true&with_quota=true' in entry.get('url', '') for entry in users_list_requests) == 1

    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN, USER_ID)