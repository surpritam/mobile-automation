import logging

import pytest

import pages


@pytest.fixture(scope='function')
def navigate_to_home_page(driver, page_manager):
    logging.info(driver.session_id)
    initial_page = page_manager.get_page(pages.InitialPage, driver)
    favorite_league_page = page_manager.get_page(pages.FavoriteLeaguePage, driver)
    favorite_teams_page = page_manager.get_page(pages.FavoriteTeamsPage, driver)
    notifications_page = page_manager.get_page(pages.NotificationsPage, driver)
    favorites_landing_page = page_manager.get_page(pages.FavoritesLandingPage, driver)
    initial_page.navigate_initial_setup()
    favorite_league_page.continue_without_selecting()
    favorite_teams_page.choose_default_continue()
    notifications_page.default_notifications_deny()
    actual_text = favorites_landing_page.default_text_search_view()
    expected_title_text = "Teams, Players, and News"
    assert actual_text == expected_title_text, f"Expected title text '{expected_title_text}', but found '{actual_text}'"

