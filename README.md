Версия агрегатора новостей, собранная в docker-compose.

Оригинальные версии:
https://github.com/AlexanderVarlamov/fast_ap_lenta
https://github.com/AlexanderVarlamov/flask_news_app

Установка:
Скачать репозиторий себе на компьютер, запустить из папки, где лежит docker-compose.yml
- docker compose up

Далее агрегатор доступен по адресу http://127.0.0.1:5111

Замечание. Поскольку на сайте news.ru для получения RSS-ленты используется JS, контейнер с сервером содержит Google Chrome и ChromeDriver. В связи с этим объём контейрнера с бэкендом получается довольно значительным (около 1Гб)