from playwright.sync_api import Page, expect
from utils.variables import *
from pages.notifications import *
from utils.create_delete_user import create_user, delete_user, give_user_to_manager
import pytest
import allure


@pytest.mark.independent
@pytest.mark.notifications
@allure.title("test_notifications_first_page")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_notifications_first_page")
def test_notifications_first_page(base_url, page: Page) -> None:
    notifications = Notifications(page)

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        notifications.navigate(base_url)

    with allure.step("Auth with user"):
        notifications.auth(LOGIN, PASSWORD)

    with allure.step("Click on block 0 from first page"):
        notifications.choose_block(0)

    with allure.step("Check that we moved to telegram new rule"):
        expect(page.get_by_text("Telegram", exact=True)).to_have_count(1)

    with allure.step("Click on block 1 from first page"):
        notifications.choose_block(1)

    with allure.step("Check that we moved to email new rule"):
        expect(page.get_by_text("Email", exact=True)).to_have_count(1)

    with allure.step("Click on block 2 from first page"):
        notifications.choose_block(2)

    with allure.step("Check that we moved to api new rule"):
        expect(page.get_by_text("API", exact=True)).to_have_count(1)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.notifications
@allure.title("test_notifications_api_method_change")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("test_notifications_api_method_change")
def test_notifications_api_method_change(base_url, page: Page) -> None:
    notifications = Notifications(page)

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        notifications.navigate(base_url)

    with allure.step("Auth with user"):
        notifications.auth(LOGIN, PASSWORD)

    with allure.step("Go to notifications"):
        notifications.click_notifications()

    with allure.step("Create api notification rule"):
        notifications.add_notification("API")

    with allure.step("Set notification name"):
        notifications.set_notification_name("auto-test-api_method_change")

    with allure.step("Set url and headers"):
        notifications.set_url_and_headers("https://www.google.com/", "someHeaders")

    with allure.step("Fill message"):
        notifications.fill_message("someText ")

    with allure.step("Change api method from POST to GET"):
        change_api_method("POST", "GET", page)

    with allure.step("Save rule"):
        notifications.save_rule()

    with allure.step("Check alert"):
        notifications.check_alert("Данные сохранены")

    with allure.step("Go back in rule after save"):
        notifications.go_back_in_rule_after_save("auto-test-api_method_change")

    with allure.step("Page reload"):
        page.reload()
        page.wait_for_selector(BlOCK_API)

    with allure.step("Check that block API has GET text"):
       expect(page.locator(BlOCK_API)).to_have_text("API*GET")

    with allure.step("Change api method from GET to PUT"):
        change_api_method("GET", "PUT", page)

    with allure.step("Save rule"):
        notifications.save_rule()

    with allure.step("Check alert"):
        notifications.check_alert("Данные сохранены")

    with allure.step("Go back in rule after save"):
        notifications.go_back_in_rule_after_save("auto-test-api_method_change")

    with allure.step("Page reload"):
        page.reload()
        page.wait_for_selector(BlOCK_API)

    with allure.step("Check that block API has PUT text"):
        expect(page.locator(BlOCK_API)).to_have_text("API*PUT")

    with allure.step("Change api method from PUT to PATCH"):
        change_api_method("PUT", "PATCH", page)

    with allure.step("Save rule"):
        notifications.save_rule()

    with allure.step("Check alert"):
        notifications.check_alert("Данные сохранены")

    with allure.step("Go back in rule after save"):
        notifications.go_back_in_rule_after_save("auto-test-api_method_change")

    with allure.step("Page reload"):
        page.reload()
        page.wait_for_selector(BlOCK_API)

    with allure.step("Check that block API has PATCH text"):
        expect(page.locator(BlOCK_API)).to_have_text("API*PATCH")

    with allure.step("Change api method from PATCH to POST"):
        change_api_method("PATCH", "POST", page)

    with allure.step("Save rule"):
        notifications.save_rule()

    with allure.step("Check alert"):
        notifications.check_alert("Данные сохранены")

    with allure.step("Go back in rule after save"):
        notifications.go_back_in_rule_after_save("auto-test-api_method_change")

    with allure.step("Page reload"):
        page.reload()
        page.wait_for_selector(BlOCK_API)

    with allure.step("Check that block API has POST text"):
        expect(page.locator(BlOCK_API)).to_have_text("API*POST")

    with allure.step("Delete rule"):
        delete_rule(page)

    with allure.step("Check that rule deleted"):
        expect(page.locator(BUTTON_KORZINA)).not_to_be_visible()

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.notifications
@allure.title("test_notifications_api")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_notifications_api")
def test_notifications_api(base_url, page: Page) -> None:
    notifications = Notifications(page)

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        notifications.navigate(base_url)

    with allure.step("Auth with user"):
        notifications.auth(LOGIN, PASSWORD)

    with allure.step("Go to notifications"):
        notifications.click_notifications()

    with allure.step("Create api notification rule"):
        notifications.add_notification("API")

    with allure.step("Set notification name"):
        notifications.set_notification_name("auto-test-api")

    with allure.step("Set url and headers"):
        notifications.set_url_and_headers("https://www.google.com/", "someHeaders")

    with allure.step("Checkbox send again when rule changed"):
        page.locator(BLOCK_RULE_MAIN_AREA).locator('[type="checkbox"]').click()

    with allure.step("Check that checkbox clicked"):
        expect(page.locator(BLOCK_RULE_MAIN_AREA).locator('[type="checkbox"]')).to_be_checked()

    with allure.step("add filter"):
        add_filter("По тегам", "auto_rule", "1", page)

    with allure.step("Fill message"):
        notifications.fill_message("someText ")

    with allure.step("Save rule"):
        notifications.save_rule()

    with allure.step("Check alert"):
        notifications.check_alert("Данные сохранены")

    with allure.step("Go back in rule after save"):
        notifications.go_back_in_rule_after_save("auto-test-api")

    with allure.step("Check"):
        expect(page.locator(BLOCK_RULE_MAIN_AREA).locator('[type="checkbox"]')).to_be_checked()
        expect(page.locator(BLOCK_RULES_LIST).locator('[type="checkbox"]')).to_be_checked()
        expect(page.locator('[aria-label="Remove auto_rule"]')).to_have_count(1)
        expect(page.locator(INPUT_COMMENT)).to_have_text("someText {{call_id}}")
        expect(page.locator(INPUT_NOTIFICATION_NAME)).to_have_value("auto-test-api")
        expect(page.locator(INPUT_URL)).to_have_value("https://www.google.com/")
        expect(page.locator(INPUT_HEADERS)).to_have_value("someHeaders")

    with allure.step("Delete rule"):
        delete_rule(page)

    with allure.step("Check that rule deleted"):
        expect(page.locator(BUTTON_KORZINA)).not_to_be_visible()

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.notifications
@allure.title("test_notifications_email")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_notifications_email")
def test_notifications_email(base_url, page: Page) -> None:
    notifications = Notifications(page)

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        notifications.navigate(base_url)

    with allure.step("Auth with user"):
        notifications.auth(LOGIN, PASSWORD)

    with allure.step("Go to notifications"):
        notifications.click_notifications()

    with allure.step("Create email notification rule"):
        notifications.add_notification("Email")

    with allure.step("Set notification name"):
        notifications.set_notification_name("auto-test-email")

    with allure.step("Checkbox send again when rule changed"):
        page.locator(BLOCK_RULE_MAIN_AREA).locator('[type="checkbox"]').click()

    with allure.step("Check that checkbox clicked"):
        expect(page.locator(BLOCK_RULE_MAIN_AREA).locator('[type="checkbox"]')).to_be_checked()

    with allure.step("add filter"):
        add_filter("По тегам", "auto_rule", "1", page)

    with allure.step("Fill message"):
        notifications.fill_message("someText ")

    with allure.step("Fill letter theme and email"):
        notifications.fill_attr_for_email('letterTheme', 'mail@.mail.com')

    with allure.step("Save rule"):
        notifications.save_rule()

    with allure.step("Check alert"):
        notifications.check_alert("Данные сохранены")

    with allure.step("Go back in rule after save"):
        notifications.go_back_in_rule_after_save("auto-test-email")

    with allure.step("Check"):
        expect(page.locator(BLOCK_RULE_MAIN_AREA).locator('[type="checkbox"]')).to_be_checked()
        expect(page.locator(BLOCK_RULES_LIST).locator('[type="checkbox"]')).to_be_checked()
        expect(page.locator('[aria-label="Remove auto_rule"]')).to_have_count(1)
        expect(page.locator(INPUT_COMMENT)).to_have_text("someText {{call_id}}")
        expect(page.locator(INPUT_NOTIFICATION_NAME)).to_have_value("auto-test-email")
        expect(page.locator(INPUT_LETTER_THEME)).to_have_value("letterTheme")
        expect(page.locator(INPUT_EMAIL)).to_have_value("mail@.mail.com")

    with allure.step("Delete rule"):
        delete_rule(page)

    with allure.step("Check that rule deleted"):
        expect(page.locator(BUTTON_KORZINA)).not_to_be_visible()

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.notifications
@allure.title("test_notifications_telegram")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_notifications_telegram")
def test_notifications_telegram(base_url,page: Page) -> None:
    notifications = Notifications(page)

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        notifications.navigate(base_url)

    with allure.step("Auth with user"):
        notifications.auth(LOGIN, PASSWORD)

    with allure.step("Go to notifications"):
        notifications.click_notifications()

    with allure.step("Create telegram notification rule"):
        notifications.add_notification("Telegram")

    with allure.step("Set notification name"):
        notifications.set_notification_name("auto-test-telegram")

    with allure.step("Checkbox send again when rule changed"):
        page.locator(BLOCK_RULE_MAIN_AREA).locator('[type="checkbox"]').nth(0).click()

    with allure.step("Check that checkbox clicked"):
        expect(page.locator(BLOCK_RULE_MAIN_AREA).locator('[type="checkbox"]').nth(0)).to_be_checked()

    with allure.step("Checkbox send audio with message"):
        page.locator(BLOCK_RULE_MAIN_AREA).locator('[type="checkbox"]').nth(1).click()

    with allure.step("Check that checkbox clicked"):
        expect(page.locator(BLOCK_RULE_MAIN_AREA).locator('[type="checkbox"]').nth(1)).to_be_checked()

    with allure.step("add filter"):
        add_filter("По тегам", "auto_rule", "1", page)

    with allure.step("Fill message"):
        notifications.fill_message("someText ")

    with allure.step("Save rule"):
        notifications.save_rule()

    with allure.step("Check alert"):
        notifications.check_alert("Данные сохранены")

    with allure.step("Go back in rule after save"):
        notifications.go_back_in_rule_after_save("auto-test-telegram")

    with allure.step("Check"):
        expect(page.locator(BLOCK_RULE_MAIN_AREA).locator('[type="checkbox"]').nth(0)).to_be_checked()
        expect(page.locator(BLOCK_RULE_MAIN_AREA).locator('[type="checkbox"]').nth(1)).to_be_checked()
        expect(page.locator('[aria-label="Remove auto_rule"]')).to_have_count(1)
        expect(page.locator(BLOCK_RULES_LIST).locator('[type="checkbox"]')).to_be_checked()
        expect(page.locator(INPUT_COMMENT)).to_have_text("someText {{call_id}}")
        expect(page.locator(INPUT_NOTIFICATION_NAME)).to_have_value("auto-test-telegram")

    with allure.step("Delete rule"):
        delete_rule(page)

    with allure.step("Check that rule deleted"):
        expect(page.locator(BUTTON_KORZINA)).not_to_be_visible()

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)



