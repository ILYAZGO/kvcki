from utils.variables import wait_until_visible

from pages.base_class import *
from playwright.sync_api import Page, expect


class GPT(BaseClass):
    def __init__(self, page: Page):
        BaseClass.__init__(self, page)

BUTTON_GPT = '[data-testid="markup_nav_gpt"]'
BUTTON_GPT_CREATE_RULE = '[data-testid="markup_addGroup"]'
BUTTON_GPT_SAVE = '[data-testid="acceptButton"]'
BUTTON_GPT_CANCEL = '[data-testid="cancelButton"]'
BUTTON_PENCIL = '[aria-label="Изменить название"]'
BUTTON_SAVE_EDITED_NAME = ".styles_root__4Hw2A"
BUTTON_IMPORT_GPT = '[data-testid="markup_importDicts"]'

INPUT_GPT_RULE_NAME = '[placeholder="Название правила"]'
INPUT_GPT_TEG_NAME = '[placeholder="Название тега"]'
INPUT_GPT_QUESTION = '[placeholder="Сформулируйте свой вопрос..."]'


def go_to_gpt(page="page: Page"):
    page.wait_for_selector(BUTTON_MARKUP, timeout=wait_until_visible)
    page.locator(BUTTON_MARKUP).click()
    page.wait_for_selector(BUTTON_GPT, timeout=wait_until_visible)
    page.locator(BUTTON_GPT).click()
    page.wait_for_selector('[filter="url(#filter0_b_4973_59500)"]', timeout=wait_until_visible)
    page.wait_for_timeout(500)

def press_save_in_gpt(page="page: Page"):
    page.locator(BUTTON_GPT_SAVE).click(force=True)
    page.wait_for_timeout(500)

def press_add_settings(page="page: Page"):
    page.get_by_role("button", name="Добавить настройки").click()
    page.wait_for_selector(MENU, timeout=wait_until_visible)

def create_gpt_rule_with_one(GptRuleName, page="page: Page"):
    page.locator(BUTTON_GPT_CREATE_RULE).click()
    page.wait_for_timeout(400)
    page.wait_for_selector(INPUT_GPT_RULE_NAME)
    page.locator(INPUT_GPT_RULE_NAME).fill(GptRuleName)
    page.wait_for_timeout(800)
    page.locator(INPUT_GPT_TEG_NAME).fill("GPTteg1")
    page.wait_for_timeout(300)
    page.locator(INPUT_GPT_QUESTION).fill("GPTquestion1")
    page.wait_for_timeout(300)


# create group with 2 tags with 2 questions inside#
def create_gpt_rule_with_two(GptRuleName, page="page: Page"):
    page.locator(BUTTON_GPT_CREATE_RULE).click()
    page.wait_for_timeout(400)
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


def add_filter(filterType, filterName, page="page: Page"):
    page.locator('[style="margin-top: 5px;"]').get_by_role("button").click()
    page.locator('[class*="-menu"]').get_by_text(filterType, exact=True).nth(1).click()
    page.wait_for_timeout(500)
    page.locator('[aria-label="Фильтр применимости правила"]').click()
    page.wait_for_timeout(500)
    page.locator('[data-testid="filters_search_by_tags"]').locator('[autocorrect=off]').fill(filterName)
    page.wait_for_timeout(2300)
    page.get_by_text(filterName, exact=True).nth(0).click()

def turn_on_rule(page="page: Page"):
    page.locator('[aria-label="Вкл/Выкл"]').locator('[type="checkbox"]').click()
    page.wait_for_selector('[class*="Mui-checked"]', timeout=wait_until_visible)

def delete_rule(page="page: Page"):
    page.wait_for_selector(BUTTON_KORZINA)
    page.locator(BUTTON_KORZINA).first.click()
    page.wait_for_selector(MODAL_WINDOW)
    page.locator(MODAL_WINDOW).get_by_role("button", name="Удалить").click()
    page.wait_for_selector(MODAL_WINDOW, state="hidden")
    page.wait_for_timeout(500)

# def all_checkboxes_to_be_checked(page="page: Page"):
#     # Находим все чекбоксы на странице
#     checkboxes = page.query_selector_all('input[type="checkbox"]')
#     # Проверяем состояние каждого чекбокса
#     all_checked = all(checkbox.is_checked() for checkbox in checkboxes)
#     return all_checked

def amount_checkboxes_to_be_checked(amount, page="page: Page"):
    # Находим все чекбоксы на странице
    checkboxes = page.query_selector_all('input[type="checkbox"]')
    # Check that amount checked
    all_checked = sum(checkbox.is_checked() for checkbox in checkboxes)
    return all_checked==amount