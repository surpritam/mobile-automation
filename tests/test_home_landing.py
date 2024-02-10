import allure
import pytest

from pages.leagues_page import LeaguesPage


@allure.testcase("Test Leagues")
@pytest.mark.parametrize('load_test_data',['teams_data.json'], indirect= True)
def test_leagues(driver, load_test_data, navigate_to_home_page):
    leagues_page = LeaguesPage(driver)
    leagues_page.navigate_to_leagues()





