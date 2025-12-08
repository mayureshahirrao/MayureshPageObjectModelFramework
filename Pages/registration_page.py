
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Pages.base_page import BasePage
from Utilities import ConfigReader

class Registration(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def fill_form(self, name, phone_num, email, country, city, username, password):
        self.enter_value('name_NAME', name, self.config_file_path)
        self.enter_value('phone_CSS', phone_num, self.config_file_path)
        self.enter_value('email_XPATH', email, self.config_file_path)

        self.select_dropdown('country_XPATH', country, self.config_file_path)

        self.enter_value('city_XPATH', city, self.config_file_path)
        self.enter_value('username_XPATH', username, self.config_file_path)
        self.enter_value('password_XPATH', password, self.config_file_path)
        self.click('submit_XPATH', self.config_file_path)


