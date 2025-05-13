#from playwright.sync_api import Page, expect
from pages.base_class import *

# inputs
INPUT_CHECK_LIST_NAME = '[name="title"]'
INPUT_FIRST_QUESTION = "[name='questions.0.title']"
INPUT_SECOND_QUESTION = "[name='questions.1.title']"
INPUT_FIRST_ANSWER = '[name="questions.0.answers.0.answer"]'
INPUT_SECOND_ANSWER = '[name="questions.0.answers.1.answer"]'
INPUT_THIRD_ANSWER = '[name="questions.1.answers.0.answer"]'
INPUT_FIRST_POINTS = '[name="questions.0.answers.0.point"]'
INPUT_SECOND_POINTS = '[name="questions.0.answers.1.point"]'
INPUT_THIRD_POINTS = '[name="questions.1.answers.0.point"]'
INPUT_LEFT_CHECK_LIST_NAME = '[class*="styles_input_"]'
INPUT_SORT_ORDER = '[name="priority"]'

# buttons
BUTTON_CHANGE_FILTERS = '[class*="styles_btnTitle_"]'
BUTTON_ADD_CHECK_LIST = '[data-testid="markup_addChecklists"]'
BUTTON_PENCIL = '[aria-label="Изменить название"]'
BUTTON_SAVE_EDITED_NAME = '[class*="checkButton"]'
BUTTON_IMPORT_CHECK_LIST = '[data-testid="markup_importDicts"]'

# other
NI4EGO_NE_NAYDENO = '[class*="styles_noFound"]'
CHECK_BOX_AUTOGENEREATE_REPORT = '[id="checklistGenerateReport"]'

class Checklists(BaseClass):
    def __init__(self, page: Page):
        super().__init__(page)
        self.button_add_check_list = page.locator(BUTTON_ADD_CHECK_LIST)
        self.input_check_list_name = page.locator(INPUT_CHECK_LIST_NAME)
        self.button_change_filters = page.locator(BUTTON_CHANGE_FILTERS)

    # def click_check_lists(self):
    #     """Go to check lists"""
    #     # self.page.wait_for_selector(BUTTON_MARKUP)
    #     # self.button_markup.click()
    #     # self.page.wait_for_selector(BUTTON_CHECK_LIST)
    #     # self.page.wait_for_timeout(500)
    #     self.button_check_list.click()
    #     self.page.wait_for_timeout(500)

    def create_check_list_with_questions_and_answers(self, check_list_name, first_question_title, second_question_title):
        """Creates 1st question with 2 answers and points and 2nd question with answer and points then delete 2nd question"""
        # creating check-list
        self.page.wait_for_selector(BUTTON_ADD_CHECK_LIST)
        self.button_add_check_list.click()
        self.page.wait_for_selector(INPUT_CHECK_LIST_NAME, timeout=self.timeout)
        self.input_check_list_name.type(check_list_name, delay=20)
        self.page.wait_for_timeout(500)
        # add 1st question
        self.page.get_by_role("button", name="Добавить вопрос").click()
        # page.locator('[class="styles_content__4ydtX"]').nth(1).get_by_role("button").click()
        self.page.locator(INPUT_FIRST_QUESTION).type(first_question_title, delay=20)
        self.page.locator(INPUT_FIRST_ANSWER).type("Answer1", delay=20)
        self.page.locator(INPUT_FIRST_POINTS).type("1", delay=20)
        self.page.get_by_role("button", name="Добавить ответ").click()
        self.page.locator(INPUT_SECOND_ANSWER).type("Answer2", delay=20)
        self.page.locator(INPUT_SECOND_POINTS).type("2", delay=20)
        # add 2nd question
        self.page.get_by_role("button", name="Добавить вопрос").click()
        self.page.locator(INPUT_SECOND_QUESTION).type(second_question_title, delay=20)
        self.page.locator(INPUT_THIRD_ANSWER).type("Answer3", delay=20)
        self.page.locator(INPUT_THIRD_POINTS).type("3", delay=20)
        # delete 2nd question
        self.page.get_by_role("button", name="Удалить вопрос").nth(1).click()
        self.page.wait_for_timeout(500)

    def add_filter_by_tags(self, filter_name):
        self.button_change_filters.click()
        self.menu.get_by_text("По тегам", exact=True).nth(1).click()
        self.page.wait_for_timeout(500)
        self.page.locator('[for="title"]').click() # click for close menu
        self.page.wait_for_selector(MENU, state="hidden")
        self.page.locator('[data-testid="filters_search_by_tags"]').locator('[type="text"]').type(filter_name, delay=20)
        self.page.wait_for_selector(MENU)
        self.page.wait_for_timeout(1500)
        self.page.get_by_text(filter_name, exact=True).nth(0).click()

    def press_button_save(self):
        self.page.get_by_role("button", name="Сохранить").click()
        self.page.wait_for_timeout(500)

    def create_appriser(self, title, points):
        self.page.wait_for_timeout(500)
        self.page.get_by_role("button", name="Добавить оценку").click()
        self.page.locator('[name="appraisers.0.title"]').type(title, delay=20)
        self.page.locator('[name="appraisers.0.points"]').type(points, delay=20)

    def delete_appriser(self):
        self.page.wait_for_timeout(500)
        self.page.locator('[class*="CheckListAppraisers_deleteBtn"]').click()
        self.page.wait_for_timeout(500)

    def press_import_checklists(self):
        self.page.locator(BUTTON_IMPORT_CHECK_LIST).click()
        self.page.wait_for_selector(MODAL_WINDOW)

    def delete_check_list(self):
        self.page.wait_for_selector(BUTTON_KORZINA)
        self.button_korzina.first.click()
        self.page.wait_for_selector(MODAL_WINDOW)
        self.modal_window.get_by_role("button", name="Удалить").click()





