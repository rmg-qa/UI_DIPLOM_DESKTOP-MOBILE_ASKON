import allure
from pages.desktop.fabric_page import fabric_page
from pages.desktop.main_page import main_page


@allure.epic('Каталог тканей')
@allure.title('Переход на страницу "Каталога тканей" и проверка фильтрации по цвету')
@allure.tag('web-desktop')
@allure.severity(allure.severity_level.NORMAL)
def test_checking_the_color_filtering_in_the_fabrics_catalog(setup_browser):
    main_page.open_the_page()
    main_page.go_to_the_fabrics_catalog_in_header()
    fabric_page.filter_fabrics_by_color(color='Красный')
    fabric_page.result_filter_fabrics_by_color(result='Casanova')
