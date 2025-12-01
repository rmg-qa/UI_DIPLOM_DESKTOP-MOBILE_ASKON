# Дипломный проект тестирования веб-версии онлайн-магазина Askona (Desktop/Mobile)
> [Askona](https://www.askona.ru)

![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](/images/first_screen_askona.png)

### Список реализованных автотестов:

#### UI-автотесты (Десктопная веб-версия сайта):
* ✅ Переход на главную страницу интернет-магазина "Askona"
* ✅ Проверка результата выдачи глобального поисковика
* ✅ Добавление товара в корзину неавторизованным пользователем
* ✅ Добавление товара в избранное неавторизованным пользователем
* ✅ Подборка подушек из пены-специальной

#### Мобильные автотесты для Android (Мобильная веб-версия сайта):
* ✅ Выбор раздела "Новогодние ёлки" через меню-бургер
* ✅ Переход на страницу "О компании" через футер страницы
* ✅ Добавление/удаление новогодней ёлки из корзины

### Используемые технологии
<p  align="center">
   <code><img width="5%" title="Python" src="images/python.png"></code>
   <code><img width="5%" title="PyCharm" src="images/pycharm.png"></code>
   <code><img width="5%" title="Android Studio" src="images/android_studio.png"></code>
   <code><img width="5%" title="Selene" src="images/selene.png"></code>
   <code><img width="5%" title="Selenium" src="images/selenium.png"></code>
   <code><img width="5%" title="Pydantic" src="images/Pydantic.png"></code>
   <code><img width="5%" title="Pytest" src="images/pytest.png"></code>
   <code><img width="5%" title="Appium" src="images/appium.png"></code>
   <code><img width="5%" title="Browserstack" src="images/browserstack.png"></code>
   <code><img width="5%" title="Jenkins" src="images/jenkins.png"></code>
   <code><img width="5%" title="Allure Report" src="images/allure_report.png"></code>
   <code><img width="5%" title="Allure TestOps" src="images/allure_testops.png"></code>
   <code><img width="5%" title="Jira" src="images/jira.png"></code>
   <code><img width="5%" title="Telegram" src="images/tg.png"></code>
</p>

Для написания UI-автотестов сайта "Askona" использовались:  
* `Python v. 3.13`: язык программирования; 
* `Pycharm`: среда разработки (IDE) для языка программирования Python;   
* `Android Studio`: среда разработки (IDE) для запуска и настройки мобильных автотестов;   
* `Selene`: поддерживаемый фреймворк вокруг инструмента `Selenium WebDriver`;  
* `Pydantic`: библиотека, с помощью которой реализован запуск мобильных автотестов в Browserstack, в эмуляторе Andriod Studio, или на реальном девайсе;  
* `PyTest`: библиотека модульного тестирования. В автотестах реализована параметризация;  
* `Appium`: фреймворк для автоматизации тестирования мобильной версии сайта;  
* `Browserstack`: облачная платформа для удаленного запуска мобильных автотестов.  
* `Jenkins`: инструмент CI/CD - с помощью этого инструмента реализован удаленный запуск автотестов, отправка уведомлений в Telegram, интеграция с TMS;  
* `ТестОпс`: TMS-платформа для управления тестированием программного обеспечения. Реализована интеграция с Jira;  
* `Jira`: комплексная система управления проектами;  
* `Selenoid`: запускает браузер с тестами в контейнерах Docker. Запись видео автотеста происходит с помощью этого инструмента;  
* `Allure Report`: собирает графический отчет о прохождении автотестов;  
* `BotFather`: настраиваемый бот в Telegram - с его помощью результаты прогона автотестов присылаются в Telegram в виде небольшого мини-отчета. 

### Локальный запуск UI автотестов (Desktop/Mobile)

1. Скачать проект и открыть в Pycharm   
2. Создайте следующие файлы:
   * `.env`, `.env.bstack`, `.env.local_emulator`, `.env.local_real` в зависимости от цели, заполните параметры в .env файлах актуальными данными.
   * Пример заполнения параметров указан в файле с расширением `.env.example`
3. Создайте и активируйте виртуальное окружение
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
4. Установите зависимости с помощью pip
   ```bash
   pip install -r requirements.txt
   ```
5. Для локального запуска автотестов необходимо выполнить команду в терминале:
    * Для десктопной версии:<br>
    ```bash
    pytest tests/ui_desktop
    ```
    * Для мобильной версии:<br>
    ```bash
    pytest tests/ui_mobile
    ```
   _Параметр запуска CONTEXT в мобильных автотестах_:  
   * ```CONTEXT="bstack" pytest tests/ui_mobile``` - запуск автотестов в облачной платформе Browserstack;  
   * ```CONTEXT="local_emulator" pytest tests/ui_mobile``` - запуск автотестов в эмуляторе Android Studio;  
   * ```CONTEXT="local_real" pytest tests/ui_mobile``` - запуск автотестов на реальном устройстве.<br>
<br>
* Для запуска всех автотестов выполните команду:<br>
   ```bash
   pytest tests
   ```
6. Выполнить запрос на формирование allure-отчета:
    ```bash
    allure serve allure-results
    ```

