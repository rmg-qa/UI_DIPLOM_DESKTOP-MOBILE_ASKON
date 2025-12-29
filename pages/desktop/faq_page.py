import allure
from selene import browser, have
from selenium.webdriver.common.by import By


class FAQPageDesktop:
    # локаторы вопросов
    HOW_TO_ORDER_SECTION = ".//li[contains(text(), 'Как оформить заказ')]"
    ONLINE_ORDER_QUESTION = ".//b[text()='Как оформить заказ в интернет-магазине?']"

    ORDER_INFO_LINK = ".//div[contains(text(), 'Информация на сайте в разделе «Покупателям»')]//child::u[contains(text(), 'Как оформить заказ')]"
    ORDER_INFO_TITLE = ".//h1[contains(@class,'information__wrapper_how_buy__title')]"

    @allure.step('Переход на вопрос: "Как оформить заказ в интернет магазине?"')
    def going_to_the_question_how_place_a_order(self):
        element_main_question = browser.driver.find_element(By.XPATH, FAQPageDesktop.HOW_TO_ORDER_SECTION)
        browser.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",
                                      element_main_question)
        browser.element(FAQPageDesktop.HOW_TO_ORDER_SECTION).click()
        element_embedded_question = browser.driver.find_element(By.XPATH, FAQPageDesktop.ONLINE_ORDER_QUESTION)
        browser.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",
                                      element_embedded_question)
        browser.element(FAQPageDesktop.ONLINE_ORDER_QUESTION).click()
        browser.element(FAQPageDesktop.ORDER_INFO_LINK).click()
        browser.element(FAQPageDesktop.ORDER_INFO_TITLE).should(have.text('Как оформить заказ'))


faq_page = FAQPageDesktop()
