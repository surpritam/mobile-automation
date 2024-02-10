import logging

import allure
import pytest

from pages.choose_favorite_league_page import FavoriteLeaguePage
from pages.choose_favorite_teams_page import FavoriteTeamsPage
from pages.favorites_landing_page import FavoritesLandingPage
from pages.notifications_page import NotificationsPage
from pages.welcome_page import InitialPage

@allure.testcase("Test Landing")
@pytest.mark.parametrize('load_test_data',['teams_data.json'], indirect= True)
def test_home_landing(driver, load_test_data):
    initial_page = InitialPage(driver)
    favorite_league_page = FavoriteLeaguePage(driver)
    favorite_teams_page = FavoriteTeamsPage(driver)
    notifications_page = NotificationsPage(driver)
    favorites_landing_page = FavoritesLandingPage(driver)
    initial_page.navigate_initial_setup()
    favorite_league_page.continue_without_selecting()
    favorite_teams_page.choose_default_continue()
    notifications_page.default_notifications_deny()
    actual_text = favorites_landing_page.default_text_search_view()
    expected_title_text = "Teams, Players, and News"
    assert actual_text == expected_title_text, f"Expected title text '{expected_title_text}', but found '{actual_text}'"
    assert load_test_data.get("favoriteTeam") == "Mercedes"
    logging.info(load_test_data.get("favoriteTeam"))



