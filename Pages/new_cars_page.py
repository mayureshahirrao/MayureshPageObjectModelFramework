from Pages.base_page import BasePage
from Pages.bmw_page import BMWPage
from Pages.tata_page import TataPage
from Pages.hyundai_page import HyundaiPage
from Pages.maruti_page import MarutiPage
from Pages.toyota_page import ToyotaPage

global config_file_path
class NewCarsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def select_hyundai(self):
        self.click("hyundai_XPATH", self.config_file_path)
        return HyundaiPage(self.driver)

    def select_toyota(self):
        self.click("toyota_XPATH", self.config_file_path)
        return ToyotaPage(self.driver)

    def select_maruti(self):
        self.click("maruti_XPATH", self.config_file_path)
        return MarutiPage(self.driver)

    def select_tata(self):
        self.click("tata_XPATH", self.config_file_path)
        return TataPage(self.driver)

    def select_bmw(self):
        self.click("bmw_XPATH", self.config_file_path)
        return BMWPage(self.driver)