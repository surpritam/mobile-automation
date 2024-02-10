from utils.element_actions import ElementActions

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ElementActions(driver)
