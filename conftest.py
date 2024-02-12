import json
import logging.config
import os
import allure
import pytest
from drivers.driver_factory import get_appium_driver
from datetime import datetime

from pages.page_objects_manager import PageObjectManager

'''
Centralized pytest fixtures, configurations, and hooks for test setup and teardown processes. 
'''
@pytest.fixture(scope="function")
def driver(request):
    """
    Prepare for the test.
    """
    logging.info("Initializing the Appium driver.")
    driver = get_appium_driver()
    driver_session_id = driver.session_id
    logging.info(f"Driver session id {driver_session_id}")
    yield driver
    logging.info("Quitting the Appium driver.")
    driver.quit()

@pytest.fixture(scope="session")
def page_manager():
    """Session-scoped PageObjectManager fixture"""
    manager = PageObjectManager()
    yield manager

@pytest.fixture(scope="function")
def load_test_data(request):
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    file_name = request.param
    with open(os.path.join(data_dir, file_name)) as f:
        return json.load(f)


def load_logging_config():
    config_path = os.path.join(os.path.dirname(__file__), 'config/logging_config.json')
    # Format the current date and time
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    with open(config_path, 'r') as config_file:
        logging_config = json.load(config_file)
    # Adjust file paths in handlers to be absolute
    for handler in logging_config['handlers'].values():
        if 'filename' in handler:
            handler['filename'] = os.path.join(os.path.dirname(__file__), handler['filename'] + '_' + timestamp + '.log')
    return logging_config


@pytest.fixture(scope="session", autouse=True)
def configure_logging():
    logging_config = load_logging_config()
    logging.config.dictConfig(logging_config)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Extends the Pytest Plugin to take and embed screenshot in html report, on test failure.
    """
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        # Only add screenshots for UI tests involving the driver
        if "driver" in item.fixturenames:  # Check if the test had the driver fixture
            driver = item.funcargs["driver"]  # Get the driver fixture instance
            take_screenshot(driver, item.nodeid)  # Capture and attach the screenshot

def take_screenshot(driver, test_name):
    """
    Captures the screenshot and attaches it to the Allure report.
    """
    try:
        # Replace invalid characters in file names
        safe_test_name = test_name.replace("/", "_").replace(":", "_").replace("\n", "_")
        allure.attach(driver.get_screenshot_as_png(),name=safe_test_name, attachment_type=allure.attachment_type.PNG)
    except Exception as e:
        logging.info(f"Failed to take screenshot: {e}")
