import pytest, logging, os, time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

@pytest.fixture(scope="session")
def base_url():
    return "https://tmdb-discover.surge.sh/"

@pytest.fixture(scope="session")
def chrome_options():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--window-size=1920,1080")
    caps = DesiredCapabilities.CHROME.copy()
    caps['goog:loggingPrefs'] = {'browser': 'ALL'}
    return opts, caps

@pytest.fixture(scope="function")
def driver(chrome_options):
    opts, caps = chrome_options
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=opts, desired_capabilities=caps)
    driver.implicitly_wait(6)
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

def _save_screenshot(driver, path):
    try:
        driver.save_screenshot(path)
    except Exception:
        pass

@pytest.fixture(autouse=True)
def attach_screenshot_on_failure(request, driver):
    yield
    for when in ("setup", "call", "teardown"):
        rep = getattr(request.node, "rep_" + when, None)
        if rep and rep.failed:
            os.makedirs("reports", exist_ok=True)
            fname = os.path.join("reports", f"{request.node.name}_{int(time.time())}.png")
            _save_screenshot(driver, fname)
