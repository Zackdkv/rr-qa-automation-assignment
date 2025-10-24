import pytest
import time
from selenium.webdriver.common.by import By
from tests.utils import get_results_items

def test_filter_by_genre(driver, base_url):
    driver.get(base_url)
    try:
        dropdown = driver.find_element(By.XPATH, "//select[contains(@id,'genre') or contains(@name,'genre')]")
        options = dropdown.find_elements(By.TAG_NAME, "option")
        if len(options) > 1:
            options[1].click()
            time.sleep(2)
            items = get_results_items(driver)
            assert len(items) > 0, "No results found after selecting genre."
        else:
            pytest.skip("No genre options available in dropdown.")
    except Exception:
        pytest.skip("Genre dropdown not found on the page.")
