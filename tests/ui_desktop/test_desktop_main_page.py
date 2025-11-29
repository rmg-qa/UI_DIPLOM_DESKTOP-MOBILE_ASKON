import pytest

import data
import allure
from selene import browser, have
from network_monitor.network_logger import logger_network
from locators.locators_desktop import LocatorsMainPage, LocatorsResultGlobalSearch, LocatorsSelectionPillow
from pages.main_page_desktop import MainPageDesktop


@allure.epic('Главная страница')
@allure.title('Открытие основной страницы интернет-магазина "Askon"')
@allure.tag('web-desktop')
@allure.severity(allure.severity_level.CRITICAL)
def test_get_first_screen(browser_settings_desktop):
    with allure.step('Открытие основной страницы и проверка элемента на первом экране'):
        browser.open(data.URL)
        browser.element(LocatorsMainPage.catalog).should(have.text('Катал'))


@allure.epic('Главная страница')
@allure.title('Проверка результата выдачи глобального поисковика')
@allure.tag('web-desktop')
@allure.severity(allure.severity_level.CRITICAL)
def test_search_item(browser_settings_desktop):
    browser.open(data.URL)
    with allure.step('Ввод текста в общий поиск и проверка результата'):
        browser.element(LocatorsMainPage.global_search).type('диван').press_enter()
        browser.element(LocatorsResultGlobalSearch.title_result_search).should(have.text('Диваны'))


@allure.epic('Главная страница')
@allure.title('Добавление товара в корзину неавторизованным пользователем')
@allure.tag('web-desktop')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_item_in_cart_unauthorized_user(browser_settings_desktop):
    browser.open(data.URL)
    with allure.step('Скролл до блока "Хиты продаж". Реализовано в виде явного указания пикселей, '
                     'тк на сайте реализована ленивая загрузка данных'):
        browser.driver.execute_script("window.scrollBy(0, 1100);")
        browser.element(LocatorsMainPage.LocatorsBlockSalesHits.first_item_button_in_cart).click()
        browser.element(LocatorsMainPage.LocatorsSideBarCart.result_add_item_in_cart).should(
            have.text('В корзине 1 товар'))


@allure.epic('Главная страница')
@allure.title('Добавление товара в избранное неавторизованным пользователем')
@allure.tag('web-desktop')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_item_in_favourite_unauthorized_user(browser_settings_desktop):
    browser.open(data.URL)
    with allure.step(
            'Скролл до блока "Хиты продаж". Реализовано в виде явного указания пикселей, '
            'тк этот блок прогружается в процессе самого скролла'):
        browser.driver.execute_script("window.scrollBy(0, 1100);")
        browser.element(LocatorsMainPage.LocatorsBlockSalesHits.first_item_button_favorite).click()
        browser.element(LocatorsMainPage.success_popup).should(have.text('Товар добавлен в избранное'))


@allure.epic('Главная страница')
@allure.title('Подборка подушек из пены-специальной')
@allure.tag('web-desktop')
@allure.description('параметризуем выбор подушки специальной на 3 шаге подбора (всего 4 варианта выбора положения сна:'
                    '"на боку", "на спине", "на животе", "меняю положение во сне"')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize('locator_case, target_url, answers', [
    [LocatorsSelectionPillow.StepThreeSleepPosition.on_the_side, data.requests_result_select_pillow[0],
     data.answers_in_step_three[0]],
    [LocatorsSelectionPillow.StepThreeSleepPosition.on_the_back, data.requests_result_select_pillow[1],
     data.answers_in_step_three[1]],
    [LocatorsSelectionPillow.StepThreeSleepPosition.on_the_stomach, data.requests_result_select_pillow[2],
     data.answers_in_step_three[2]],
    [LocatorsSelectionPillow.StepThreeSleepPosition.i_change_my_position_in_my_sleep,
     data.requests_result_select_pillow[3], data.answers_in_step_three[3]]])
def test_select_pillow(browser_settings_desktop, locator_case, target_url, answers):
    with allure.step('Параметрируем тест с выбором подушки из пены-специальной. Затем получаем логи из вкладки network '
                     'и сравниваем query-параметры (answers) в финальном запросе на получение списка товаров'):
        MainPageDesktop.select_pillow(locator_case)
    with allure.step('Собираем логи, выявляем финальный запрос с query-параметрами ответов (answers)'):
        logs = browser.driver.execute("getLog", {'type': 'performance'})['value']
        logs_network = logger_network(logs)
        target_requests = [item for item in logs_network if item.get('url') == target_url]
        print(target_requests)
        final_url = target_requests[0]['url']
    assert answers in final_url
