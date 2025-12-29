import allure
from pages.desktop.fabric_page import fabric_page
from pages.desktop.main_page import main_page


@allure.epic('Каталог тканей')
@allure.title('Переход на страницу "Каталога тканей" и проверка фильтрации по цвету')
@allure.tag('web-desktop')
@allure.severity(allure.severity_level.NORMAL)
def test_go_to_the_fabric_catalog_and_check_the_filtering(setup_browser):
    main_page.open_the_page()
    main_page.go_to_the_fabric_catalog_page()
    fabric_page.filtering_of_fabrics_by_color(color='Красный')
    fabric_page.result_of_filtering_the_fabric_by_color(result='Casanova')
