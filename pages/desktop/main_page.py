import allure
from selene import browser, have, be
from selenium.webdriver.common.by import By
from tests.data import url_main_page


class MainPageDesktop:

    @allure.step('Открытие страницы')
    def open_a_page(self):
        browser.open(url_main_page)

    @allure.step('Выбор города "Кемерово" в хедере главной страницы')
    def choosing_another_city(self, input_text, choice_result):
        browser.element('[data-test-header="location"]').click()
        browser.element('[data-test-header="location_input"]').type(input_text)
        browser.element('.//div[@data-test-city="list"]//child::b').click()
        browser.element('[data-test-header="location"]').should(have.text(choice_result))

    @allure.step('Выбор страницы "Салонов"')
    def go_to_the_salons_page(self):
        browser.element('[data-test-header="shops"]').click()

    @allure.step('Выбор страницы "Каталог тканей" через выпадающий список "Покупателям" в хедере главной страницы')
    def go_to_the_fabric_catalog_page(self):
        browser.element(".//div[text()='Покупателям']").click()
        browser.element('[data-test-burger="fabric-library"]').click()

    @allure.step('Ввод текста в глобальный поиск и проверка результата')
    def global_search(self, input_text, search_result):
        browser.element('[type="text"]').type(input_text).press_enter()
        browser.element('.//h1[contains(@class, "TitleBlock")]').should(have.text(search_result))
        browser.element('.//div[contains(@class, "ProductGrid_gridItem")][1]').should(be.visible)

    @allure.step('Добавление 1 товара в корзину')
    def adding_1_product_to_the_cart(self):
        browser.element(".//div[contains(@class, 'ProductGrid_gridI')][5]//child::button[text()='В корзину']").click()
        button_in_popup = ".//button[contains(@class, 'AddToCardPopupMain')]"
        try:
            browser.element(button_in_popup).should(be.visible)
            browser.element(button_in_popup).click()
        except:
            pass
        browser.element('.//div[contains(@class, "header_block")]').should(
            have.text('В корзине 1 товар'))

    @allure.step('Добавление 1 товара в избранное')
    def adding_1_product_to_favorites(self):
        browser.element(
            ".//div[contains(@class, 'ProductGrid_gridI')][1]//child::button[@data-test-listing='favorite']").click()
        browser.element('[data-test-site="success"]').should(have.text('Товар добавлен в избранное'))

    @allure.step('Переход на страницу FAQ через кнопку "Узнать" в футере страницы')
    def opening_the_faq_page_via_the_main_page_footer(self):
        element = browser.driver.find_element(By.XPATH, ".//a[text()='Узнать']")
        browser.driver.execute_script("arguments[0].scrollIntoView();", element)
        browser.element(".//a[text()='Узнать']").click()


main_page = MainPageDesktop()
