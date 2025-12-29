import allure
from pages.desktop.faq_page import faq_page
from pages.desktop.main_page import main_page


@allure.epic('Страница FAQ')
@allure.title('Переход на страницу FAQ: "Как оформить заказ" через футер главной страницы')
@allure.tag('web-desktop')
@allure.severity(allure.severity_level.NORMAL)
def test_going_to_the_faq_page(setup_browser):
    main_page.open_the_page()
    main_page.opening_the_faq_page_via_the_main_page_footer()
    faq_page.going_to_the_question_how_place_a_order()
