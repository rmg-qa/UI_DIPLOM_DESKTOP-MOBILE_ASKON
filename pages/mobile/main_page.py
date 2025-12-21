import allure
from selene import browser, have, be
from selenium.webdriver.common.by import By
from tests.data import url_main_page


class MainPageMobile:

    @allure.step('Открытие страницы')
    def open_a_page(self):
        browser.open(url_main_page)

    @allure.step('Выбираем стандартную геопозицию: город "Москва"')
    def choosing_a_standard_location(self):
        browser.element(".//button[text()='Да, верно']").should(be.clickable).click()

    @allure.step('Переходим в бургерное меню, в категорию "Матрасы-Односпальные"')
    def choosing_a_mattress_category_single(self):
        browser.element('[title="Меню"]').should(be.clickable).click()
        browser.element(".//span[text()='Матрасы' and contains(@class, 'style_text')]").click()
        browser.element(".//span[text()='Односпальные']").click()
        browser.element('.//h1[contains(@class, "TitleBlock_title")]').should(have.text('Односпальные матрасы'))
        browser.element('.//div[contains(@class, "ProductGrid_gridItem")][1]').should(be.present)

    @allure.step('Выбор товара в конструкторе подушек')
    def pillow_selection(self):
        element = browser.driver.find_element(By.XPATH, ".//a[contains(@class, 'PickupItem_card_')][3]")
        browser.driver.execute_script("arguments[0].scrollIntoView();", element)
        browser.element(".//a[contains(@class, 'PickupItem_card_')][3]").click()
        browser.element('.//button[@data-test-picker="chose"][1]').click()
        browser.element('.//button[@data-test-picker="chose"][1]').click()
        browser.element('.//button[@data-test-picker="chose"][1]').click()
        browser.element('.//button[@data-test-picker="chose"][1]').click()
        browser.element('.//button[@data-test-picker="chose"][1]').click()
        browser.element(".//div[text()=' Результаты подбора']").should(be.present)
        browser.element('.//div[contains(@class,"Results_wrapper")]').should(be.present)

    @allure.step('Переходим внутрь товара и добавляем его в корзину')
    def adding_the_product_to_the_cart_from_an_internal_page(self):
        browser.element('.//div[contains(@class, "ProductGrid_gridI")][1]').click()
        browser.element("[class='js-cookie-data-warning__close']").should(be.clickable).click()
        browser.element('[data-test-card="add_basket"]').should(be.clickable).click()
        browser.element(".//div[text()='Товар добавлен в корзину']").should(be.present)

    @allure.step('Удаляем товар из корзины')
    def deleting_an_item_from_the_shopping_cart(self):
        browser.element('[data-name="IconBin"]').should(be.clickable).click()
        browser.element(".//button[@type='button' and text()='Удалить']").should(be.visible).click()
        browser.element(".//div[text()='Товар удален из корзины']").should(be.present)


main_page_mobile = MainPageMobile()
