
from Pages.base_page import BasePage
from Pages.new_cars_page import NewCarsPage

global config_file_path
class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def find_new_car(self):
        self.move_to("newCar_XPATH", self.config_file_path)
        self.click("findNewCars_XPATH", self.config_file_path)
        return NewCarsPage(self.driver)

    def compare_cars(self):
        pass

    def check_used_cars(self):
        pass