from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.calls import *
import pytest

'''Searching all communications for Ecotelecom'''


@pytest.mark.calls
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)

    auth(ECOTELECOM, ECOPASS, page)

    page.wait_for_selector(INPUT_ID)

    page.locator(INPUT_NOMER_CLIENTA).fill("79251579005")
    page.locator(POISK_PO_FRAGMENTAM).click()
    page.locator(INPUT_NOMER_SOTRUDNIKA).fill("4995055555")
    page.locator(POISK_PO_FRAGMENTAM).click()

    page.locator(INPUT_SLOVAR_ILI_TEXT_CLIENT).fill("адрес")
    page.wait_for_timeout(2600)
    page.locator(POISK_PO_FRAGMENTAM).click()

    page.locator(INPUT_SLOVAR_ILI_TEXT_SOTRUDNIK).fill("2223")
    page.wait_for_timeout(2600)
    page.locator(POISK_PO_FRAGMENTAM).click()

    fill_search_length(">10", page)
    page.locator(POISK_PO_FRAGMENTAM).click()
    page.locator(INPUT_VREMYA_ZVONKA).fill("11:42")
    page.locator(POISK_PO_FRAGMENTAM).click()
    page.locator(INPUT_ID).fill("1644474236.14425")
    page.locator(POISK_PO_FRAGMENTAM).click()

    page.wait_for_selector(INPUT_PO_TEGAM)
    page.locator(INPUT_PO_TEGAM).fill("Другой отдел")
    page.wait_for_timeout(2600)
    page.get_by_text("Другой отдел", exact=True).first.click()
    page.locator(POISK_PO_FRAGMENTAM).click()

    expect(page.locator('[aria-label="Remove 79251579005"]')).to_be_visible()
    expect(page.locator('[aria-label="Remove 4995055555"]')).to_be_visible()
    expect(page.locator('[aria-label="Remove адрес"]')).to_be_visible()
    expect(page.locator('[aria-label="Remove 2223"]')).to_be_visible()
    expect(page.locator('[aria-label="Remove >10"]')).to_be_visible()
    expect(page.locator('[aria-label="Remove 11:42"]')).to_be_visible()
    expect(page.locator('[aria-label="Remove 1644474236.14425"]')).to_be_visible()
    expect(page.locator('[aria-label="Remove Другой отдел"]')).to_be_visible()

    page.get_by_role("button", name="Очистить").click()

    expect(page.locator('[aria-label="Remove 79251579005"]')).not_to_be_visible()
    expect(page.locator('[aria-label="Remove 4995055555"]')).not_to_be_visible()
    expect(page.locator('[aria-label="Remove адрес"]')).not_to_be_visible()
    expect(page.locator('[aria-label="Remove 2223"]')).not_to_be_visible()
    expect(page.locator('[aria-label="Remove >10"]')).not_to_be_visible()
    expect(page.locator('[aria-label="Remove 11:42"]')).not_to_be_visible()
    expect(page.locator('[aria-label="Remove 1644474236.14425"]')).not_to_be_visible()
    expect(page.locator('[aria-label="Remove Другой отдел"]')).not_to_be_visible()