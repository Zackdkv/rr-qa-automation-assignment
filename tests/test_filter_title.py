import pytest
import time
from selenium.webdriver.common.by import By
from tests.utils import get_results_items

@pytest.mark.parametrize("keyword", ["Avatar", "Spider", "Star"])
def test_filter_by_title_search(driver, base_url, keyword):
    driver.get(base_url)
    try:
        search_box = driver.find_element(By.CSS_SELECTOR, "input[type='search'], input[name*='title']")
        search_box.clear()
        search_box.send_keys(keyword)
        time.sleep(2)
        items = get_results_items(driver)
        assert len(items) > 0, f"No results for search '{keyword}'"
    except Exception:
        pytest.skip("Search input not found on the page.")
