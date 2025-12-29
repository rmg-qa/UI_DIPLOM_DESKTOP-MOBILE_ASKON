import allure
from selene import browser, be


class FabricPageDesktop:
    # локаторы фильтации тканей по цвету
    APPLY_BTN = ".//button[text()='Применить']"
    FILTERING_RESULT = ".//div[contains(@class, 'catalog__item-wrapper')][1]"

    @allure.step('Фильтруем ткань по переданному цвету')
    def filtering_of_fabrics_by_color(self, color):
        fabric_color = f'[data-color="{color}"]'
        browser.element(fabric_color).click()
        browser.element(FabricPageDesktop.APPLY_BTN).click()

    @allure.step('Результат фильтрации по определенному цвету')
    def result_of_filtering_the_fabric_by_color(self, result):
        browser.element(FabricPageDesktop.FILTERING_RESULT + f"//child::p[text()='{result}']").should(
            be.visible)


fabric_page = FabricPageDesktop()
