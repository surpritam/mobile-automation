import logging

from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class LeaguesPage(BasePage):
    __leagues_tab = (AppiumBy.XPATH,"//*[@resource-id=\"com.fivemobile.thescore:id/navigation_bar_item_small_label_view\" and @text=\"Leagues\"]")
    __leagues_heading = (AppiumBy.XPATH,"//*[@resource-id=\"com.fivemobile.thescore:id/titleTextView\" and @text=\"Leagues\"]")

    def navigate_to_leagues(self):
        self.actions.click(self.__leagues_tab)
        actual_header = self.actions.get_element(self.__leagues_heading).text
        try:
            assert (actual_header == "Leagues")
        except AssertionError as ae:
            logging.error(f"Header text is not Leagues instead {actual_header}")
