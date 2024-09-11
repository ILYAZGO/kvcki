from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.users import *
from utils.create_delete_user import create_user, delete_user, give_manager_all_rights
import pytest
import allure
import random


@pytest.mark.independent
@pytest.mark.users
@allure.title("test_add_delete_admin_by_admin")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_delete_admin_by_admin(base_url, page: Page) -> None:
    NEW_NAME = NEW_LOGIN = f"auto_test_user_{datetime.now().strftime('%m%d%H%M')}{datetime.now().microsecond}"
    EMAIL = f"email_{datetime.now().microsecond}{random.randint(100, 200)}@mail.ru"
    PHONE = str(random.randint(10000000000, 99999999999))

    with allure.step("Create admin 1"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with admin 1"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to users"):
        go_to_users(page)
        page.wait_for_selector(FIRST_ROW_IN_USERS_LIST, timeout=wait_until_visible)

    with allure.step("Press button (Add User)"):
        press_button_add_user(page)

    with allure.step("Set admin 2 info"):
        set_user(NEW_NAME,
                 NEW_LOGIN,
                 PASSWORD,
                 EMAIL,
                 PHONE,
                 "someComment",
                 "Администратор",
                 page)

    with allure.step("Press button (Add) in modal window"):
        press_button_add_in_modal(page)
        page.wait_for_selector('[class*="PersonalInfo_form"]', timeout=wait_until_visible)

    with allure.step("Check"):
        expect(page.locator(INPUT_NAME)).to_have_value(NEW_NAME, timeout=wait_until_visible)
        expect(page.locator(INPUT_LOGIN)).to_have_value(NEW_LOGIN, timeout=wait_until_visible)
        expect(page.locator(INPUT_EMAIL)).to_have_value(EMAIL, timeout=wait_until_visible)
        expect(page.locator(INPUT_COMMENT)).to_have_text("someComment", timeout=wait_until_visible)
        expect(page.locator(SELECT_ROLE)).to_have_text("Администратор", timeout=wait_until_visible)
        page.wait_for_timeout(500)
        expect(page.locator(INPUT_PHONE)).to_have_value(PHONE)
        expect(page.locator(INPUT_NEW_PASSWORD)).to_be_visible(timeout=wait_until_visible)
        expect(page.locator(INPUT_NEW_PASSWORD_REPEAT)).to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete admin 2"):
        delete_added_user(page)

    with allure.step("Check that admin 2 deleted"):
        expect(page.locator(INPUT_LOGIN)).to_have_value(LOGIN, timeout=wait_until_visible)

    with allure.step("Delete admin 1"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.users
@allure.title("test_add_delete_manager_by_admin")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_delete_manager_by_admin(base_url, page: Page) -> None:
    NEW_NAME = NEW_LOGIN = f"auto_test_user_{datetime.now().strftime('%m%d%H%M')}{datetime.now().microsecond}"
    EMAIL = f"email_{datetime.now().microsecond}{random.randint(100, 200)}@mail.ru"
    PHONE = str(random.randint(10000000000, 99999999999))

    with allure.step("Create admin"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with admin"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to users"):
        go_to_users(page)
        page.wait_for_selector(FIRST_ROW_IN_USERS_LIST, timeout=wait_until_visible)

    with allure.step("Press button (Add User)"):
        press_button_add_user(page)

    with allure.step("Set manager info"):
        set_user(NEW_NAME,
                 NEW_LOGIN,
                 PASSWORD,
                 EMAIL,
                 PHONE,
                 "someComment",
                 "Интегратор",
                 page)

    with allure.step("Press button (Add) in modal window"):
        press_button_add_in_modal(page)
        page.wait_for_selector(INPUT_PHONE, timeout=wait_until_visible)

    with allure.step("Check"):
        expect(page.locator(INPUT_LOGIN)).to_have_value(NEW_LOGIN, timeout=wait_until_visible)
        expect(page.locator(INPUT_NAME)).to_have_value(NEW_NAME, timeout=wait_until_visible)
        expect(page.locator(INPUT_EMAIL)).to_have_value(EMAIL, timeout=wait_until_visible)
        expect(page.locator(INPUT_COMMENT)).to_have_text("someComment", timeout=wait_until_visible)
        expect(page.locator(SELECT_ROLE)).to_have_text("Интегратор", timeout=wait_until_visible)
        expect(page.locator(INPUT_PHONE)).to_have_value(PHONE)
        expect(page.locator(INPUT_NEW_PASSWORD)).to_be_visible(timeout=wait_until_visible)
        expect(page.locator(INPUT_NEW_PASSWORD_REPEAT)).to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete added manager"):
        delete_added_user(page)

    with allure.step("Check that manager deleted"):
        expect(page.locator(INPUT_LOGIN)).to_have_value(LOGIN, timeout=wait_until_visible)

    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.users
@allure.title("test_add_delete_user_by_admin")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_delete_user_by_admin(base_url, page: Page) -> None:
    NEW_NAME = NEW_LOGIN = f"auto_test_user_{datetime.now().strftime('%m%d%H%M')}{datetime.now().microsecond}"
    EMAIL = f"email_{datetime.now().microsecond}{random.randint(100, 200)}@mail.ru"
    PHONE = str(random.randint(10000000000, 99999999999))

    with allure.step("Create admin"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with admin"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to users"):
        go_to_users(page)
        page.wait_for_selector(FIRST_ROW_IN_USERS_LIST, timeout=wait_until_visible)

    #
    with allure.step("Press button (Add User)"):
        press_button_add_user(page)

    with allure.step("Cancel by button CANCEL"):
        page.locator(BUTTON_OTMENA).click()

    with allure.step("Check"):
        expect(page.locator(INPUT_PASSWORD)).not_to_be_visible()

    with allure.step("Press button (Add User)"):
        press_button_add_user(page)

    with allure.step("Cancel by button KRESTIK"):
        page.locator(BUTTON_KRESTIK).click()

    with allure.step("Check"):
        expect(page.locator(INPUT_PASSWORD)).not_to_be_visible()
    #

    with allure.step("Press button (Add User)"):
        press_button_add_user(page)

    with allure.step("Set user info"):
        set_user(NEW_NAME,
                 NEW_LOGIN,
                 PASSWORD,
                 EMAIL,
                 PHONE,
                 "someComment",
                 "Компания",
                 page)

    with allure.step("Set industry and partner for user"):
        set_industry_and_partner("Недвижимость",
                                 "managerIM",
                                 page)

    with allure.step("Set STT for user"):
        set_stt("Русский",
                "Deepgram",
                "whisper",
                page)

    with allure.step("Press button (Add) in modal window"):
        press_button_add_in_modal(page)
        page.wait_for_selector(INPUT_PHONE, timeout=wait_until_visible)

    with allure.step("Check"):
        expect(page.locator(INPUT_LOGIN)).to_have_value(NEW_LOGIN, timeout=wait_until_visible)
        expect(page.locator(INPUT_NAME)).to_have_value(NEW_NAME, timeout=wait_until_visible)
        expect(page.locator(INPUT_EMAIL)).to_have_value(EMAIL, timeout=wait_until_visible)
        #page.wait_for_timeout(2300)
        expect(page.locator(INPUT_COMMENT)).to_have_text("someComment", timeout=wait_until_visible)
        expect(page.locator(SELECT_ROLE)).to_have_text("Компания", timeout=wait_until_visible)
        expect(page.locator(SELECT_INDUSTRY)).to_have_text("Недвижимость", timeout=wait_until_visible)
        expect(page.locator(SELECT_PARTNER)).to_have_text("managerIM", timeout=wait_until_visible)
        expect(page.locator(INPUT_PHONE)).to_have_value(PHONE)
        expect(page.locator(INPUT_NEW_PASSWORD)).to_be_visible(timeout=wait_until_visible)
        expect(page.locator(INPUT_NEW_PASSWORD_REPEAT)).to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete added user"):
        delete_added_user(page)

    with allure.step("Check that user deleted"):
        expect(page.locator(INPUT_LOGIN)).to_have_value(LOGIN, timeout=wait_until_visible)

    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.users
@allure.title("test_add_user_disabled_for_manager_without_right")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_add_user_disabled_for_manager_without_right")
def test_add_user_disabled_for_manager_without_right(base_url, page: Page) -> None:

    with allure.step("Create manager without right to add"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_MANAGER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with admin"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to users"):
        go_to_users(page)

    with allure.step("Check"):
        expect(page.locator(BUTTON_DOBAVIT_POLZOVATELIA)).to_be_disabled()
        expect(page.locator('[class="rs-table-body-info"]')).to_contain_text("Информация отсутствует")

    with allure.step("Delete manager"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.users
@allure.title("test_add_delete_user_by_manager")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Precondition : manager should have access_rights for create and delete user")
def test_add_delete_user_by_manager(base_url, page: Page) -> None:
    NEW_NAME = NEW_LOGIN = f"auto_test_user_{datetime.now().strftime('%m%d%H%M')}{datetime.now().microsecond}"
    EMAIL = f"email_{datetime.now().microsecond}{random.randint(100, 200)}@mail.ru"
    PHONE = str(random.randint(10000000000, 99999999999))

    with allure.step("Create manager without right to add"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_MANAGER, PASSWORD)

    with allure.step("Give created manager all rights"):
        give_manager_all_rights(API_URL, USER_ID, TOKEN)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with manager"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to users"):
        go_to_users(page)

    with allure.step("Press button (Add User)"):
        press_button_add_user(page)

    with allure.step("Set user info"):
        set_user(NEW_NAME,
                 NEW_LOGIN,
                 PASSWORD,
                 EMAIL,
                 PHONE,
                 "someComment",
                 "Компания",
                 page)

    with allure.step("Check that select partner not available"):
        expect(page.locator(SELECT_PARTNER)).not_to_be_visible(timeout=wait_until_visible)

    with allure.step("Set industry"):
        set_industry("Недвижимость", page)

    with allure.step("Set STT"):
        set_stt("Русский",
                "IMOT.IO",
                "Стандарт",
                 page)

    with allure.step("Press button (Add) in modal window"):
        press_button_add_in_modal(page)
        page.wait_for_selector(INPUT_PHONE, timeout=wait_until_visible)

    with allure.step("Check"):
        expect(page.locator(INPUT_LOGIN)).to_have_value(NEW_LOGIN, timeout=wait_until_visible)
        expect(page.locator(INPUT_NAME)).to_have_value(NEW_NAME, timeout=wait_until_visible)
        expect(page.locator(INPUT_EMAIL)).to_have_value(EMAIL, timeout=wait_until_visible)
        page.wait_for_timeout(3400)
        expect(page.get_by_text("Компания")).to_have_count(1, timeout=wait_until_visible)
        expect(page.get_by_text("Недвижимость")).to_have_count(1, timeout=wait_until_visible)
        expect(page.locator(INPUT_PHONE)).to_have_value(PHONE)
        expect(page.locator(INPUT_NEW_PASSWORD)).to_be_visible(timeout=wait_until_visible)
        expect(page.locator(INPUT_NEW_PASSWORD_REPEAT)).to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete added user"):
        delete_added_user(page)

    with allure.step("Check that user deleted"):
        expect(page.locator(INPUT_LOGIN)).to_have_value(LOGIN, timeout=wait_until_visible)

    with allure.step("Delete manager"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.users
@allure.title("test_add_delete_operator_by_user")
@allure.severity(allure.severity_level.NORMAL)
def test_add_delete_operator_by_user(base_url, page: Page) -> None:
    NEW_OPERATOR_NAME = NEW_OPERATOR_LOGIN = f"auto_test_operator_{datetime.now().strftime('%m%d%H%M')}_{datetime.now().microsecond}"
    EMAIL = f"email_{datetime.now().microsecond}{random.randint(100, 200)}@mail.ru"
    PHONE = str(random.randint(10000000000, 99999999999))

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with user"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to settings"):
        page.locator(BUTTON_NASTROIKI).click()

    with allure.step("Go to employees"):
        page.locator(BUTTON_SOTRUDNIKI).click()

    with allure.step("Press button (Add employee)"):
        press_button_add_employee(page)

    with allure.step("Set operator info"):
        set_operator(NEW_OPERATOR_NAME,
                     NEW_OPERATOR_LOGIN,
                     PASSWORD,
                     PHONE,
                     EMAIL,
                     EMAIL,
                     page)
    with allure.step("Press button (Add) in modal window"):
        press_button_add_in_modal(page)

    with allure.step("Check"):
        expect(page.locator(INPUT_NAME)).to_have_value(NEW_OPERATOR_NAME, timeout=wait_until_visible)
        expect(page.locator(INPUT_LOGIN)).to_have_value(NEW_OPERATOR_LOGIN, timeout=wait_until_visible)
        expect(page.locator(INPUT_PHONE)).to_have_value(PHONE, timeout=wait_until_visible)
        expect(page.locator(INPUT_EMAIL)).to_have_value(EMAIL, timeout=wait_until_visible)
        #expect(page.locator(INPUT_COMMENT)).to_have_text(EMAIL7, timeout=wait_until_visible)
        expect(page.locator(INPUT_PHONE)).to_be_visible(timeout=wait_until_visible)
        expect(page.locator(INPUT_NEW_PASSWORD)).to_be_visible(timeout=wait_until_visible)
        expect(page.locator(INPUT_NEW_PASSWORD_REPEAT)).to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete added employee"):
        delete_added_user(page)

    with allure.step("Check that employee deleted"):
        expect(page.locator(BUTTON_DOBAVIT_SOTRUDNIKA)).to_be_visible(timeout=wait_until_visible)
        expect(page.locator(USER_LOGIN_IN_LEFT_MENU)).to_have_text(LOGIN, timeout=wait_until_visible)

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.users
@allure.title("test_check_search")
@allure.severity(allure.severity_level.NORMAL)
def test_check_search(base_url, page: Page) -> None:

    with allure.step("Create admin"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with admin"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to users"):
        go_to_users(page)
        page.wait_for_selector(FIRST_ROW_IN_USERS_LIST, timeout=wait_until_visible)

    with allure.step("Fill searchString"):
        page.locator(INPUT_POISK).fill("ecot")

    with allure.step("Check ecotelecom visible and 1userIM not visible"):
        expect(page.get_by_text("ecotelecom")).to_be_visible(timeout=wait_until_visible)
        expect(page.get_by_text("1userIM")).not_to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.independent
@pytest.mark.users
@allure.title("test_check_stt_parameters_when_adding_user")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Admin checking all stt parameters while adding new user ")
def test_check_stt_parameters_when_adding_user(base_url, page: Page) -> None:
    NEW_NAME = NEW_LOGIN = f"auto_test_user_{datetime.now().strftime('%m%d%H%M')}{datetime.now().microsecond}"
    EMAIL = f"email_{datetime.now().microsecond}{random.randint(100, 200)}@mail.ru"
    PHONE = str(random.randint(10000000000, 99999999999))

    expected_languages = ("Английский (Великобритания)Английский (США)Испанский (Латинская Америка, Карибский регион, "
                          "код региона UN M49)Испанский (Испания)Французский (Франция)Португальский "
                          "(Бразилия)Португальский (Португалия)РусскийТурецкий (Турция)УкраинскийУзбекскийАвто")

    expected_engines = "DeepgramHappyscribeNLab SpeechIMOT.IOЯндексyandex_v3"

    alert_merge = "Опция 'Объединить дорожки в один файл' не может быть выбрана одновременно с любой из диаризаций"

    alert_diarization = "Выберите только одну диаризацию среди опций"

    action_started = "Пользователь успешно добавлен"

    with allure.step("Create admin"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    with allure.step("Go to url"):
        page.goto(base_url, timeout=wait_until_visible)

    with allure.step("Auth with admin"):
        auth(LOGIN, PASSWORD, page)

    with allure.step("Go to users"):
        go_to_users(page)
        page.wait_for_selector(FIRST_ROW_IN_USERS_LIST, timeout=wait_until_visible)

    with allure.step("Press button (Add User)"):
        press_button_add_user(page)

    with allure.step("Set user info"):
        set_user(NEW_NAME,
                 NEW_LOGIN,
                 PASSWORD,
                 EMAIL,
                 PHONE,
                 "someComment",
                 "Компания",
                 page)

    #  check all combinations of engines and models

    with allure.step("Click to language"):
        page.locator(SELECT_LANGUAGE).locator('[type="text"]').click()
        page.wait_for_selector(SELECT_MENU)

    with allure.step("Check language list"):
        expect(page.locator(SELECT_MENU)).to_contain_text(expected_languages)

    with allure.step("Choose russian language"):
        choose_option(7, page)

    with allure.step("Click to engine"):
        click_engine_select(page)

    with allure.step("Check engine list"):
        expect(page.locator(SELECT_MENU)).to_contain_text(expected_engines)


    # DELETE
    # with allure.step("Choose any2text"):
    #     choose_option(0, page)
    #
    # with allure.step("Click to model"):
    #     click_model_select(page)
    #
    # with allure.step("Check model list"):
    #     expect(page.locator(SELECT_MENU)).to_contain_text("Стандарт")
    #
    # with allure.step("Select model"):
    #     choose_option(0, page)
    #
    # with allure.step("Check engine parameters"):
    #     expect(page.locator(SELECT_ENGINE)).to_contain_text("any2text")
    #     expect(page.locator(SELECT_MODEL)).to_contain_text("Стандарт")
    #     expect(page.locator(CHECKBOX_MERGE_ALL_TO_ONE)).not_to_be_checked()
    #     expect(page.locator(RECOGNITION_PRIORITY).locator('[type="number"]')).to_have_value("1")
    #     expect(page.locator(CHECKBOX_DIARIZATION)).not_to_be_checked()
    #     expect(page.locator(CHECKBOX_ECONOMIZE)).not_to_be_checked()
    #     expect(page.locator('[type="checkbox"]')).to_have_count(3)
    # DELETE

    # with allure.step("Click to engine"):
    #     click_engine_select(page)
    #
    # with allure.step("Choose assembly_ai"):
    #     choose_option(1, page)
    #
    # with allure.step("Click to model"):
    #     click_model_select(page)
    #
    # with allure.step("Check model list"):
    #     expect(page.locator(SELECT_MENU)).to_contain_text("bestconformer-2nano")
    #
    # with allure.step("Select model best"):
    #     choose_option(0, page)
    #
    # with allure.step("Click to model"):
    #     click_model_select(page)
    #
    # with allure.step("Select model conformer-2"):
    #     choose_option(1, page)
    #
    # with allure.step("Click to model"):
    #     click_model_select(page)
    #
    # with allure.step("Select model nano"):
    #     choose_option(2, page)
    #
    # with allure.step("Check engine parameters"):
    #     expect(page.locator(SELECT_ENGINE)).to_contain_text("assembly_ai")
    #     expect(page.locator(SELECT_MODEL)).to_contain_text("nano")
    #     expect(page.locator(CHECKBOX_MERGE_ALL_TO_ONE)).not_to_be_checked()
    #     expect(page.locator(RECOGNITION_PRIORITY).locator('[type="number"]')).to_have_value("1")
    #     expect(page.locator(CHECKBOX_DIARIZATION)).not_to_be_checked()
    #     expect(page.locator(CHECKBOX_USE_WEBHOOK)).not_to_be_checked()
    #     expect(page.locator(CHECKBOX_ADD_PUNCTUATION)).to_be_checked()
    #     expect(page.locator(CHECKBOX_ENGINE_DIARIZATION)).to_be_checked()
    #     expect(page.locator(CHECKBOX_ECONOMIZE)).not_to_be_checked()
    #     expect(page.locator('[type="checkbox"]')).to_have_count(6)

    # DELETE
    # with allure.step("Click to engine"):
    #     click_engine_select(page)
    #
    # with allure.step("Choose ClaritySpeech"):
    #     choose_option(2, page)
    #
    # with allure.step("Click to model"):
    #     click_model_select(page)
    #
    # with allure.step("Check model list"):
    #     expect(page.locator(SELECT_MENU)).to_contain_text("СтандартАЗС")
    #
    # with allure.step("Select model Стандарт"):
    #     choose_option(0, page)
    #
    # with allure.step("Click to model"):
    #     click_model_select(page)
    #
    # with allure.step("Select model АЗС"):
    #     choose_option(1, page)
    #
    # with allure.step("Check engine parameters"):
    #     expect(page.locator(SELECT_ENGINE)).to_contain_text("ClaritySpeech")
    #     expect(page.locator(SELECT_MODEL)).to_contain_text("АЗС")
    #     expect(page.locator(CHECKBOX_MERGE_ALL_TO_ONE)).not_to_be_checked()
    #     expect(page.locator(RECOGNITION_PRIORITY).locator('[type="number"]')).to_have_value("1")
    #     expect(page.locator(CHECKBOX_DIARIZATION)).not_to_be_checked()
    #     expect(page.locator(CHECKBOX_USE_WEBHOOK)).not_to_be_checked()
    #     expect(page.locator(CHECKBOX_ECONOMIZE)).not_to_be_checked()
    #     expect(page.locator('[type="checkbox"]')).to_have_count(4)
    # DELETE

    with allure.step("Click to engine"):
        click_engine_select(page)

    with allure.step("Choose Deepgram"):
        choose_option(0, page)

    with allure.step("Click to model"):
        click_model_select(page)

    with allure.step("Check model list"):
        expect(page.locator(SELECT_MENU)).to_contain_text("Обобщённаяwhisper")

    with allure.step("Select model Обобщённая"):
        choose_option(0, page)

    with allure.step("Click to model"):
        click_model_select(page)

    with allure.step("Select model whisper"):
        choose_option(1, page)

    with allure.step("Check engine parameters"):
        expect(page.locator(SELECT_ENGINE)).to_contain_text("Deepgram")
        expect(page.locator(SELECT_MODEL)).to_contain_text("whisper")
        expect(page.locator(CHECKBOX_MERGE_ALL_TO_ONE)).not_to_be_checked()
        expect(page.locator(RECOGNITION_PRIORITY).locator('[type="number"]')).to_have_value("1")
        expect(page.locator(CHECKBOX_DIARIZATION)).not_to_be_checked()
        expect(page.locator(CHECKBOX_ECONOMIZE)).not_to_be_checked()
        expect(page.locator('[type="checkbox"]')).to_have_count(3)

    with allure.step("Click to engine"):
        click_engine_select(page)

    with allure.step("Choose Happyscribe"):
        choose_option(1, page)

    with allure.step("Click to model"):
        click_model_select(page)

    with allure.step("Check model list"):
        expect(page.locator(SELECT_MENU)).to_contain_text("Стандарт")

    with allure.step("Select model Стандарт"):
        choose_option(0, page)

    with allure.step("Check engine parameters"):
        expect(page.locator(SELECT_ENGINE)).to_contain_text("Happyscribe")
        expect(page.locator(SELECT_MODEL)).to_contain_text("Стандарт")
        expect(page.locator(CHECKBOX_MERGE_ALL_TO_ONE)).not_to_be_checked()
        expect(page.locator(RECOGNITION_PRIORITY).locator('[type="number"]')).to_have_value("1")
        expect(page.locator(CHECKBOX_DIARIZATION)).not_to_be_checked()
        expect(page.locator(CHECKBOX_ECONOMIZE)).not_to_be_checked()
        expect(page.locator('[type="checkbox"]')).to_have_count(3)

    with allure.step("Click to engine"):
        click_engine_select(page)

    with allure.step("Choose NLab Speech"):
        choose_option(2, page)

    with allure.step("Click to model"):
        click_model_select(page)

    with allure.step("Check model list"):
        expect(page.locator(SELECT_MENU)).to_contain_text("ОбобщённаяЖадный")

    with allure.step("Select model Обобщённая"):
        choose_option(0, page)

    with allure.step("Click to model"):
        click_model_select(page)

    with allure.step("Select model Жадный"):
        choose_option(1, page)

    with allure.step("Check engine parameters"):
        expect(page.locator(SELECT_ENGINE)).to_contain_text("NLab Speech")
        expect(page.locator(SELECT_MODEL)).to_contain_text("Жадный")
        expect(page.locator(CHECKBOX_MERGE_ALL_TO_ONE)).not_to_be_checked()
        expect(page.locator(RECOGNITION_PRIORITY).locator('[type="number"]')).to_have_value("1")
        expect(page.locator(CHECKBOX_DIARIZATION)).not_to_be_checked()
        expect(page.locator(CHECKBOX_ECONOMIZE)).not_to_be_checked()
        expect(page.locator('[type="checkbox"]')).to_have_count(3)

    # DELETE
    # with allure.step("Click to engine"):
    #     click_engine_select(page)
    #
    # with allure.step("Choose Sova ASR"):
    #     choose_option(6, page)
    #
    # with allure.step("Click to model"):
    #     click_model_select(page)
    #
    # with allure.step("Check model list"):
    #     expect(page.locator(SELECT_MENU)).to_contain_text("Стандарт")
    #
    # with allure.step("Select model Стандарт"):
    #     choose_option(0, page)
    #
    # with allure.step("Check engine parameters"):
    #     expect(page.locator(SELECT_ENGINE)).to_contain_text("Sova ASR")
    #     expect(page.locator(SELECT_MODEL)).to_contain_text("Стандарт")
    #     expect(page.locator(CHECKBOX_MERGE_ALL_TO_ONE)).not_to_be_checked()
    #     expect(page.locator(RECOGNITION_PRIORITY).locator('[type="number"]')).to_have_value("1")
    #     expect(page.locator(CHECKBOX_DIARIZATION)).not_to_be_checked()
    #     expect(page.locator(CHECKBOX_ECONOMIZE)).not_to_be_checked()
    #     expect(page.locator('[type="checkbox"]')).to_have_count(3)
    # DELETE


    with allure.step("Click to engine"):
        click_engine_select(page)

    with allure.step("Choose IMOT.IO"):
        choose_option(3, page)

    with allure.step("Click to model"):
        click_model_select(page)

    with allure.step("Check model list"):
        expect(page.locator(SELECT_MENU)).to_contain_text("Стандарт")

    with allure.step("Select model Стандарт"):
        choose_option(0, page)

    with allure.step("Check engine parameters"):
        expect(page.locator(SELECT_ENGINE)).to_contain_text("IMOT.IO")
        expect(page.locator(SELECT_MODEL)).to_contain_text("Стандарт")
        expect(page.locator(CHECKBOX_MERGE_ALL_TO_ONE)).not_to_be_checked()
        expect(page.locator(RECOGNITION_PRIORITY).locator('[type="number"]')).to_have_value("1")
        expect(page.locator(CHECKBOX_DIARIZATION)).not_to_be_checked()
        expect(page.locator(CHECKBOX_ECONOMIZE)).not_to_be_checked()
        expect(page.locator('[type="checkbox"]')).to_have_count(3)
    # DELETE
    # with allure.step("Click to engine"):
    #     click_engine_select(page)
    #
    # with allure.step("Choose whisper"):
    #     choose_option(8, page)
    #
    # with allure.step("Click to model"):
    #     click_model_select(page)
    #
    # with allure.step("Check model list"):
    #     expect(page.locator(SELECT_MENU)).to_contain_text("Стандарт")
    #
    # with allure.step("Select model Стандарт"):
    #     choose_option(0, page)
    #
    # with allure.step("Check engine parameters"):
    #     expect(page.locator(SELECT_ENGINE)).to_contain_text("whisper")
    #     expect(page.locator(SELECT_MODEL)).to_contain_text("Стандарт")
    #     expect(page.locator(CHECKBOX_MERGE_ALL_TO_ONE)).not_to_be_checked()
    #     expect(page.locator(RECOGNITION_PRIORITY).locator('[type="number"]')).to_have_value("1")
    #     expect(page.locator(CHECKBOX_DIARIZATION)).not_to_be_checked()
    #     expect(page.locator(CHECKBOX_ECONOMIZE)).not_to_be_checked()
    #     expect(page.locator('[type="checkbox"]')).to_have_count(3)
    # DELETE

    with allure.step("Click to engine"):
        click_engine_select(page)

    with allure.step("Choose Яндекс"):
        choose_option(4, page)

    with allure.step("Click to model"):
        click_model_select(page)

    with allure.step("Check model list"):
        expect(page.locator(SELECT_MENU)).to_contain_text("Отложенная обобщённаяОбобщённая")

    with allure.step("Select model Отложенная обобщённая"):
        choose_option(0, page)

    with allure.step("Click to model"):
        click_model_select(page)

    with allure.step("Select model Обобщённая"):
        choose_option(1, page)

    with allure.step("Check engine parameters"):
        expect(page.locator(SELECT_ENGINE)).to_contain_text("Яндекс")
        expect(page.locator(SELECT_MODEL)).to_contain_text("Обобщённая")
        expect(page.locator(CHECKBOX_MERGE_ALL_TO_ONE)).to_be_checked()
        expect(page.locator(RECOGNITION_PRIORITY).locator('[type="number"]')).to_have_value("1")
        expect(page.locator(CHECKBOX_DIARIZATION)).not_to_be_checked()
        expect(page.locator(CHECKBOX_ECONOMIZE)).not_to_be_checked()
        expect(page.locator('[type="checkbox"]')).to_have_count(3)

    with allure.step("Click to engine"):
        click_engine_select(page)

    with allure.step("Choose yandex_v3"):
        choose_option(5, page)

    with allure.step("Click to model"):
        click_model_select(page)

    with allure.step("Check model list"):
        expect(page.locator(SELECT_MENU)).to_contain_text("Отложенная обобщённаяОбобщённая")

    with allure.step("Select model Отложенная обобщённая"):
        choose_option(0, page)

    with allure.step("Click to model"):
        click_model_select(page)

    with allure.step("Select model Обобщённая"):
        choose_option(1, page)

    with allure.step("Check engine parameters"):
        expect(page.locator(SELECT_ENGINE)).to_contain_text("yandex_v3")
        expect(page.locator(SELECT_MODEL)).to_contain_text("Обобщённая")
        expect(page.locator(CHECKBOX_MERGE_ALL_TO_ONE)).to_be_checked()
        expect(page.locator(RECOGNITION_PRIORITY).locator('[type="number"]')).to_have_value("1")
        expect(page.locator(CHECKBOX_DIARIZATION)).not_to_be_checked()
        expect(page.locator(CHECKBOX_ENGINE_DIARIZATION)).to_be_checked()
        expect(page.locator(CHECKBOX_ECONOMIZE)).not_to_be_checked()
        expect(page.locator(CHECKBOX_NORMALIZATION)).not_to_be_checked()
        expect(page.locator(CHECKBOX_PROFANITY_FILTER)).not_to_be_checked()
        expect(page.locator(CHECKBOX_LITERATURE_STYLE)).not_to_be_checked()
        expect(page.locator(CHECKBOX_PHONE_FORMATTING)).to_be_checked()
        expect(page.locator('[type="checkbox"]')).to_have_count(8)

    #  check save combinations

    with allure.step("Click to engine"):
        click_engine_select(page)

    with allure.step("Choose assembly_ai"):
        choose_option(5, page)

    with allure.step("Click to model"):
        click_model_select(page)

    with allure.step("Select model best"):
        choose_option(0, page)

    with allure.step("Check merge all to one checkbox"):
        page.locator(CHECKBOX_MERGE_ALL_TO_ONE).set_checked(checked=True)

    with allure.step("Try to save"):
        page.locator(BUTTON_DOBAVIT).click()

    with allure.step("Wait for alert and check alert message"):
        page.wait_for_selector(ALERT, timeout=wait_until_visible)
        expect(page.locator(ALERT)).to_contain_text(alert_merge)
        page.wait_for_selector(ALERT, state="hidden", timeout=wait_until_visible)

    with allure.step("Uncheck merge all to one checkbox"):
        page.locator(CHECKBOX_MERGE_ALL_TO_ONE).uncheck()

    with allure.step("Check diarization checkbox"):
        page.locator(CHECKBOX_DIARIZATION).set_checked(checked=True)

    with allure.step("Try to save"):
        page.locator(BUTTON_DOBAVIT).click()

    with allure.step("Wait for alert and check alert message"):
        page.wait_for_selector(ALERT, timeout=wait_until_visible)
        expect(page.locator(ALERT)).to_contain_text(alert_diarization)
        page.wait_for_selector(ALERT, state="hidden", timeout=wait_until_visible)

    with allure.step("Uncheck diarization checkbox"):
        page.locator(CHECKBOX_DIARIZATION).uncheck()

    with allure.step("Change parameters"):
        page.locator(RECOGNITION_PRIORITY).locator('[type="number"]').fill("10")
        page.locator(CHECKBOX_ECONOMIZE).set_checked(checked=True)
        #page.locator(CHECKBOX_USE_WEBHOOK).set_checked(checked=True)

    with allure.step("Press (Save)"):
        page.locator(BUTTON_DOBAVIT).click()

    with allure.step("Wait for alert and check alert message"):
        page.wait_for_selector(ALERT, timeout=wait_until_visible)
        expect(page.locator(ALERT)).to_contain_text(action_started)
        page.wait_for_selector(ALERT, state="hidden", timeout=wait_until_visible)
        page.wait_for_selector(INPUT_PHONE, timeout=wait_until_visible)

    with allure.step("Check"):
        expect(page.locator(INPUT_LOGIN)).to_have_value(NEW_LOGIN, timeout=wait_until_visible)
        expect(page.locator(INPUT_NAME)).to_have_value(NEW_NAME, timeout=wait_until_visible)
        expect(page.locator(INPUT_EMAIL)).to_have_value(EMAIL, timeout=wait_until_visible)
        expect(page.locator(INPUT_COMMENT)).to_have_text("someComment", timeout=wait_until_visible)
        expect(page.locator(INPUT_PHONE)).to_have_value(PHONE)
        expect(page.locator(INPUT_NEW_PASSWORD)).to_be_visible(timeout=wait_until_visible)
        expect(page.locator(INPUT_NEW_PASSWORD_REPEAT)).to_be_visible(timeout=wait_until_visible)

    with allure.step("Delete added user"):
        delete_added_user(page)

    with allure.step("Check that user deleted"):
        expect(page.locator(INPUT_LOGIN)).to_have_value(LOGIN, timeout=wait_until_visible)

    with allure.step("Delete admin"):
        delete_user(API_URL, TOKEN, USER_ID)
