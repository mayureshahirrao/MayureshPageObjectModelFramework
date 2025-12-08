import os

import allure
import pytest
import logging

from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService

from Utilities import ConfigReader
from Utilities.log_util import Logger


log = Logger(__name__, logging.INFO)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can be "setup", "call", "teardown"
    setattr(item, 'rep_' + rep.when, rep)
    return rep


@pytest.fixture()
def on_log_failure(request,browser_setup):
    yield
    item = request.node
    driver = browser_setup
    # This code runs after the test
    if item.rep_call.failed:
        log.logger.info("Test failed! Taking screenshot...")
        allure.attach(driver.get_screenshot_as_png(),
                      name="PAge_Screenshot",
                      attachment_type=AttachmentType.PNG)

# @pytest.fixture(params=['chrome', 'firefox', 'edge'], scope='function', autouse=True)
@pytest.fixture(params=['chrome'], scope='function', autouse=True)
def browser_setup(request):
    global driver
    if request.param == 'chrome':
        chrome_service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=chrome_service)
        log.logger.info("Chrome browser launched")
    elif request.param == 'firefox':
        firefox_service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=firefox_service)
        log.logger.info("Firefox browser launched")
    elif request.param == 'edge':
        # edge_service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge()
        log.logger.info("Edge browser launched")

    request.cls.driver = driver
    driver.maximize_window()
    driver.implicitly_wait(10)

    cwd = os.getcwd()
    print(f"current_dir in conftest: {cwd}")
    if cwd == "D:\\Programming\\PythonProgramming\\PageObjectModelFramework":
        config_file_path = "Configurations\\config.ini"
    else:
        config_file_path = "..\\Configurations\\config.ini"

    driver.get(ConfigReader.read_config('basic info','testsiteurl',config_file_path))
    # driver.get("https://www.qa.way2automation.com/")

    yield driver
    driver.quit()

if __name__ == "__main__":
    print(ConfigReader.read_config())