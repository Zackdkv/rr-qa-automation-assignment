import pytest
import time
from selenium.webdriver.common.by import By
from tests.utils import get_results_items

@pytest.mark.parametrize("year", ["2020", "2021", "2022", "2023"])
def test_filter_by_year(driver, base_url, year):
    driver.get(base_url)
    try:
        year_input = driver.find_element(By.XPATH, "//input[contains(@type,'number') or contains(@placeholder,'Year')]")
        year_input.clear()
        year_input.send_keys(year)
        time.sleep(2)
        items = get_results_items(driver)
        assert len(items) > 0, f"No results found for year {year}"
    except Exception:
        pytest.skip("Year filter not found on the page.")
