import logging

import pytest

import pages

"""
This file defines pytest fixtures used for setting up prerequisite workflows in automated tests. 
These fixtures utilize a Page Object Model approach to interact with the application, 
navigating through a series of pages and performing specific actions to reach desired states 
before executing test scenarios.

- `navigate_to_home_page`: A function-scoped fixture that guides the test through the initial 
setup process, continuing through favorite league and team selection, dismissing notifications, 
and verifying arrival at the home page by checking the displayed text. This setup ensures tests 
start from a consistent home page state.

- `navigate_to_search`: Also function-scoped, this fixture depends on `navigate_to_home_page` 
to first navigate to the home page. It then proceeds to the search functionality, preparing 
the application for tests that involve search operations. This layered approach to fixtures 
allows for modular and reusable setup sequences across different test cases.
"""

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

@pytest.fixture(scope='function')
def navigate_to_search(driver, navigate_to_home_page,  page_manager):
    favorites_landing_page = page_manager.get_page(pages.FavoritesLandingPage, driver)
    favorites_landing_page.enter_text_search_view()

