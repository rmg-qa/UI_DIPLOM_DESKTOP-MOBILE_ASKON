import allure
import pytest
import allure_commons
from appium.options.android import UiAutomator2Options
from selene import browser
import utils.mobile_attach_result
from config.config_mobile import config
from appium import webdriver
import dotenv


@pytest.fixture(scope='function')
def mobile_management():
    options = UiAutomator2Options()
    options.load_capabilities({
        'platformVersion': '13.0',
        'browserName': config.BROWSER_NAME,
        'bstack:options': {
            "userName": config.BROWSERSTACK_USERNAME,
            "accessKey": config.BROWSERSTACK_ACCESS_KEY,
            "projectName": config.BROWSERSTACK_PROJECT_NAME,
            "buildName": config.BROWSERSTACK_BUILD_NAME,
            "sessionName": config.BROWSERSTACK_SESSION_NAME,
            'deviceName': config.DEVICE_NAME
        },
        'goog:chromeOptions': {
            'args': [
                '--disable-fre',
                '--no-first-run',
                '--disable-infobars',
                '--incognito',
                '--no-default-browser-check',
                '--lang=ru'
            ]
        }
    })

    if config.context == 'local_emulator':
        options.set_capability('udid', dotenv.dotenv_values('.env.local_emulator').get('UDID'))
    elif config.context == 'local_real':
        options.set_capability('udid', dotenv.dotenv_values('.env.local_real').get('UDID'))

    browser.config.timeout = config.timeout
    browser.config.wait_decorator = allure_commons._allure.step

    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(
            config.remote_url,
            options=options
        )

    yield

    # Attachments после теста
    utils.mobile_attach_result.attach_bstack_screenshot()
    utils.mobile_attach_result.attach_bstack_page_source()

    session_id = browser.driver.session_id
    if config.context == 'bstack':
        utils.mobile_attach_result.attach_bstack_video(session_id, version_driver="")

    browser.driver.quit()
