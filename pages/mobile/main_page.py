import allure
from selene import browser, have, be
from selenium.webdriver.common.by import By
from test_data.data import url_main_page


class MainPageMobile:
    # стандартные локаторы
    LOCATION_CONFIRM_BTN = ".//button[text()='Да, верно']"
    BURGER_MENU_BTN = '[title="Меню"]'
    COOKIES_CONSENT_BTN = "[class='js-cookie-data-warning__close']"

    # категории и продукты
    TITLE_OF_THE_SELECTION_RESULT = './/h1[contains(@class, "TitleBlock_title")]'
    FIRST_PRODUCT_CARD = ".//div[contains(@class, 'ProductGrid_gridItem')][1]"
    THE_FIRST_ITEM_OF_THE_PRODUCT = './/div[contains(@class, "ProductGrid_gridI")][1]'

    # конструктор подушек
    PILLOW_DESIGNER = ".//a[contains(@class, 'PickupItem_card_')][3]"
    FIRST_CHOICE_IN_THE_PILLOW_DESIGNER = './/button[@data-test-picker="chose"][1]'
    PILLOW_RESULTS_HEADER = ".//div[text()=' Результаты подбора']"
    PILLOW_RESULTS_CONTAINER = './/div[contains(@class,"Results_wrapper")]'

    # Локаторы корзины
    ADD_TO_CART_BTN = '[data-test-card="add_basket"]'
    REMOVE_FROM_CART_ICON = '[data-name="IconBin"]'
    DELETE_CONFIRMATION_BUTTON = ".//button[@type='button' and text()='Удалить']"

    # системные уведомления
    CART_ADD_SUCCESS_MSG = ".//div[text()='Товар добавлен в корзину']"
    CART_REMOVE_SUCCESS_MSG = ".//div[text()='Товар удален из корзины']"

    @allure.step('Открытие страницы')
    def open_the_page(self):
        browser.open(url_main_page)

    @allure.step('Выбираем стандартную геопозицию: город "Москва"')
    def choosing_a_standard_location(self):
        browser.element(MainPageMobile.LOCATION_CONFIRM_BTN).should(be.clickable).click()

    @allure.step('Переходим в бургерное меню, выбираем определенную категорию')
    def choosing_category_and_subcategory_product(self, category, subcategory):
        locator_section = f".//span[text()='{category}' and contains(@class, 'style_text')]"
        locator_subsection = f".//span[text()='{subcategory}']"
        browser.element(MainPageMobile.BURGER_MENU_BTN).should(be.clickable).click()
        browser.element(locator_section).click()
        browser.element(locator_subsection).click()

    @allure.step('Проверяем результат выбора категории и подкатегории')
    def results_selecting_product_category_and_subcategory(self, title_result, product_category):
        browser.element(MainPageMobile.TITLE_OF_THE_SELECTION_RESULT).should(have.text(title_result))
        browser.element(
            MainPageMobile.FIRST_PRODUCT_CARD + f"//child::div[contains(text(), '{product_category}')]").should(
            be.visible)

    @allure.step('Выбор категорий товаров в конструкторе подушек')
    def pillow_selection(self):
        element = browser.driver.find_element(By.XPATH, MainPageMobile.PILLOW_DESIGNER)
        browser.driver.execute_script("arguments[0].scrollIntoView();", element)
        browser.element(MainPageMobile.PILLOW_DESIGNER).click()
        browser.element(MainPageMobile.FIRST_CHOICE_IN_THE_PILLOW_DESIGNER).click()
        browser.element(MainPageMobile.FIRST_CHOICE_IN_THE_PILLOW_DESIGNER).click()
        browser.element(MainPageMobile.FIRST_CHOICE_IN_THE_PILLOW_DESIGNER).click()
        browser.element(MainPageMobile.FIRST_CHOICE_IN_THE_PILLOW_DESIGNER).click()
        browser.element(MainPageMobile.FIRST_CHOICE_IN_THE_PILLOW_DESIGNER).click()

    @allure.step('Результат подбора подушек')
    def result_of_pillows_selection(self):
        browser.element(MainPageMobile.PILLOW_RESULTS_HEADER).should(be.visible)
        browser.element(MainPageMobile.PILLOW_RESULTS_CONTAINER).should(be.visible)

    @allure.step('Переходим внутрь товара и добавляем его в корзину')
    def add_product_to_the_cart_from_internal_page(self):
        browser.element(MainPageMobile.THE_FIRST_ITEM_OF_THE_PRODUCT).click()
        browser.element(MainPageMobile.COOKIES_CONSENT_BTN).should(be.clickable).click()
        browser.element(MainPageMobile.ADD_TO_CART_BTN).should(be.clickable).click()
        browser.element(MainPageMobile.CART_ADD_SUCCESS_MSG).should(be.present)

    @allure.step('Удаляем товар из корзины')
    def deleting_product_from_cart(self):
        browser.element(MainPageMobile.REMOVE_FROM_CART_ICON).should(be.clickable).click()
        browser.element(MainPageMobile.DELETE_CONFIRMATION_BUTTON).should(be.visible).click()
        browser.element(MainPageMobile.CART_REMOVE_SUCCESS_MSG).should(be.present)

    @allure.step('Проверка отображения попапа об успешном добавлении товара в корзину')
    def displaying_popup_after_adding_product_in_cart(self):
        browser.element(MainPageMobile.CART_ADD_SUCCESS_MSG).should(have.text('Товар добавлен в корзину'))

    @allure.step('Проверка отображения попапа об успешном удалении товара из корзины')
    def displaying_popup_after_adding_product_in_favourite(self):
        browser.element(MainPageMobile.CART_REMOVE_SUCCESS_MSG).should(be.present)


main_page_mobile = MainPageMobile()
