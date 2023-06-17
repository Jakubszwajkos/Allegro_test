from telnetlib import EC

#import item as item
import pytest
from selenium import webdriver
import time
driver = None

from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="firefox")


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "firefox":
        service_obj = Service("/Users/Szwajkos/Desktop/firefox_driver/geckodriver")
        driver = webdriver.Firefox(service=service_obj)

    elif browser_name == "chrome":
        service_obj = Service("/Users/Szwajkos/Desktop/chromedriver_mac64/chromedriver")
        driver = webdriver.Chrome(service=service_obj)

    elif browser_name == "IE":
        print("IE driver")

    driver.get("https://allegro.pl/")
    driver.maximize_window()


    request.cls.driver = driver
    driver.find_element(By.XPATH, "//button[text()='Ok, zgadzam się']").click()
    yield
    driver.close()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    global driver
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

