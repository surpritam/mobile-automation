from appium.webdriver.common.appiumby import AppiumBy

import pages


class FavoriteLeaguePage(pages.BasePage):
    __continue_btn = (AppiumBy.ID, "com.fivemobile.thescore:id/btn_primary")

    def continue_without_selecting(self):
        self.actions.click(self.__continue_btn)