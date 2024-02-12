# Mobile Application Testing Framework

This testing framework is developed for mobile application testing, utilizing Python, PyTest, Allure Reporting, and Appium with the Page Object Model (POM) design principles. It's designed to provide a robust, scalable, and easy-to-maintain testing solution for mobile applications.

## Project Pre-requisites

- [Python](https://www.python.org/downloads/) >= 3.x installed
- [Node/npm](https://nodejs.org/) installed
- [Android Studio](https://developer.android.com/studio) installed with `ANDROID_HOME` added to PATH
- [Java](https://www.oracle.com/ca-en/java/technologies/downloads/) installed with `JAVA_HOME` added to PATH
- [Appium](https://appium.io/docs/en/2.2/quickstart/install/) installed
- [UIAutomator2](https://appium.io/docs/en/2.0/quickstart/uiauto2-driver/) driver installed

## Setup Instructions

1. Clone the repository to your local machine.
2. Navigate to the project folder(if not already there)
3. Run `setup.sh` to install all project dependencies and set up the virtual environment.
   ```sh
   ./setup.sh

## Project Structure

- `allure-report`: Stores the test run report (`index.html`).
- `allure-result`: Stores result artifacts used to generate the Allure report.
- `config`: Contains generic configuration files, such as logging and test configurations in JSON format.
- `data`: Centralized storage for test data.
- `drivers`: Driver factory where the Appium driver is created based on the configuration from `config/test_config.json`.
- `logs`: Stores logs locally for each run with filenames in the format `test_log_<current_date_time>.log`.
- `pages`: Central repository for all page objects of the application. The `__init__.py` file stores references to all pages and methods, acting as a central reference for imports.
- `resources`: Stores the application under test.
- `tests`: Contains test definitions. The `conftest.py` file under `tests/` stores all prerequisite flows required in the actual tests, implemented as pytest fixtures.
- `utils`: Holds custom actions used to interact with page elements (e.g., `click`, `send_keys`, `get_element`).
- `conftest.py`: Defines methods used across all packages, added to pytest fixtures with defined scopes (`function` or `session`).
- `pytest.ini`: Pytest-specific configuration.
- `requirements.txt`: Framework dependencies.
- `run_tests.bat`: Batch file for test execution in a virtual environment on Windows.
- `run_tests.sh`: Shell script for test execution using a virtual environment on Mac/Linux.
- `setup.sh`: Script to install project dependencies and initiate the virtual environment.

Feel free to customize this template further to match your project's specific requirements, instructions, or any additional information you wish to include.
