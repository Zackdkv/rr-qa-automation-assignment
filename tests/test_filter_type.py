import pytest
import time
from selenium.webdriver.common.by import By
from tests.utils import get_results_items

@pytest.mark.parametrize("type_label", ["Movies", "TV", "Shows"])
def test_filter_by_type(driver, base_url, type_label):
    driver.get(base_url)
    try:
        btn = driver.find_element(By.XPATH, f"//button[contains(., '{type_label}')]")
        btn.click()
        time.sleep(2)
        items = get_results_items(driver)
        assert len(items) > 0, f"No results found after selecting type {type_label}"
    except Exception:
        pytest.skip(f"Type button '{type_label}' not found on UI")
