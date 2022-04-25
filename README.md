# Magic The Gathering LADDER
## Архитектура REST API
Архитектура REST API - микросервисная. Это означает, что приложение состоит из небольших независимых сервисов, которые связываются между друг другом простейшим HTTP запросом. Благодаря такому подходу приложение имеет горизонтальное масштабирование. На данный момент список сервисов выглядит так:
- USER SERVICE. Предоставляет функции для работы с пользователями - авторизация, регистрация и т.п. **Корень** - /api/auth/
- CARD SERVICE. Предоставляет функции для работы с картами Magic The Gathering и правилами для них. **Корень** - /api/cards/

## Запуск веб-приложения
Перед запуском веб-приложения обязательно прочтите раздел ["Настройка Django"](#настройка-django)
Для запуска веб-приложения необходимо установить docker и docker-compose.
Порядок действий:
- Перейдите в папку docker/sugar-clicker_instances
  ```bash 
  cd docker/sugar-clicker_instances
  ```
- Скопируйте содержимое файла .env.sample в новосозданный файл .env
  ```bash
  cp .env.sample .env
  ```
- Отредактируйте файл .env под себя, подробнее можно [здесь](#редактирование-env)
- Соберите проект
  ```bash
  ./build
  ``` 
  или
  ```bash
  docker-compose build
  ```
- Запуск осуществляется с помощью
  ```bash
  ./start
  ```
  или
  ```bash
  docker-compose up -d
  ```
- Остановка осуществляется с помощью
  ```bash
  ./stop
  ```
  или
  ```bash
  docker-compose down
   ```
## Редактирование .env
С помощью граммотной настройки переменного накружения вы сможете запустить проект в удобном месте на вашем компьютере. Рассмотрим, за что отвечае каждая переменная
```NETWORK=172.100.1.49/24```
Укажите здесь сеть, по которой будут взаимодействовать docker-контейнеры. Формат - IPv4/24
    
    HTTP_PORT=80
    HTTPS_PORT=443
 Укажите здесь, на каких внешних портах вашего компьютера запускать какие приложение. Формат - строго числовой. Как можно понять по названиям, запускает приложение на двух портах
 
    {SERVICE_NAME}_DB_NAME=sugar_db
    {SERVICE_NAME}_DB_PORT=5432
    {SERVICE_NAME}_DB_USER=admin
    {SERVICE_NAME}_DB_PASS=TESTPASS888
 Здесь указываются настройки для базы данных отдельных сервисов (в {SERVICE_NAME} в файле .env.sample имя конкретного сервиса в верхнем регистре. После запуска ./build автоматически будет создана база данных с указанным именем на указанном порте с указанным пользователем, имеющий все привелегии
 
     DB_HOST=pg_db
 Поле сделано для Backend CI. Оставьте по умолчанию
 
    DJANGO_SECRETKEY=foobar
    DJANGO_DEBUG=1
  Здесь укажите настройки DJANGO. DJANGO_SECRETKEY отвечает за заполнение SECRET_KEY в backend/djangoProject/settings.py. Сделайте его наиболее сложным, чтобы защитить свое приложение. DJANGO_DEBUG, если значение установлено 1, включит режим DEBUG у DJANGO. Если вы планируете его держать в публичном доступе, лучше установить 0, которое отключит режим DEBUG.
 
    SMTP_HOST=smtp.yandex.ru
    SMTP_PORT=465
    SMTP_USE_SSL=1
    
    EMAIL=you_email@yandex.ru
    EMAIL_PASSWORD=you_password
  Данное приложение использует почтовый smtp сервер для аутентификации по почте. Укажите здесь актуальные данные smtp сервера. Поле SMTP_USE_SSL принимает значения 0, если шифрования нет и значение 1, если шифрование есть

## Настройка Django

После запуска контейнера миграция осуществляется, но в каком либо случае, чтобы их осуществить, используйте скрипты внутри папки backend
- Перейдите в папку backend
  ```bash
  cd backend/
  ```
- Запустите файл make_migrations
  ```bash
  ./make_migrations
  ```
Чтобы заполнить базу данных картами, запустите скрипт в card_service
  ```bash
  ./load_cards
   ```
Чтобы создать суперпользователя или осуществить любое другое действие в командной строке в контейнере backend, запустите файл
  ```bash
  ./open_bash
  ```
Все конфиги написаны с использованием стандартных команд docker-compose, поэтому вы можете осуществлять эти действия, используя их

## Документация REST API
Так как приложение микросервисное, под каждый сервис идет отдельная документация. Различные пути для backend-сервисов вы можете увидеть в nginx-конфиге. В каждом таком есть путь /documentation/, по которому можно прочитать документацию по отдельному микросервису. Учтите, что все пути указаны от корня этого сервиса!
