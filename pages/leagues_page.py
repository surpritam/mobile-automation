import logging

import allure
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

import pages


class LeaguesPage(pages.BasePage):
    _leagues_tab = (AppiumBy.XPATH,"//*[@resource-id=\"com.fivemobile.thescore:id/navigation_bar_item_small_label_view\" and @text=\"Leagues\"]")
    _leagues_heading = (AppiumBy.XPATH,"//*[@resource-id=\"com.fivemobile.thescore:id/titleTextView\" and @text=\"Leagues\"]")
    _recycler_view = "com.fivemobile.thescore:id/recyclerView"
    _league_name_heading = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id=\"com.fivemobile.thescore:id/titleTextView\"]")

    @allure.step("Navigate to Leagues tab")
    def navigate_to_leagues(self):
        self.actions.click(self._leagues_tab)
        actual_header = self.actions.get_element(self._leagues_heading).text
        try:
            assert (actual_header == "Leagues")
        except AssertionError as ae:
            logging.error(f"Header text is not Leagues instead {actual_header}")

    @allure.step("Select League")
    def select_league(self, league_name):
        league_element_locator = (AppiumBy.XPATH,f"//android.widget.TextView[@resource-id=\"com.fivemobile.thescore:id/league_name_text\" and @text=\"{league_name}\"]")
        self.actions.click(league_element_locator)

    @allure.step("Verify League Name heading")
    def verify_league_name_heading(self, league_name):
        actual_league_name = self.actions.get_element(self._league_name_heading).text
        try:
            assert (actual_league_name.lower() == league_name.lower())
        except AssertionError as ae:
            logging.error(f"Actual league name {actual_league_name} does not match with expected name {league_name}")
            raise (f"Actual league name {actual_league_name} does not match with expected name {league_name}") from ae

    @allure.step("Navigate to SubTab")
    def navigate_to_sub_tab(self, sub_tab):
        sub_tab_locator = (AppiumBy.ANDROID_UIAUTOMATOR,f'new UiSelector().description("{sub_tab}")')
        self.actions.click(sub_tab_locator)
        is_sub_tab_selected = self.actions.get_element(sub_tab_locator).is_selected()
        try:
            assert(is_sub_tab_selected == True)
        except AssertionError as ae:
            logging.error(f"{sub_tab} is not selected, actual : {is_sub_tab_selected}")
            raise AssertionError(f"{sub_tab} is not selected, actual : {is_sub_tab_selected}") from ae
    @allure.step("Verify Sub tab info")
    def verify_sub_tab(self, sub_tab_info):
        sub_tab_default_locator = (AppiumBy.XPATH,f"//android.widget.LinearLayout[@content-desc=\"{sub_tab_info}\"]")
        sub_tab_default_selected = self.actions.get_element(sub_tab_default_locator).is_selected()
        try:
            assert(sub_tab_default_selected == True)
        except AssertionError as ae:
            logging.error(f"{sub_tab_info} is not selected, actual : {sub_tab_default_selected}")
            raise AssertionError(f"{sub_tab_info} is not selected, actual : {sub_tab_default_selected}") from ae