import logging

import allure
from appium.webdriver.common.appiumby import AppiumBy

import pages


class TeamsPage(pages.BasePage):
    __teams_tab = (AppiumBy.XPATH,"//android.widget.TextView[@text=\"TEAMS\"]")
    __team_name_heading = (AppiumBy.ID, "com.fivemobile.thescore:id/team_name")
    __team_stats = (AppiumBy.XPATH, "//android.widget.LinearLayout[@content-desc=\"Team Stats\"]")
    __team_stats_header = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id=\"com.fivemobile.thescore:id/header_text\"]")
    __team_stats_header_secondary = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id=\"com.fivemobile.thescore:id/header_secondary_text\"]")
    _team_list_recycler_view = "com.fivemobile.thescore:id/recyclerView"
    _team_info = (AppiumBy.XPATH, "//android.widget.LinearLayout[@content-desc=\"Info\"]")

    @allure.step("Navigate to Teams tab")
    def navigate_to_teams(self):
        self.actions.click(self.__teams_tab)

    @allure.step("Verify team name heading")
    def verify_team_name_heading(self, team_name):
        actual_team_name = self.actions.get_element(self.__team_name_heading).text
        try:
            assert (actual_team_name.lower() == team_name.lower())
        except AssertionError as ae:
            logging.error(f"Actual team name {actual_team_name} does not match with expected name {team_name}")
            raise(f"Actual team name {actual_team_name} does not match with expected name {team_name}")

    @allure.step("Select Team")
    def select_team(self, team_name):
        team_element_locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().resourceId("{self._team_list_recycler_view}").childSelector(new UiSelector().text("{team_name}"))')
        team_element = self.actions.get_element(team_element_locator)
        self.actions.click(team_element)
        self.verify_team_name_heading(team_name)

    @allure.step("Select team stats")
    def navigate_team_stats(self, team_name, expected_team_stats):
        self.actions.click(self.__team_stats)
        is_team_status_selected = self.actions.get_element(self.__team_stats).is_selected()
        try:
            assert (is_team_status_selected == True)
        except AssertionError as ae:
            logging.error(f"Team stats is not selected, actual: {is_team_status_selected}")
            raise AssertionError(f"Team stats is not selected, actual: {is_team_status_selected}") from ae

        self.verify_team_name_heading(team_name)
        self.verify_team_stats(expected_team_stats)

    @allure.step("Verify team stats heading")
    def verify_team_stats(self, expected_team_stats):
        logging.info(f"Expected status {expected_team_stats}")
        actual_team_stats_header = self.actions.get_element(self.__team_stats_header).text
        actual_team_stats_header_secondary = self.actions.get_element(self.__team_stats_header_secondary).text
        try:
            assert (actual_team_stats_header == expected_team_stats['header'])
        except AssertionError as ae:
            logging.error(f"Actual header {actual_team_stats_header} did not match with expected: {expected_team_stats['header']}")
            raise AssertionError(f"Actual header {actual_team_stats_header} did not match with expected: {expected_team_stats['header']}") from ae

        try:
            assert (actual_team_stats_header_secondary == expected_team_stats['header_secondary'])
        except AssertionError as ae:
            logging.error(f"Actual header {actual_team_stats_header_secondary} did not match with expected: {expected_team_stats['header_secondary']}")
            raise AssertionError(f"Actual header {actual_team_stats_header_secondary} did not match with expected: {expected_team_stats['header_secondary']}") from ae

    @allure.step("Navigate team info")
    def navigate_team_info(self):
        self.actions.click(self._team_info)