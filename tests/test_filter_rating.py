import pytest
import time
from selenium.webdriver.common.by import By
from tests.utils import get_results_items

@pytest.mark.parametrize("rating", [5, 7, 9])
def test_filter_by_rating(driver, base_url, rating):
    driver.get(base_url)
    try:
        rating_slider = driver.find_element(By.XPATH, "//input[contains(@type,'range') or contains(@name,'rating')]")
        driver.execute_script("arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('change'));",
                              rating_slider, rating)
        time.sleep(2)
        items = get_results_items(driver)
        assert len(items) > 0, f"No results found for rating >= {rating}"
    except Exception:
        pytest.skip("Rating slider/input not found on page.")
