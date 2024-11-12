from utils.variables import wait_until_visible
from playwright.sync_api import Page, expect
from pages.base_class import *


class Checklists(BaseClass):
    def __init__(self, page: Page):
        BaseClass.__init__(self, page)


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
BUTTON_CHECK_LIST = '[data-testid="markup_nav_checklists"]'
BUTTON_DOBAVIT_CHECK_LIST = '[data-testid="markup_addChecklists"]'
BUTTON_SAVE = ".MuiButton-contained"
BUTTON_KORZINA = '[aria-label="Удалить"]'
BUTTON_PENCIL = '[aria-label="Изменить название"]'
BUTTON_SAVE_EDITED_NAME = '[class*="checkButton"]'

# other
SEARCH_IN_IMPORT_MODAL = '[data-testid="markup_checklists_importSearch}"]'
NI4EGO_NE_NAYDENO = '[class*="styles_noFound"]'
CHECK_BOX_AUTOGENEREATE_REPORT = '[id="checklistGenerateReport"]'

def go_to_check_list(page="page: Page"):
    page.wait_for_selector(BUTTON_MARKUP)
    page.locator(BUTTON_MARKUP).click()
    page.wait_for_selector(BUTTON_CHECK_LIST)
    page.wait_for_timeout(500)
    page.locator(BUTTON_CHECK_LIST).click()


#  creates first question with 2 answers and points and second question with answer and points then delete second question
def create_check_list_with_questions_and_answers(checkListName, firstQustionTitle, secondQuestionTitle, page="page: Page"):
    # create check-list
    page.wait_for_selector(BUTTON_DOBAVIT_CHECK_LIST)
    page.locator(BUTTON_DOBAVIT_CHECK_LIST).click()
    page.wait_for_selector(INPUT_CHECK_LIST_NAME, timeout=wait_until_visible)
    page.locator(INPUT_CHECK_LIST_NAME).fill(checkListName)
    page.wait_for_timeout(500)
    # add questions
    page.locator('[class="styles_content__4ydtX"]').nth(1).get_by_role("button").click()

    page.locator(INPUT_FIRST_QUESTION).fill(firstQustionTitle)
    page.locator(INPUT_FIRST_ANSWER).fill("Answer1")
    page.locator(INPUT_FIRST_POINTS).fill("1")
    #page.locator(BUTTON_ADD_ANSWER).click()
    page.get_by_role("button", name="Добавить ответ").click()
    page.locator(INPUT_SECOND_ANSWER).fill("Answer2")
    page.locator(INPUT_SECOND_POINTS).fill("2")
    #page.locator(BUTTON_ADD_QUESTION).click()
    page.get_by_role("button", name="Добавить вопрос").click()
    page.locator(INPUT_SECOND_QUESTION).fill(secondQuestionTitle)
    page.locator(INPUT_THIRD_ANSWER).fill("Answer3")
    page.locator(INPUT_THIRD_POINTS).fill("3")
    #page.locator(BUTTON_DELETE_QUESTION).nth(1).click()
    page.get_by_role("button", name="Удалить вопрос").nth(1).click()
    page.wait_for_timeout(500)


def add_filter(filterType, filterName, page="page: Page"):
    page.locator('[class*="styles_btnTitle_"]').click()
    page.locator('[class*="-menu"]').get_by_text(filterType, exact=True).nth(1).click()
    page.wait_for_timeout(500)
    page.locator('[for="title"]').click()
    page.wait_for_timeout(500)
    page.locator('[data-testid="filters_search_by_tags"]').locator('[autocorrect=off]').fill(filterName)
    page.wait_for_timeout(2300)
    page.get_by_text(filterName, exact=True).nth(0).click()


def press_button_save(page="page: Page"):
    page.locator(BUTTON_SAVE).click()
    page.wait_for_timeout(500)


def create_appriser(title, points, page="page: Page"):
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Добавить оценку").click()
    #page.locator('[class*="CheckListAppraisers_addBtn"]').click()
    page.locator('[name="appraisers.0.title"]').fill(title)
    page.locator('[name="appraisers.0.points"]').fill(points)


def delete_appriser(page="page: Page"):
    page.wait_for_timeout(500)
    page.locator('[class*="CheckListAppraisers_deleteBtn"]').click()
    page.wait_for_timeout(500)

def press_import_checklists(page="page: Page"):
    page.locator('[data-testid="markup_importDicts"]').click()
    page.wait_for_selector(MODAL_WINDOW)

def delete_check_list(page="page: Page"):
    page.wait_for_selector(BUTTON_KORZINA)
    page.locator(BUTTON_KORZINA).first.click()
    page.wait_for_selector(MODAL_WINDOW)
    page.locator(MODAL_WINDOW).get_by_role("button", name="Удалить").click()

def delete_rule(page="page: Page"):
    page.wait_for_selector(BUTTON_KORZINA)
    page.locator('[class*="styles_groupItem__B425x"]').nth(0).locator('[type="checkbox"]').first.click()
    page.wait_for_timeout(600)
    page.locator(BUTTON_CHECK_LIST).click()
    page.locator(BUTTON_KORZINA).first.click()
    page.wait_for_selector(MODAL_WINDOW)
    #  confirm deleting
    page.locator(MODAL_WINDOW).get_by_role("button", name="Удалить").click()
