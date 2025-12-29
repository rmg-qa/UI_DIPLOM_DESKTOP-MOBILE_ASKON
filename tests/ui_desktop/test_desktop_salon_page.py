import allure
from pages.desktop.main_page import main_page
from pages.desktop.salon_page import salon_page


@allure.epic('Страница "Салоны"')
@allure.title('Переход на страницу определенного салона в определенном городе')
@allure.tag('web-desktop')
@allure.severity(allure.severity_level.NORMAL)
def test_go_to_the_salon_page(setup_browser):
    main_page.open_the_page()
    main_page.search_and_select_the_city_in_the_header(input_text='Кемерово')
    main_page.checking_the_display_of_the_selected_city(result='Кемерово')
    main_page.go_to_the_salons_page()
    salon_page.choosing_the_first_salon_in_the_list(name_salon='ТЦ Радуга')
    salon_page.the_result_of_choosing_a_salon(result='ТЦ Радуга')
