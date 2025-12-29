import allure
from selene import browser, have


class SalonPageDesktop:
    # локаторы страницы салонов
    SALONS_LIST = ".//ul[contains(@class, 'map_list__')]"
    SALON_DETAILS = './/div[contains(@class,"shop_content")]'

    @allure.step('Выбираем первый салон в списке')
    def choosing_the_first_salon_in_the_list(self, name_salon):
        browser.element(SalonPageDesktop.SALONS_LIST + f"//child::div[text()='{name_salon}']").click()
        all_windows = browser.driver.window_handles  # получаем все открытые вкладки, переключаем драйвер на только что открытую
        browser.driver.switch_to.window(all_windows[1])

    @allure.step('Проверяем результат: описание выбранного салона')
    def the_result_of_choosing_a_salon(self, result):
        browser.element(SalonPageDesktop.SALON_DETAILS).should(have.text(result))


salon_page = SalonPageDesktop()
