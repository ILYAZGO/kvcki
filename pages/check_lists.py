#  all for check-lists

USERS_LIST = "#react-select-2-input"

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

# buttons
BUTTON_RAZMETKA = '[value="tags"]'
BUTTON_CHECK_LIST = '[data-testid="markup_nav_checklists"]'
BUTTON_DOBAVIT_CHECK_LIST = '[data-testid="markup_addChecklists"]'
BUTTON_SAVE = ".MuiButton-contained"
BUTTON_KORZINA = '[aria-label="Удалить"]'
BUTTON_PENCIL = '[aria-label="Изменить название"]'
BUTTON_SAVE_EDITED_NAME = '[class*="checkButton"]'

# other
NI4EGO_NE_NAYDENO = '[class*="styles_noFound"]'

def go_to_check_list(page="page: Page"):
    page.wait_for_selector(BUTTON_RAZMETKA)
    page.locator(BUTTON_RAZMETKA).click()
    page.locator(BUTTON_CHECK_LIST).click()


#  creates first question with 2 answers and points and second question with answer and points then delete second question
def create_check_list_with_questions_and_answers(checkListName, firstQustionTitle, secondQuestionTitle, page="page: Page"):
    # create check-list
    page.wait_for_selector(BUTTON_DOBAVIT_CHECK_LIST)
    page.locator(BUTTON_DOBAVIT_CHECK_LIST).click()
    page.wait_for_selector(INPUT_CHECK_LIST_NAME)
    page.locator(INPUT_CHECK_LIST_NAME).fill(checkListName)
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


def press_button_save(page="page: Page"):
    page.locator(BUTTON_SAVE).click()
    page.wait_for_timeout(500)


def create_appriser(title, points, page="page: Page"):
    page.wait_for_timeout(200)
    page.get_by_role("button", name="Добавить оценку").click()
    #page.locator('[class*="CheckListAppraisers_addBtn"]').click()
    page.locator('[name="appraisers.0.title"]').fill(title)
    page.locator('[name="appraisers.0.points"]').fill(points)

def delete_appriser(page="page: Page"):
    page.wait_for_timeout(200)
    page.locator('[class*="CheckListAppraisers_deleteBtn"]').click()
    page.wait_for_timeout(300)


def delete_check_list(page="page: Page"):
    page.wait_for_timeout(200)
    page.locator(BUTTON_KORZINA).click()
    page.get_by_role("button", name="Удалить").click()

def delete_rule(page="page: Page"):
    page.wait_for_selector(BUTTON_KORZINA)
    page.locator('[class*="styles_groupItem__B425x"]').nth(0).locator('[type="checkbox"]').first.click()
    page.wait_for_timeout(400)
    page.locator(BUTTON_CHECK_LIST).click()
    page.locator(BUTTON_KORZINA).first.click()
    page.wait_for_timeout(400)
    #  confirm deleting
    page.get_by_role("button", name="Удалить").click()
    page.wait_for_timeout(800)