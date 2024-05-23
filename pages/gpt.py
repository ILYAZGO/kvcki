#  all for gpt
BUTTON_RAZMETKA = '[value="tags"]'
USERS_LIST = "#react-select-2-input"

BUTTON_GPT = '[data-testid="markup_nav_gpt"]'
BUTTON_GPT_CREATE_RULE = '[data-testid="markup_addGroup"]'
BUTTON_GPT_SAVE = '[data-testid="acceptButton"]'
BUTTON_KORZINA = '[aria-label="Удалить"]'
BUTTON_PENCIL = '[aria-label="Изменить название"]'
BUTTON_SAVE_EDITED_NAME = ".styles_root__4Hw2A"

INPUT_GPT_RULE_NAME = '[placeholder="Название правила"]'
INPUT_GPT_TEG_NAME = '[placeholder="Название тега"]'
INPUT_GPT_QUESTION = '[placeholder="Сформулируйте свой вопрос..."]'

def go_to_gpt(page="page: Page"):
    page.wait_for_selector(BUTTON_RAZMETKA)
    page.locator(BUTTON_RAZMETKA).click()
    page.wait_for_selector(BUTTON_GPT)
    page.locator(BUTTON_GPT).click()
    page.wait_for_selector('[filter="url(#filter0_b_4973_59500)"]')
    page.wait_for_timeout(500)

def press_save_in_gpt(page="page: Page"):
    page.locator(BUTTON_GPT_SAVE).click(force=True)
    page.wait_for_timeout(1700)
    # page.wait_for_selector(BUTTON_KORZINA)

def create_gpt_rule_with_one(GptRuleName, page="page: Page"):
    page.locator(BUTTON_GPT_CREATE_RULE).click()
    page.wait_for_timeout(500)
    page.wait_for_selector(INPUT_GPT_RULE_NAME)
    page.locator(INPUT_GPT_RULE_NAME).fill(GptRuleName)
    page.wait_for_timeout(800)
    page.locator(INPUT_GPT_TEG_NAME).fill("GPTteg1")
    page.wait_for_timeout(300)
    page.locator(INPUT_GPT_QUESTION).fill("GPTquestion1")
    page.wait_for_timeout(300)
    #page.locator(BUTTON_GPT_SAVE).click(force=True)
    #page.wait_for_timeout(1000)
    #page.wait_for_selector(BUTTON_KORZINA)


# create group with 2 tags with 2 questions inside
def create_gpt_rule_with_two(GptRuleName, page="page: Page"):
    page.locator(BUTTON_GPT_CREATE_RULE).click()
    page.wait_for_timeout(300)
    page.wait_for_selector(INPUT_GPT_RULE_NAME)
    page.locator(INPUT_GPT_RULE_NAME).fill(GptRuleName)
    page.wait_for_timeout(800)
    page.locator(INPUT_GPT_TEG_NAME).fill("GPTteg1")
    page.wait_for_timeout(300)
    page.locator(INPUT_GPT_QUESTION).fill("GPTquestion1")
    page.wait_for_timeout(300)
    page.get_by_role("button", name="Добавить вопрос").click()
    page.wait_for_timeout(700)
    page.locator(INPUT_GPT_TEG_NAME).nth(1).fill("GPTteg2")
    page.wait_for_timeout(300)
    page.locator(INPUT_GPT_QUESTION).nth(1).fill("GPTquestion2")
    page.wait_for_timeout(300)
    #page.locator(BUTTON_GPT_SAVE).click(force=True)
    #page.wait_for_timeout(1000)
    #page.wait_for_selector(BUTTON_KORZINA)

def turn_on_rule(page="page: Page"):
    page.locator('[aria-label="Вкл/Выкл"]').locator('[type="checkbox"]').click()
    page.wait_for_timeout(1200)

def delete_rule(page="page: Page"):
    page.wait_for_selector(BUTTON_KORZINA)
    #page.locator('[class*="styles_groupItem__B425x"]').nth(0).locator('[type="checkbox"]').first.click()
    #page.wait_for_timeout(800)
    #page.mouse.move(100, 0)
    #page.wait_for_timeout(600)
    page.locator(BUTTON_KORZINA).first.click()
    page.wait_for_timeout(600)
    #  confirm deleting
    page.get_by_role("button", name="Удалить").click()
    page.wait_for_timeout(2000)