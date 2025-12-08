import os
import logging

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from Pages.registration_page import Registration
from TestCases.BaseTest import BaseTest
from Utilities import data_provider
from Utilities.log_util import Logger


log = Logger(__name__, logging.INFO)

class Test_SignUp(BaseTest):
    @pytest.mark.parametrize("name, phone_num, email, country, city, username, password", data_provider.get_data("LoginTest"))
    def test_signup(self, name, phone_num, email, country, city, username, password):
        current_dir = os.getcwd()
        log.logger.info(f"Starting test_signup in directory: {current_dir}")
        log.logger.info(f"Executing test_signup with data:"
                        f" {name}, {phone_num}, {email}, {country}, {city}, {username}, {password}")
        reg_page = Registration(self.driver)
        reg_page.fill_form(name, phone_num, email, country, city, username, password)
        log.logger.info("Executed test_signup successfully.")
