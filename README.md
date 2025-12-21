# Дипломный проект тестирования веб-версии онлайн-магазина Askona (UI: Desktop/Mobile)
> [Askona](https://www.askona.ru)

![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](/images/first_screen_askona.png)

### Список реализованных автотестов:

#### UI-автотесты (Десктопная версия сайта):
* ✅ Проверка результата выдачи глобального поисковика
* ✅ Добавление товара в корзину неавторизованным пользователем
* ✅ Добавление товара в избранное неавторизованным пользователем
* ✅ Выбор города "Кемерово" в хедере страницы
* ✅ Переход на страницу FAQ: "Как оформить заказ" через футер главной страницы
* ✅ Переход на страницу "Каталога тканей" и проверка фильтрации красных тканей
* ✅ Переход на страницу салона "ТЦ Радуга" в г. Кемерово

#### Мобильные автотесты для Android (Мобильная версия сайта):
* ✅ Выбор раздела "Матрасы-Односпальные" в меню-бургере
* ✅ Вывод товаров в подборщике подушек
* ✅ Добавляем в корзину товар "Матрас-Односпальный" неавторизованным пользователем

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

* `Python v. 3.13`: язык программирования; 
* `Pycharm`: среда разработки (IDE) для языка программирования Python;   
* `Android Studio`: среда разработки (IDE) для запуска и настройки мобильных автотестов;   
* `Selene`: поддерживаемый фреймворк, под капотом используется `Selenium WebDriver`;  
* `Pydantic`: библиотека, с помощью которой реализована конфигурация запуска мобильных автотестов: в Browserstack, на эмуляторе, или на реальном девайсе;
* `PyTest`: библиотека модульного тестирования. В автотестах реализована параметризация;  
* `Appium`: фреймворк для автоматизации тестирования мобильной версии сайта;  
* `Browserstack`: облачная платформа для удаленного запуска мобильных автотестов.  
* `Jenkins`: инструмент CI/CD - с помощью этого инструмента реализован удаленный запуск автотестов, отправка уведомлений в Telegram, интеграция с TMS;  
* `ТестОпс`: TMS-платформа для управления тестированием программного обеспечения. Есть совмещение ручного теста и автотестов в одной системе. Реализована интеграция с Jira;  
* `Jira`: комплексная система управления проектами;  
* `Selenoid`: запускает браузер с тестами в контейнерах Docker (и записывает видео);  
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
   ```CONTEXT="bstack" pytest tests/ui_mobile``` - запуск автотестов в облачной платформе Browserstack;  
   ```CONTEXT="local_emulator" pytest tests/ui_mobile``` - запуск автотестов в эмуляторе Android Studio;  
   ```CONTEXT="local_real" pytest tests/ui_mobile``` - запуск автотестов на реальном устройстве.<br>
    * Для запуска всех автотестов выполните команду:<br>
    ```bash
      pytest tests
    ```

6. Выполнить запрос на формирование allure-отчета:
    ```bash
    allure serve allure-results
    ```

<!-- Jenkins -->

### <img width="3%" title="Jenkins" src="images/jenkins.png"> Запуск проекта в Jenkins
##### В конфигурациях джобы реализованы параметры запуска автотестов с возможностью выбора: только дестоп, только мобильные, или запуск всех автотестов сразу.
### [Задача в Jenkins](https://jenkins.autotests.cloud/job/UI_DIPLOM_DESKTOP_AND_MOBILE_ROMAN_GOROKHOVIK/)
![This is a image](images/job_jenkins.png)


<!-- Allure report -->

### <img width="3%" title="Allure Report" src="images/allure_report.png"> Allure report

##### Результаты выполнения тестов можно посмотреть в Allure-отчете
![This is a image](images/allure_dashboard.png)
![This is a image](images/allure-suites.png)


##### Видео прохождение теста на мобильном устройстве

![Видео запуска мобильного автотеста!](images/test_add_item_in_cart.gif)

<!-- Allure TestOps -->

### <img width="3%" title="Allure TestOps" src="images/allure_testops.png"> Интеграция с Allure TestOps

### [Dashboard](https://allure.autotests.cloud/project/5023/dashboards)

![This is an image](images/allure_testops_dash.png)
![This is an image](images/run_manual_test.png)


<!-- Jira -->

### <img width="3%" title="Jira" src="images/jira.png"> Интеграция с Jira

![This is an image](images/jira_1.png)
![This is an image](images/jira_2.png)


<!-- Telegram -->

### <img width="3%" title="Telegram" src="images/tg.png"> Оповещения в Telegram
##### После выполнения тестов в Telegram bot приходит сообщение с графиком и информацией о тестовом прогоне. Реализовано оповещение, только когда тесты падают (условия оповещения настроены в Jenkins job).

![Уведомление только тогда, когда тест падает. Настраивается в джобе Jenkins](images/notification_fail_tests.png)