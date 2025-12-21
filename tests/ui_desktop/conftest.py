import pytest
import os
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import desktop_attach_allure

from dotenv import load_dotenv


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        help='Браузер, в котором будут запущены тесты',
        choices=['firefox', 'chrome'],
        default='chrome'
    )
    parser.addoption(
        '--browser_version',
        default='128.0',
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function')
def setup_browser(request):
    browser_name = request.config.getoption('--browser')
    browser_version = request.config.getoption('--browser_version')

    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 60

    options = Options()
    options.page_load_strategy = 'eager'

    # Также можно добавить другие опции для решения проблемы с askona.ru
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--disable-web-security')
    options.add_argument('--allow-insecure-localhost')

    selenoid_capabilities = {
        "browserName": browser_name,
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        },
        "acceptInsecureCerts": True  # Важно для SSL проблем!
    }

    options.capabilities.update(selenoid_capabilities)
    login = os.getenv('LOGIN_SELENOID')
    password = os.getenv('PASSWORD_SELENOID')
    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    driver.set_page_load_timeout(60)
    browser.config.driver = driver

    yield browser

    desktop_attach_allure.add_screenshot(browser)
    desktop_attach_allure.add_logs(browser)
    desktop_attach_allure.add_html(browser)
    desktop_attach_allure.add_video(browser)

    browser.quit()
