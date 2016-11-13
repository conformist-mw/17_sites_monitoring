# Sites monitoring

Данный скрипт выводит статус каждого сайта. С сайтом всё хорошо, если:

* сервер отвечает на запрос статусом HTTP 200;
* доменное имя сайта проплачено как минимум на 1 месяц вперед.

## Запуск скрипта.

Для запуска нужно установить зависимости из файла, например так:
```
pip3 install -r requirements.txt
```
и далее:
```
python3 check_sites_health.py urls.txt
```