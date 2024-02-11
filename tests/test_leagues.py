import allure
import pytest

import pages


@allure.testcase("Test Leagues")
@pytest.mark.parametrize('load_test_data',['league_data.json'], indirect= True)
def test_leagues(driver, load_test_data, navigate_to_home_page, page_manager):
    leagues_page = page_manager.get_page(pages.LeaguesPage, driver)
    leagues_page.navigate_to_leagues()





