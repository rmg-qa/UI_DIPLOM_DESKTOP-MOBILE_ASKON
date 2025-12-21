import allure
from pages.desktop.fabric_page import fabric_page
from pages.desktop.faq_page import faq_page
from pages.desktop.main_page import main_page
from pages.desktop.salon_page import salon_page


@allure.epic('Главная страница')
@allure.title('Проверка результата выдачи глобального поисковика')
@allure.tag('web-desktop')
@allure.severity(allure.severity_level.CRITICAL)
def test_product_search_in_global_search(setup_browser):
    main_page.open_a_page()
    main_page.global_search(input_text='диван', search_result='Диваны')


@allure.epic('Главная страница')
@allure.title('Добавление товара в корзину неавторизованным пользователем')
@allure.tag('web-desktop')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_item_to_cart_unauthorized_user(setup_browser):
    main_page.open_a_page()
    main_page.global_search(input_text='диван', search_result='Диваны')
    main_page.adding_1_product_to_the_cart()


@allure.epic('Главная страница')
@allure.title('Добавление товара в избранное неавторизованным пользователем')
@allure.tag('web-desktop')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_item_to_favourite_unauthorized_user(setup_browser):
    main_page.open_a_page()
    main_page.global_search(input_text='диван', search_result='Диваны')
    main_page.adding_1_product_to_favorites()


@allure.epic('Главная страница')
@allure.title('Выбор города "Кемерово" в хедере страницы')
@allure.tag('web-desktop')
@allure.severity(allure.severity_level.NORMAL)
def test_choosing_another_city_in_the_header(setup_browser):
    main_page.open_a_page()
    main_page.choosing_another_city(input_text='Кемерово', choice_result='Кемерово')


@allure.epic('Страница FAQ')
@allure.title('Переход на страницу FAQ: "Как оформить заказ" через футер главной страницы')
@allure.tag('web-desktop')
@allure.severity(allure.severity_level.NORMAL)
def test_going_to_the_faq_page(setup_browser):
    main_page.open_a_page()
    main_page.opening_the_faq_page_via_the_main_page_footer()
    faq_page.going_to_the_question_how_place_a_order()


@allure.epic('Каталог тканей')
@allure.title('Переход на страницу "Каталога тканей" и проверка фильтрации красных тканей')
@allure.tag('web-desktop')
@allure.severity(allure.severity_level.NORMAL)
def test_go_to_the_fabric_catalog_and_check_the_filtering(setup_browser):
    main_page.open_a_page()
    main_page.go_to_the_fabric_catalog_page()
    fabric_page.filtration_of_red_tissues()


@allure.epic('Страница "Салоны"')
@allure.title('Переход на страницу салона "ТЦ Радуга" в г. Кемерово')
@allure.tag('web-desktop')
@allure.severity(allure.severity_level.NORMAL)
def test_go_to_the_page_of_the_salon_in_kemerovo(setup_browser):
    main_page.open_a_page()
    main_page.choosing_another_city(input_text='Кемерово', choice_result='Кемерово')
    main_page.go_to_the_salons_page()
    salon_page.choosing_the_salon_of_the_rainbow_shopping_center()
