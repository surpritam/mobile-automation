import allure
import pytest

from pages.favorites_landing_page import FavoritesLandingPage
from pages.search_page import SearchPage
from pages.teams_page import TeamsPage


@allure.testcase("Test Teams")
@pytest.mark.parametrize('load_test_data',['teams_data.json'], indirect= True)
def test_teams(driver, load_test_data, navigate_to_home_page, page_manager):
    favorites_landing_page = page_manager.get_page(FavoritesLandingPage, driver)
    favorites_landing_page.enter_text_search_view()
    search_page = page_manager.get_page(SearchPage, driver)
    search_page.search("Toronto Maple Leafs")
    teams_page = page_manager.get_page(TeamsPage, driver)
    teams_page.navigate_to_teams()
    teams_page.select_team("Toronto Maple Leafs")
    teams_page.select_team_stats("Toronto Maple Leafs",{'header':'OFFENSIVE STATS','header_secondary':'(RANK)'})