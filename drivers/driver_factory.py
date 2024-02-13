from appium import webdriver
from appium.options.android import UiAutomator2Options
import os
import json

'''
This Python script provides functions for configuring and initializing an Appium driver for mobile app testing. It includes:
Configuration Loading: Loads testing settings from test_config.json, specifying Appium driver capabilities.
Driver Initialization: Creates and returns an Appium driver with settings derived from the loaded configuration, ready for automating tests on Android devices.
'''
def __load_config():
    config_path = os.path.join(os.path.dirname(__file__),'..','config/test_config.json')
    with open(config_path,'r') as config_file:
        return json.load(config_file)


def get_appium_driver():
    config = __load_config()
    android_capability = config.get('android_capability',{})
    base_dir = os.path.dirname(os.path.dirname(__file__))
    apk_path = os.path.join(base_dir, 'resources', android_capability.get('app',''))
    server_url = config.get('serverUrl','http://localhost:4723')
    capabilities = {
        'platformName': android_capability.get('platformName',''),
        'automationName': android_capability.get('automationName',''),
        'deviceName': android_capability.get('deviceName',''),
        'appPackage': android_capability.get('appPackage',''),
        'app': apk_path
    }
    driver = webdriver.Remote(server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    return driver
