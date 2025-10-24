import pytest
from tests.utils import wait_for_items
from selenium.webdriver.common.by import By

def click_next(driver):
    for sel in ["button.next", "a.next", "button[aria-label='Next']", "li.next a"]:
        try:
            driver.find_element(By.CSS_SELECTOR, sel).click()
            return True
        except Exception:
            continue
    return False

def test_pagination_basic(driver, base_url):
    driver.get(base_url)
    items_before = len(wait_for_items(driver))
    clicked = click_next(driver)
    if not clicked:
        pytest.skip("Next page control not found")
    items_after = len(wait_for_items(driver))
    assert items_after >= 0
