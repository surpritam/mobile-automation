import allure
import pytest

import pages

'''
Tests related to Leagues
'''
@allure.testcase("Test Leagues")
@pytest.mark.parametrize('load_test_data',['league_data.json'], indirect= True)
@pytest.mark.regression
def test_leagues(driver, load_test_data, navigate_to_home_page, page_manager):
    '''
    Scenario: Select a league and verify standings
    '''
    leagues_page = page_manager.get_page(pages.LeaguesPage, driver)
    leagues_page.navigate_to_leagues()
    for league_data in load_test_data:
        leagues_page.select_league(league_data["league_name"])
        leagues_page.verify_league_name_heading(league_data["league_name"])
        leagues_page.navigate_to_sub_tab(league_data["sub_tab"])
        leagues_page.verify_sub_tab(league_data["league_standings"])
        navigation_page = page_manager.get_page(pages.NavigationPages, driver)
        navigation_page.navigate_back()






