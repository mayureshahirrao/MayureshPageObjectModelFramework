from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.wait import WebDriverWait
import os

from Utilities import ConfigReader


class CarBase:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10)
        cwd = os.getcwd()
        if cwd =="D:\\Programming\\PythonProgramming\\PageObjectModelFramework":
            self.config_file_path = "Configurations\\config.ini"
        else:
            self.config_file_path = "..\\Configurations\\config.ini"


    def get_page_title(self):
        # return self.driver.title
        # cwd = os.getcwd()
        # print(f"Current working directory in get_page_title: {cwd}")
        car_title_xpath = ConfigReader.read_config('locators', 'carTitle_XPATH', self.config_file_path)
        # print(car_title_xpath)
        return self.driver.find_element(
            By.XPATH,
            car_title_xpath).text

    def get_model_details(self):
        car_details = {}
        car_names = self.driver.find_elements(
            By.XPATH,
            ConfigReader.read_config( 'locators', 'carName_XPATH', self.config_file_path))
        # print(f"Car names found: {[car.text for car in car_names]}")
        for car_name in car_names:
            car_price = None
            try:
                car_price = self.driver.find_element(
                    locate_with(
                        By.XPATH,
                        ConfigReader.read_config( 'locators', 'carPrice_XPATH', self.config_file_path)
                    ).below(car_name)
                ).text
            except Exception as e:
                print(f"Could not find price for car {car_name.text}: {e}")
            car_details[car_name.text] = car_price
        return car_details
