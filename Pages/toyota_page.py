from Pages.base_page import BasePage
from Pages.car_base import CarBase


class ToyotaPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.car = CarBase(self.driver)

    def get_page_title(self):
        return self.car.get_page_title()

    def get_available_models(self):
        return self.car.get_model_details()

