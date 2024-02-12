import allure
import pytest

import pages


@allure.testcase("Test Players")
@pytest.mark.parametrize('load_test_data',['player_data.json'], indirect= True)
def test_player(driver, load_test_data, navigate_to_search, page_manager):
    for player_data in load_test_data:
        search_page = page_manager.get_page(pages.SearchPage, driver)
        search_page.search(player_data["player_name"])
        players_page = page_manager.get_page(pages.PlayersPage, driver)
        players_page.navigate_to_players()
        players_page.select_player(player_data["player_name"])
        players_page.verify_player_name_heading(player_data["player_name"])
        players_page.navigate_to_info()
        players_page.verify_player_info(player_data["player_info"])
        navigation_page = page_manager.get_page(pages.NavigationPages, driver)
        navigation_page.navigate_back()