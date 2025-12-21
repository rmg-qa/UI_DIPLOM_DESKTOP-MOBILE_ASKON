import allure
from pages.mobile.main_page import main_page_mobile


@allure.epic('Главная страница')
@allure.title('Выбор раздела "Матрасы-Односпальные" в меню-бургере')
@allure.tag('web-mobile')
@allure.severity(allure.severity_level.NORMAL)
def test_go_to_the_mattresses_single_section(mobile_management):
    main_page_mobile.open_a_page()
    main_page_mobile.choosing_a_standard_location()
    main_page_mobile.choosing_a_mattress_category_single()


@allure.epic('Главная страница')
@allure.title('Вывод товаров в подборщике подушек')
@allure.tag('web-mobile')
@allure.severity(allure.severity_level.NORMAL)
def test_showing_products_in_the_pillow_picker(mobile_management):
    main_page_mobile.open_a_page()
    main_page_mobile.choosing_a_standard_location()
    main_page_mobile.pillow_selection()


@allure.epic('Главная страница')
@allure.title('Добавляем в корзину товар "Матрас-Односпальный" неавторизованным пользователем')
@allure.tag('web-mobile')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_to_cart_mattresses_single(mobile_management):
    main_page_mobile.open_a_page()
    main_page_mobile.choosing_a_standard_location()
    main_page_mobile.choosing_a_mattress_category_single()
    main_page_mobile.adding_the_product_to_the_cart_from_an_internal_page()
    main_page_mobile.deleting_an_item_from_the_shopping_cart()
