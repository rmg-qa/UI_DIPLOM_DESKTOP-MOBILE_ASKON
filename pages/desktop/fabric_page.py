import allure
from selene import browser, be

class FabricPageDesktop:

    @allure.step('Фильтруем ткань по красному цвету')
    def filtration_of_red_tissues(self):
        browser.element('[data-color="Красный"]').click()
        browser.element(".//button[text()='Применить']").click()
        browser.element(".//div[contains(@class, 'catalog__item-wrapper')][1]").should(be.visible)


fabric_page = FabricPageDesktop()
