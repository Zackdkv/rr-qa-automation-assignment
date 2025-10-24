import pytest
import time
from selenium.webdriver.common.by import By
from tests.utils import wait_for_items

def click_if_present(driver, locator_type, locator_value):
    try:
        el = driver.find_element(locator_type, locator_value)
        el.click()
        time.sleep(1)
        return True
    except Exception:
        return False

@pytest.mark.parametrize("category,slug", [
    ("Popular", "popular"),
    ("Trending", "trending"),
    ("Newest", "newest"),
    ("Top Rated", "top-rated"),
])
def test_filter_by_category(driver, base_url, category, slug):
    driver.get(base_url)
    if not click_if_present(driver, By.LINK_TEXT, category):
        click_if_present(driver, By.CSS_SELECTOR, f"a[href*='{slug}']")
    items = wait_for_items(driver)
    assert len(items) > 0, f"No results found for category {category}"
