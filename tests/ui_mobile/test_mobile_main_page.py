import allure
from pages.mobile.main_page import main_page_mobile


@allure.epic('Главная страница')
@allure.title('Выбор определенного раздела/подраздела товара в меню-бургере')
@allure.tag('web-mobile')
@allure.severity(allure.severity_level.NORMAL)
def test_select_section_and_subsection_product_in_burger_menu(mobile_management):
    main_page_mobile.open_the_page()
    main_page_mobile.choosing_a_standard_location()
    main_page_mobile.choosing_category_and_subcategory_product(category='Матрасы', subcategory='Односпальные')
    main_page_mobile.results_selecting_product_category_and_subcategory(
        title_result='Односпальные матрасы', product_category='матрас')


@allure.epic('Главная страница')
@allure.title('Вывод товаров в подборщике подушек')
@allure.tag('web-mobile')
@allure.severity(allure.severity_level.NORMAL)
def test_showing_products_in_the_pillow_picker(mobile_management):
    main_page_mobile.open_the_page()
    main_page_mobile.choosing_a_standard_location()
    main_page_mobile.pillow_selection()
    main_page_mobile.result_of_pillows_selection()


@allure.epic('Главная страница')
@allure.title('Добавляем в корзину определенный товар неавторизованным пользователем')
@allure.tag('web-mobile')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_product_to_the_cart(mobile_management):
    main_page_mobile.open_the_page()
    main_page_mobile.choosing_a_standard_location()
    main_page_mobile.choosing_category_and_subcategory_product(category='Матрасы', subcategory='Односпальные')
    main_page_mobile.add_product_to_the_cart_from_internal_page()
    main_page_mobile.displaying_popup_after_adding_product_in_cart()
    main_page_mobile.deleting_product_from_cart()
    main_page_mobile.displaying_popup_after_adding_product_in_favourite()
