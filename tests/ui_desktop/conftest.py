import pytest
import os
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import desktop_attach_allure

from dotenv import load_dotenv


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function')
def setup_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 60
    browser.config._save_screenshot_on_failure = False
    browser.config._save_page_source_on_failure = False
    options = Options()

    # Также можно добавить другие опции для решения проблемы таймаута в селеноиде
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--disable-web-security')
    options.add_argument('--allow-insecure-localhost')
    options.add_argument('--disable-blink-features=AutomationControlled')

    selenoid_capabilities = {
        "browserName": 'chrome',
        "browserVersion": '128.0',
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        },
        "acceptInsecureCerts": True  # доп настройка для решения проблемы таймаута в селеноиде
    }

    options.capabilities.update(selenoid_capabilities)
    login = os.getenv('LOGIN_SELENOID')
    password = os.getenv('PASSWORD_SELENOID')
    driver = webdriver.Remote(
        #command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        command_executor=f"http://127.0.0.1:4444/wd/hub",  # добавил ссылку на свой селеноид на ВМ
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
