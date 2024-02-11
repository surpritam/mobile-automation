from appium.webdriver.common.appiumby import AppiumBy

import pages


class FavoriteTeamsPage(pages.BasePage):
    __follow_favorite_default_first = (AppiumBy.XPATH, "(//android.widget.ImageView[@resource-id=\"com.fivemobile.thescore:id/follow_icon\"])[1]")
    __continue_btn = (AppiumBy.ID, "com.fivemobile.thescore:id/btn_primary")

    def choose_default_continue(self):
        self.actions.click(self.__follow_favorite_default_first)
        self.actions.click(self.__continue_btn)