import logging

import allure
from appium.webdriver.common.appiumby import AppiumBy

import pages

'''
Page elements and methods related to Players page
'''
class PlayersPage(pages.BasePage):
    _players_tab = (AppiumBy.ACCESSIBILITY_ID,"Players")
    _recycler_view = "com.fivemobile.thescore:id/recyclerView"
    _player_name_heading = (AppiumBy.ID, "com.fivemobile.thescore:id/txt_player_name")
    _player_info = (AppiumBy.ACCESSIBILITY_ID,"Info")
    _title_locator = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.fivemobile.thescore:id/title']")
    _value_locator = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.fivemobile.thescore:id/value']")

    @allure.step("Navigate to Players tab")
    def navigate_to_players(self):
        self.actions.click(self._players_tab)

    @allure.step("Select Player")
    def select_player(self, player_name):
        player_element_locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().resourceId("{self._recycler_view}").childSelector(new UiSelector().textContains("{player_name}"))')
        self.actions.click(player_element_locator)

    @allure.step("Verify Player Name heading")
    def verify_player_name_heading(self, player_name):
        actual_player_name = self.actions.get_element(self._player_name_heading).text
        try:
            assert (actual_player_name.lower() == player_name.lower())
        except AssertionError as ae:
            logging.error(f"Actual player name {actual_player_name} does not match with expected name {player_name}")
            raise (f"Actual player name {actual_player_name} does not match with expected name {player_name}") from ae

    @allure.step("Navigate to Info sub-tab")
    def navigate_to_info(self):
        self.actions.click(self._player_info)
        is_player_info_selected = self.actions.get_element(self._player_info).is_selected()
        try:
            assert(is_player_info_selected == True)
        except AssertionError as ae:
            logging.error(f"Team status is not selected, actual : {is_player_info_selected}")
            raise AssertionError(f"Team status is not selected, actual : {is_player_info_selected}") from ae

    @allure.step("Verify Player Info")
    def verify_player_info(self, player_info):
        title_element = self.actions.get_element(self._title_locator)
        assert title_element.text == player_info['title'], "The title text does not match expected."
        value_element = self.actions.get_element(self._value_locator)
        assert  player_info['value'] in value_element.text, "The value text does not match expected."
