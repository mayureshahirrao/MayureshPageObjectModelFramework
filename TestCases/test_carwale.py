import os
import logging
import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from Pages.car_base import CarBase
from Pages.home_page import HomePage
from TestCases.BaseTest import BaseTest
from Utilities import data_provider
from Utilities.log_util import Logger


log = Logger(__name__, logging.INFO)

class Test_CarWale(BaseTest):

    @pytest.mark.parametrize("car_brand, car_model", data_provider.get_data("NewCarsTest"))
    def test_find_new_cars(self, car_brand, car_model):
        current_dir = os.getcwd()
        log.logger.info(f"Starting test_signup in directory: {current_dir}")
        log.logger.info("**********Inside New Cars Test**********")
        home = HomePage(self.driver)
        new_car = home.find_new_car()
        selected_car_brand = None
        if car_brand.lower() == "maruti":
            selected_car_brand = new_car.select_maruti()
        elif car_brand.lower() == "hyundai":
            selected_car_brand = new_car.select_hyundai()
        elif car_brand.lower() == "toyota":
            selected_car_brand = new_car.select_toyota()
        elif car_brand.lower() == "tata":
            selected_car_brand = new_car.select_tata()
        elif car_brand.lower() == "bmw":
            selected_car_brand = new_car.select_bmw()
        else:
            log.logger.error(f"Invalid car brand: {car_brand}")
            assert False, f"Invalid car brand: {car_brand}"
        log.logger.info(f"Car Title: {selected_car_brand.get_page_title()}")

        available_car_models = selected_car_brand.get_available_models()
        for model in available_car_models:
            log.logger.info(f"{model}: {available_car_models[model]}")


        time.sleep(5)
