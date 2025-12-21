import allure
from selene import browser, have


class FAQPageDesktop:

    @allure.step('Переход на вопрос: "Как оформить заказ в интернет магазине?"')
    def going_to_the_question_how_place_a_order(self):
        browser.element(".//li[contains(text(), 'Как оформить заказ')]").click()
        browser.element(".//b[text()='Как оформить заказ в интернет-магазине?']").click()
        browser.element(
            ".//div[contains(text(), 'Информация на сайте в разделе «Покупателям»')]//child::u[contains(text(), 'Как оформить заказ')]").click()
        browser.element(".//h1[contains(@class,'information__wrapper_how_buy__title')]").should(
            have.text('Как оформить заказ'))


faq_page = FAQPageDesktop()