@pytest.mark.independent
@pytest.mark.notifications
@allure.title("test_notifications_amo_crm")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_notifications_amo_crm")
def est_notifications_amo_crm(base_url, page: Page) -> None:  # turn on later
    notifications = Notifications(page)

    with allure.step("Create admin"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    with allure.step("Go to url"):
        notifications.navigate(base_url)

    with allure.step("Auth with admin"):
        notifications.auth(LOGIN, PASSWORD)

    with allure.step("Go to user IMOT.IO"):
        notifications.go_to_user("IMOT.IO")

    with allure.step("Go to notifications"):
        notifications.click_notifications()

    with allure.step("Check that notification auto-test-amoCRM deleted before"):
        if page.get_by_text("auto-test-amoCRM").is_visible():
            notifications.go_back_in_rule_after_save("auto-test-amoCRM")
            page.locator('[class*="styles_selected_"]').locator(BUTTON_KORZINA).click()
            page.wait_for_timeout(500)
            page.locator(MODAL_WINDOW).get_by_role("button", name="Удалить").click()
            page.wait_for_timeout(2000)

    with allure.step("Create api notification rule"):
        notifications.add_notification("AmoCRM")

    with allure.step("Set notification name"):
        notifications.set_notification_name("auto-test-amoCRM")

    with allure.step("Checkbox Send again when rule changed"):
        page.locator(BLOCK_RULE_MAIN_AREA).locator('[type="checkbox"]').nth(0).click()

    with allure.step("Check that checkbox clicked"):
        expect(page.locator(BLOCK_RULE_MAIN_AREA).locator('[type="checkbox"]').nth(0)).to_be_checked()

    with allure.step("Checkbox Allow overwriting fields from CRM"):
        page.locator(BLOCK_RULE_MAIN_AREA).locator('[type="checkbox"]').nth(1).click()

    with allure.step("Check that checkbox clicked"):
        expect(page.locator(BLOCK_RULE_MAIN_AREA).locator('[type="checkbox"]').nth(1)).to_be_checked()

    with allure.step("add filter"):
        add_filter("По тегам", "Бренд", "1", page)

    with allure.step("Fill message"):
        notifications.fill_message("someText ")

    with allure.step("Save rule"):
        notifications.save_rule()

    with allure.step("Check alert"):
        notifications.check_alert("Данные сохранены")

    with allure.step("Go back in rule after save"):
        notifications.go_back_in_rule_after_save("auto-test-amoCRM")

    with allure.step("Check"):
        expect(page.locator(BLOCK_RULE_MAIN_AREA).locator('[type="checkbox"]').nth(0)).to_be_checked()
        expect(page.locator(BLOCK_RULE_MAIN_AREA).locator('[type="checkbox"]').nth(1)).to_be_checked()
        expect(page.locator('[aria-label="Remove Бренд"]')).to_have_count(1)
        expect(page.locator(INPUT_COMMENT)).to_have_text("someText {{call_id}}")
        expect(page.locator(INPUT_NOTIFICATION_NAME)).to_have_value("auto-test-amoCRM")

    with allure.step("Delete rule"):
        #delete_rule(page)
        page.locator('[class*="styles_selected_"]').locator(BUTTON_KORZINA).click()
        page.wait_for_timeout(500)
        page.locator(MODAL_WINDOW).get_by_role("button", name="Удалить").click()
        page.wait_for_timeout(1000)

    with allure.step("Check that rule deleted"):
        expect(page.locator(BUTTON_KORZINA)).to_have_count(2)

    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.notifications
@allure.title("test_notifications_import_rules_by_admin")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_notifications_import_rules_by_admin")
def test_notifications_import_rules_by_admin(base_url, page: Page) -> None:
    notifications = Notifications(page)

    with allure.step("Create admin"):
        USER_ID_ADMIN, TOKEN_ADMIN, LOGIN_ADMIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    with allure.step("Create user for import"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        notifications.navigate(base_url)

    with allure.step("Auth with admin"):
        notifications.auth(LOGIN_ADMIN, PASSWORD)

    with allure.step("Go to user"):
        notifications.go_to_user(LOGIN_USER)

    with allure.step("Go to notifications page"):
        notifications.click_notifications()

    with allure.step("Press button import notifications"):
        page.locator(BUTTON_IMPORT_RULES).get_by_role("button").click()
        page.wait_for_selector(SEARCH_IN_IMPORT_MODAL)

    with allure.step("Choose user import from"):
        page.locator('[class*="CustomSelect_simpleSelect"]').locator('[type="text"]').fill("importFrom")
        page.wait_for_timeout(500)
        page.locator(MENU).get_by_text("importFrom", exact=True).click()
        page.wait_for_timeout(1000)

    with allure.step("Import first rule"):
        page.locator('[aria-label="Импортировать"]').locator('[type="checkbox"]').nth(0).click()

    with allure.step("Press (Go on) button"):
        page.locator(BLOCK_AFTER_IMPORT).get_by_role("button", name="Продолжить").click()

    with allure.step("Import second rule"):
        page.locator('[aria-label="Импортировать"]').locator('[type="checkbox"]').nth(1).click()

    with allure.step("Go to new rules"):
        page.locator(BLOCK_AFTER_IMPORT).get_by_role("button", name="К новым правилам").click()
        page.wait_for_timeout(1800)

    with allure.step("Check that import was successful"):
        expect(page.get_by_text("pochta")).to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("telega")).to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete first rule"):
        delete_rule(page)

    with allure.step("Check that first rule deleted"):
        expect(page.locator(MODAL_WINDOW)).not_to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("pochta")).not_to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete second rule"):
        delete_rule(page)

    with allure.step("Check that first rule deleted"):
        expect(page.locator(MODAL_WINDOW)).not_to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("telega")).not_to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN_ADMIN, USER_ID_ADMIN)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)


