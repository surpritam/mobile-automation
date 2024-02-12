import logging

import allure
import pytest

import pages


@allure.testcase("Test Teams")
@pytest.mark.parametrize('load_test_data',['teams_data.json'], indirect= True)
def test_teams(driver, load_test_data, navigate_to_search, page_manager):
    for team_data in load_test_data:
        search_page = page_manager.get_page(pages.SearchPage, driver)
        search_page.search(team_data["team_name"])
        teams_page = page_manager.get_page(pages.TeamsPage, driver)
        teams_page.navigate_to_teams()
        teams_page.select_team(team_data["team_name"])
        teams_page.navigate_team_stats(team_data["team_name"], team_data["stats"])
        navigation_page = page_manager.get_page(pages.NavigationPages, driver)
        navigation_page.navigate_back()
