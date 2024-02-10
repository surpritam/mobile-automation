from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class FavoriteLeaguePage(BasePage):
    __continue_btn = (AppiumBy.ID, "com.fivemobile.thescore:id/btn_primary")

    def continue_without_selecting(self):
        self.actions.click(self.__continue_btn)