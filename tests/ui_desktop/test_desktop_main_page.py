import allure
from pages.desktop.main_page import main_page


@allure.epic('Главная страница')
@allure.title('Проверка результата выдачи основного поисковика')
@allure.tag('web-desktop')
@allure.severity(allure.severity_level.CRITICAL)
def test_product_search_in_global_search(setup_browser):
    main_page.open_the_page()
    main_page.search_from_title_bar(input_text='Коврик для ванной')
    main_page.title_bar_search_result(result='Коврик для ванной')


@allure.epic('Главная страница')
@allure.title('Добавление товара в корзину неавторизованным пользователем')
@allure.tag('web-desktop')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_item_to_cart_unauthorized_user(setup_browser):
    main_page.open_the_page()
    main_page.search_from_title_bar(input_text='диван')
    main_page.add_one_product_to_the_cart()
    main_page.verify_cart_added_desktop()


@allure.epic('Главная страница')
@allure.title('Добавление товара в избранное неавторизованным пользователем')
@allure.tag('web-desktop')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_item_to_favourite_unauthorized_user(setup_browser):
    main_page.open_the_page()
    main_page.search_from_title_bar(input_text='диван')
    main_page.add_one_product_to_favorites()
    main_page.verify_favorite_added_desktop()


@allure.epic('Главная страница')
@allure.title('Выбор определенного города в хедере страницы')
@allure.tag('web-desktop')
@allure.severity(allure.severity_level.NORMAL)
def test_choosing_another_city_in_the_header(setup_browser):
    main_page.open_the_page()
    main_page.search_and_select_the_city_in_the_header(input_text='Кемерово')
    main_page.checking_the_display_of_the_selected_city(result='Кемерово')


@allure.epic('Главная страница')
@allure.title('Проверка фильтрации товара по цене')
@allure.tag('web-desktop')
@allure.severity(allure.severity_level.CRITICAL)
def test_filtering_products_by_price(setup_browser):
    main_page.open_the_page()
    main_page.search_from_title_bar(input_text='диван')
    main_page.filtering_products_by_price(price_from=5000, price_up_to=10000)
    main_page.checking_the_display_of_the_filtered_product_by_price(price_from=5000, price_up_to=10000)