@pytest.mark.independent
@pytest.mark.notifications
@allure.title("test_notifications_import_rules_by_manager")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_notifications_import_rules_by_manager")
def test_notifications_import_rules_by_manager(base_url, page: Page) -> None:
    notifications = Notifications(page)

    with allure.step("Create manager"):
        USER_ID_MANAGER, TOKEN_MANAGER, LOGIN_MANAGER = create_user(API_URL, ROLE_MANAGER, PASSWORD)

    with allure.step("Create user for import"):
        USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Give user to manager"):
        give_user_to_manager(API_URL, USER_ID_MANAGER, USER_ID_USER, TOKEN_MANAGER)

    with allure.step("Go to url"):
        notifications.navigate(base_url)

    with allure.step("Auth with manager"):
        notifications.auth(LOGIN_MANAGER, PASSWORD)

    with allure.step("Go to user"):
        notifications.go_to_user(LOGIN_USER)

    with allure.step("Go to notifications page"):
        notifications.click_notifications()

    with allure.step("Press button import notifications"):
        page.locator(BUTTON_IMPORT_RULES).get_by_role("button").click()
        page.wait_for_selector('[data-testid="NotifyRuleCopyMode_search"]')

    with allure.step("Choose user import from"):
        page.locator('[class*="CustomSelect_simpleSelect"]').locator('[type="text"]').fill("importFrom")
        page.wait_for_timeout(500)
        page.locator(MENU).get_by_text("importFrom", exact=True).click()
        page.wait_for_timeout(1000)

    with allure.step("Import first rule"):
        page.locator('[aria-label="Импортировать"]').locator('[type="checkbox"]').nth(0).click()
        page.wait_for_timeout(500)

    with allure.step("Press (Go on) button"):
        page.locator(BLOCK_AFTER_IMPORT).get_by_role("button", name="Продолжить").click()
        page.wait_for_timeout(500)

    with allure.step("Import second rule"):
        page.locator('[aria-label="Импортировать"]').locator('[type="checkbox"]').nth(1).click()
        page.wait_for_timeout(500)

    with allure.step("Go to new rules"):
        page.locator(BLOCK_AFTER_IMPORT).get_by_role("button", name="К новым правилам").click()
        page.wait_for_timeout(1600)

    with allure.step("Check that import was successful"):
        expect(page.get_by_text("pochta")).to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("telega")).to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete first rule"):
        delete_rule(page)

    with allure.step("Check that first rule deleted"):
        expect(page.locator(MODAL_WINDOW)).not_to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("pochta")).not_to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete second rule"):
        delete_rule(page)

    with allure.step("Check that first rule deleted"):
        expect(page.locator(MODAL_WINDOW)).not_to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("telega")).not_to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete manager"):
        delete_user(API_URL, TOKEN_MANAGER, USER_ID_MANAGER)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN_USER, USER_ID_USER)


@pytest.mark.independent
@pytest.mark.notifications
@allure.title("test_check_old_notification")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_check_old_notification for Ecotelecom")
def test_check_old_notification(base_url, page: Page) -> None:
    notifications = Notifications(page)

    with allure.step("Go to url"):
        notifications.navigate(base_url)

    with allure.step("Auth with Ecotelecom"):
        notifications.auth(ECOTELECOM, ECOPASS)

    with allure.step("Go to notifications"):
        notifications.click_notifications()

    with allure.step("Click at first Ecotelecom rule"):
        page.locator(BLOCK_RULES_LIST).locator('[class*="styles_content__"]').first.click()
        page.wait_for_selector(INPUT_COMMENT, timeout=wait_until_visible)

    with allure.step("Check that first Ecotelecom rule opened"):
        expect(page.locator(INPUT_COMMENT)).to_be_visible()
        expect(page.locator(BLOCK_RULE_MAIN_AREA)).to_be_visible()