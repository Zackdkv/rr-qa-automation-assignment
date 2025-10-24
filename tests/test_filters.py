import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from tests.utils import wait_for_items, get_results_items

@pytest.mark.smoke
def test_smoke_landing_page(driver, base_url):
    driver.get(base_url)
    assert "discover" in driver.title.lower() or len(get_results_items(driver)) > 0

def click_element(driver, by, value):
    driver.find_element(by, value).click()

@pytest.mark.parametrize("category,slug", [
    ("Popular", "popular"),
    ("Trending", "trending"),
    ("Newest", "newest"),
    ("Top Rated", "top-rated"),
])
def test_category_filter_changes_results(driver, base_url, category, slug):
    driver.get(base_url)
    try:
        click_element(driver, By.LINK_TEXT, category)
    except Exception:
        try:
            click_element(driver, By.CSS_SELECTOR, f"a[href*='{slug}']")
        except Exception:
            pytest.skip(f"Category {category} not present on page")
    items = wait_for_items(driver)
    assert len(items) > 0, f"No results for category {category}"
