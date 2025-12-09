import time
from configparser import ConfigParser
import logging

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Utilities import ConfigReader
from Utilities import log_util
from Utilities.log_util import Logger
import os

log = Logger(__name__, logging.INFO)

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10)
        cwd = os.getcwd()
        print(f"current_dir in config reader: {cwd}")
        if cwd.endswith("PageObjectModelFramework"):
            self.config_file_path = "Configurations\\config.ini"
        else:
            self.config_file_path = "..\\Configurations\\config.ini"


    def click(self, locator, config_file_path):
        if str(locator).endswith('_XPATH'):
            self.driver.find_element(
                By.XPATH,
                ConfigReader.read_config( 'locators', locator, config_file_path)
            ).click()
        elif str(locator).endswith('_CSS'):
            self.driver.find_element(
                By.CSS_SELECTOR,
                ConfigReader.read_config( 'locators', locator, config_file_path)
            ).click()
        elif str(locator).endswith('_LINK'):
            self.driver.find_element(
                By.LINK_TEXT,
                ConfigReader.read_config( 'locators', locator, config_file_path)
            ).click()
        elif str(locator).endswith('_ID'):
            self.driver.find_element(
                By.ID,
                ConfigReader.read_config( 'locators', locator, config_file_path)
            ).click()
        elif str(locator).endswith('_NAME'):
            self.driver.find_element(
                By.NAME,
                ConfigReader.read_config( 'locators', locator, config_file_path)
            ).click()
        elif str(locator).endswith('_TAGNAME'):
            self.driver.find_element(
                By.TAG_NAME,
                ConfigReader.read_config( 'locators', locator, config_file_path)
            ).click()
        elif str(locator).endswith('_CLASSNAME'):
            self.driver.find_element(
                By.CLASS_NAME,
                ConfigReader.read_config( 'locators', locator, config_file_path)
            ).click()
        log.logger.info(f"Clicked on element with locator: {locator}")

    def enter_value(self, locator, text, config_file_path):
        if str(locator).endswith('_XPATH'):
            self.driver.find_element(
                By.XPATH,
                ConfigReader.read_config( 'locators', locator, config_file_path)
            ).send_keys(text)
        elif str(locator).endswith('_CSS'):
            self.driver.find_element(
                By.CSS_SELECTOR,
                ConfigReader.read_config( 'locators', locator, config_file_path)
            ).send_keys(text)
        elif str(locator).endswith('_LINK'):
            self.driver.find_element(
                By.PARTIAL_LINK_TEXT,
                ConfigReader.read_config( 'locators', locator, config_file_path)
            ).send_keys(text)
        elif str(locator).endswith('_ID'):
            self.driver.find_element(
                By.ID,
                ConfigReader.read_config( 'locators', locator, config_file_path)
            ).send_keys(text)
        elif str(locator).endswith('_NAME'):
            self.driver.find_element(
                By.NAME,
                ConfigReader.read_config( 'locators', locator, config_file_path)
            ).send_keys(text)
        elif str(locator).endswith('_TAGNAME'):
            self.driver.find_element(
                By.TAG_NAME,
                ConfigReader.read_config( 'locators', locator, config_file_path)
            ).send_keys(text)
        elif str(locator).endswith('_CLASSNAME'):
            self.driver.find_element(
                By.CLASS_NAME,
                ConfigReader.read_config( 'locators', locator, config_file_path)
            ).send_keys(text)
        log.logger.info(f"Entered value '{text}' in element with locator: {locator}")

    def select_dropdown(self, locator, value, config_file_path):
        global dropdown
        if str(locator).endswith('_XPATH'):
            dropdown = self.driver.find_element(
                By.XPATH,
                ConfigReader.read_config( 'locators', locator, config_file_path)
            )
        elif str(locator).endswith('_CSS'):
            dropdown = self.driver.find_element(
                By.CSS_SELECTOR,
                ConfigReader.read_config( 'locators', locator, config_file_path)
            )
        elif str(locator).endswith('_LINK'):
            dropdown = self.driver.find_element(
                By.PARTIAL_LINK_TEXT,
                ConfigReader.read_config( 'locators', locator, config_file_path)
            )
        elif str(locator).endswith('_ID'):
            dropdown = self.driver.find_element(
                By.ID,
                ConfigReader.read_config( 'locators', locator, config_file_path)
            )
        elif str(locator).endswith('_NAME'):
            dropdown = self.driver.find_element(
                By.NAME,
                ConfigReader.read_config( 'locators', locator, config_file_path)
            )
        elif str(locator).endswith('_TAGNAME'):
            dropdown = self.driver.find_element(
                By.TAG_NAME,
                ConfigReader.read_config( 'locators', locator, config_file_path)
            )
        elif str(locator).endswith('_CLASSNAME'):
            dropdown = self.driver.find_element(
                By.CLASS_NAME,
                ConfigReader.read_config( 'locators', locator, config_file_path)
            )

        select = Select(dropdown)
        select.select_by_visible_text(value)

        log.logger.info(f"Selected value '{value}' from dropdown with locator: {str(locator)}")

    def move_to(self, locator, config_file_path):
        global element
        if str(locator).endswith('_XPATH'):
            element = self.driver.find_element(
                By.XPATH,
                ConfigReader.read_config( 'locators', locator, config_file_path)
            )
        elif str(locator).endswith('_CSS'):
            element = self.driver.find_element(
                By.CSS_SELECTOR,
                ConfigReader.read_config( 'locators', locator, config_file_path)
            )
        elif str(locator).endswith('_LINK'):
            element = self.driver.find_element(
                By.PARTIAL_LINK_TEXT,
                ConfigReader.read_config( 'locators', locator, config_file_path)
            )
        elif str(locator).endswith('_ID'):
            element = self.driver.find_element(
                By.ID,
                ConfigReader.read_config( 'locators', locator, config_file_path)
            )
        elif str(locator).endswith('_NAME'):
            element = self.driver.find_element(
                By.NAME,
                ConfigReader.read_config( 'locators', locator, config_file_path)
            )
        elif str(locator).endswith('_TAGNAME'):
            element = self.driver.find_element(
                By.TAG_NAME,
                ConfigReader.read_config( 'locators', locator, config_file_path)
            )
        elif str(locator).endswith('_CLASSNAME'):
            element = self.driver.find_element(
                By.CLASS_NAME,
                ConfigReader.read_config( 'locators', locator, config_file_path)
            )

        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        log.logger.info(f"Moved to element with locator: {str(locator)}")


if __name__=="__main__":
    print(ConfigReader.read_config( 'locators', 'phone_CSS', "..\\Configurations\\config.ini"))

