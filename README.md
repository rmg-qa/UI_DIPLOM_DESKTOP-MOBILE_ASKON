# Проект Web (Desktop/Mobile) тестирования онлайн-магазина Askona
> [Askona](https://www.askona.ru)

![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](/images/first_screen_askona.png)

### Используемые технологии
<p  align="center">
   <code><img width="5%" title="Python" src="images/python.png"></code>
  <code><img width="5%" title="Pytest" src="images/pytest.png"></code>
  <code><img width="5%" title="Requests" src="images/requests.png"></code>
  <code><img width="5%" title="Selene" src="images/selene.png"></code>
  <code><img width="5%" title="Selenium" src="images/selenium.png"></code>
   <code><img width="5%" title="Appium" src="images/appium.png"></code>
   <code><img width="5%" title="Browserstack" src="images/browserstack.png"></code>
   <code><img width="5%" title="PyCharm" src="images/pycharm.png"></code>
  <code><img width="5%" title="Android Studio" src="images/android_studio.png"></code>
  <code><img width="5%" title="Jenkins" src="images/jenkins.png"></code>
  <code><img width="5%" title="Allure Report" src="images/allure_report.png"></code>
  <code><img width="5%" title="Allure TestOps" src="images/allure_testops.png"></code>
  <code><img width="5%" title="Jira" src="images/jira.png"></code>
  <code><img width="5%" title="Telegram" src="images/tg.png"></code>
  <code><img width="5%" title="Pydantic" src="images/pydantic.png"></code>
</p>

### Список реализованных автотестов:

#### UI-автотесты (Десктопная веб-версия сайта):
* ✅ Переход на главную страницу интернет-магазина "Askona"
* ✅ Проверка результата выдачи глобального поисковика
* ✅ Добавление товара в корзину неавторизованным пользователем
* ✅ Добавление товара в избранное неавторизованным пользователем
* ✅ Подборка подушек из пены-специальной - реализовано с использованием параметризации pytest.mark.parametrize

#### Мобильные-автотесты (Мобильная веб-версия сайта):
* ✅ Выбор раздела "Новогодние ёлки" через меню-бургер
* ✅ Переход на страницу "О компании" через футер страницы
* ✅ Добавление/удаление новогодней ёлки из корзины