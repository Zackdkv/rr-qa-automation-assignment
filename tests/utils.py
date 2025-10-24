from selenium.webdriver.common.by import By
import time

def get_results_items(driver):
    items = driver.find_elements(By.CSS_SELECTOR, "div.card, .card, .movie-card, .result-card")
    if not items:
        items = driver.find_elements(By.CSS_SELECTOR, "li, .list-item")
    return items

def wait_for_items(driver, timeout=6):
    end = time.time() + timeout
    while time.time() < end:
        items = get_results_items(driver)
        if items:
            return items
    return []
