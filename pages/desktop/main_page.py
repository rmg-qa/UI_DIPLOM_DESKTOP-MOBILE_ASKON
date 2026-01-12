import time

import allure
from selene import browser, have, be
from selenium.webdriver.common.by import By
from test_data.data import url_main_page
from selenium.common.exceptions import NoSuchElementException
from selene.core.exceptions import TimeoutException


class MainPageDesktop:
    # локаторы хедера
    CITY_HEADER = '[data-test-header="location"]'
    CITY_SEARCH = '[data-test-header="location_input"]'
    FIRST_CITY_IN_LIST = './/div[@data-test-city="list"]//child::li[1]//child::b'
    SALONS_LINK = '[data-test-header="shops"]'
    CUSTOMERS_MENU = ".//div[text()='Покупателям']"
    FABRIC_LIBRARY_LINK = '[data-test-burger="fabric-library"]'
    # локаторы основного поиска
    MAIN_SEARCH_INPUT = '[type="text"]'

    # локаторы корзины
    ADD_TO_CART_BTN = ".//div[contains(@class, 'ProductGrid_gridI')][1]//child::button[text()='В корзину']"
    CONFIRM_ADD_POPUP = ".//button[contains(@class, 'AddToCardPopupMain')]"
    CART_HEADER = './/div[contains(@class, "header_block")]'
    BUTTON_ADD_TO_FAVOURITES = ".//div[contains(@class, 'ProductGrid_gridI')][1]//child::button[@data-test-listing='favorite']"
    # локаторы системных уведомлений
    FAV_SUCCESS_POPUP = '[data-test-site="success"]'
    # локаторы футера
    FOOTER_LEARN_LINK = ".//a[text()='Узнать']"
    # локаторы результата основного поиска
    PRICE_FILTER = './/div[@data-test-listing="Цена, ₽"]'
    SEARCH_RESULT_TITLE = './/h1[contains(@class, "TitleBlock")]'
    FIRST_SEARCH_RESULT = ".//div[contains(@class, 'ProductGrid_gridItem')][1]"
    # локаторы фильтрации товаров
    INPUT_MIN_PRICE = './/div[@data-test-listing="Цена, ₽"]//child::input[@data-view="min"]'
    INPUT_MAX_PRICE = './/div[@data-test-listing="Цена, ₽"]//child::input[@data-view="max"]'

    @allure.step('Открытие страницы')
    def open_the_page(self):
        browser.open(url_main_page)

    @allure.step('Ввод названия города и выбор результата выдачи в хедере главной страницы')
    def search_and_select_city_in_header(self, input_text):
        browser.element(MainPageDesktop.CITY_HEADER).click()
        browser.element(MainPageDesktop.CITY_SEARCH).type(input_text)
        browser.element(MainPageDesktop.FIRST_CITY_IN_LIST).click()

    @allure.step('Переход на страницу "Салонов" в хедере')
    def go_to_the_salons_page(self):
        browser.element(MainPageDesktop.SALONS_LINK).click()

    @allure.step('Выбор страницы "Каталог тканей" через выпадающий список "Покупателям" в хедере главной страницы')
    def go_to_the_fabrics_catalog_in_header(self):
        browser.element(MainPageDesktop.CUSTOMERS_MENU).click()
        browser.element(MainPageDesktop.FABRIC_LIBRARY_LINK).click()

    @allure.step('Поиск товара в главном поисковике')
    def search_product_from_title_bar(self, input_text):
        browser.element(MainPageDesktop.MAIN_SEARCH_INPUT).type(input_text).press_enter()
        browser.element(MainPageDesktop.FIRST_SEARCH_RESULT).should(be.visible)

    @allure.step('Добавление одного товара в корзину')
    def add_one_product_to_the_cart(self):
        browser.element(MainPageDesktop.ADD_TO_CART_BTN).click()
        try:
            browser.with_(timeout=3).element(MainPageDesktop.CONFIRM_ADD_POPUP).should(
                be.visible).click()
        except (NoSuchElementException, TimeoutException):
            pass

    @allure.step('Добавление одного товара в избранное')
    def add_one_product_to_favorites(self):
        browser.element(MainPageDesktop.BUTTON_ADD_TO_FAVOURITES).click()

    @allure.step('Переход на страницу FAQ через кнопку "Узнать" в футере страницы')
    def open_faq_page_in_footer(self):
        element = browser.driver.find_element(By.XPATH, MainPageDesktop.FOOTER_LEARN_LINK)
        browser.driver.execute_script("arguments[0].scrollIntoView();", element)
        browser.element(MainPageDesktop.FOOTER_LEARN_LINK).click()

    @allure.step('Фильтрация товаров по определенной цене: от и до')
    def filtering_products_by_price(self, price_from, price_up_to):
        element = browser.driver.find_element(By.XPATH, MainPageDesktop.PRICE_FILTER)
        browser.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        browser.element(MainPageDesktop.INPUT_MIN_PRICE).type(price_from)
        browser.element(MainPageDesktop.INPUT_MAX_PRICE).type(price_up_to)
        time.sleep(5)  # запрос на фильтрацию происходит автоматически, ждем, когда прогрузится страница

    @allure.step('Проверка отображения цены первого товара после фильтрации')
    def checking_display_filtered_product_by_price(self, price_from, price_up_to):
        filtered_product_by_price = browser.element(
            MainPageDesktop.FIRST_SEARCH_RESULT + '//child::div[@data-test-listing="new_price"]')
        price_text = filtered_product_by_price.locate().text
        price_value = int(price_text.replace('₽', '').replace(' ', '').strip())
        assert price_up_to > price_value > price_from

    @allure.step('Проверка результата отображения выбранного города в хедере страницы')
    def checking_display_selected_city(self, result):
        browser.element(MainPageDesktop.CITY_HEADER).should(have.text(result))

    @allure.step('Проверка отображения результата главного поисковика')
    def global_search_product_result(self, result):
        browser.element(
            MainPageDesktop.FIRST_SEARCH_RESULT + f"//child::div[text()='{result}']").should(
            be.visible)

    @allure.step('Проверка отображения попапа об успешном добавлении товара в корзину')
    def verify_cart_added_desktop(self):
        browser.element(MainPageDesktop.CART_HEADER).should(have.text('В корзине 1 товар'))

    @allure.step('Проверка отображения попапа об успешном добавлении товара в избранное')
    def verify_favorite_added_desktop(self):
        browser.element(MainPageDesktop.FAV_SUCCESS_POPUP).should(
            have.text('Товар добавлен в избранное'))


main_page = MainPageDesktop()
