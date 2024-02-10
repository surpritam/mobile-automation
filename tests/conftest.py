import pytest

from pages.choose_favorite_league_page import FavoriteLeaguePage
from pages.choose_favorite_teams_page import FavoriteTeamsPage
from pages.favorites_landing_page import FavoritesLandingPage
from pages.notifications_page import NotificationsPage
from pages.welcome_page import InitialPage


@pytest.fixture(scope='function')
def navigate_to_home_page(driver):
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
