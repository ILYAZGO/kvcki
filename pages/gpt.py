#  all for gpt
BUTTON_RAZMETKA = '[value="tags"]'

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
    page.locator(BUTTON_GPT).click()
    page.wait_for_timeout(500)

def create_gpt_rule_with_one(GptRuleName, page="page: Page"):
    page.locator(BUTTON_GPT_CREATE_RULE).click()
    page.wait_for_selector(INPUT_GPT_RULE_NAME)
    page.wait_for_timeout(500)
    page.locator(INPUT_GPT_RULE_NAME).fill(GptRuleName)
    page.wait_for_timeout(500)
    page.locator(INPUT_GPT_TEG_NAME).fill("GPTteg1")
    page.locator(INPUT_GPT_QUESTION).fill("GPTquestion1")
    page.locator(BUTTON_GPT_SAVE).click(force=True)
    page.wait_for_timeout(1000)


# create group with 2 tags with 2 questions inside
def create_gpt_rule_with_two(GptRuleName, page="page: Page"):
    page.locator(BUTTON_GPT_CREATE_RULE).click()
    page.wait_for_selector(INPUT_GPT_RULE_NAME)
    page.wait_for_timeout(500)
    page.wait_for_selector(INPUT_GPT_RULE_NAME)
    page.locator(INPUT_GPT_RULE_NAME).fill(GptRuleName)
    page.wait_for_timeout(500)
    page.locator(INPUT_GPT_TEG_NAME).fill("GPTteg1")
    page.locator(INPUT_GPT_QUESTION).fill("GPTquestion1")
    page.get_by_role("button", name="Добавить вопрос").click()
    page.wait_for_timeout(700)
    page.locator(INPUT_GPT_TEG_NAME).nth(1).fill("GPTteg2")
    page.locator(INPUT_GPT_QUESTION).nth(1).fill("GPTquestion2")
    page.locator(BUTTON_GPT_SAVE).click(force=True)
    page.wait_for_timeout(1000)

def turn_on_rule(page="page: Page"):
    page.locator('[aria-label="Вкл/Выкл"]').locator('[type="checkbox"]').click()
    page.wait_for_timeout(1200)