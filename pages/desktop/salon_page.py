import allure
from selene import browser, be


class SalonPageDesktop:

    @allure.step('Выбираем перый салон в списке города "Кемерово" – "ТЦ Радуга"')
    def choosing_the_salon_of_the_rainbow_shopping_center(self):
        browser.element('.//ul[contains(@class, "map_list__")]//child::li[1]').click()
        all_windows = browser.driver.window_handles  # получаем все открытые вкладки, переключаем драйвер на только что открытую
        browser.driver.switch_to.window(all_windows[1])
        browser.element('.//div[contains(@class,"shop_content")]').should(be.present)


salon_page = SalonPageDesktop()
