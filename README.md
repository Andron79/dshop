## Описание проекта.

Интернет магазин гаджетов.
*  В проекте используются 4 приложения:
```bash
  * dshop - сам магазин, с категориями и товарами.  
  * cart - корзина для покупок и оформление заказа.
  * orders - оформление заказов, запись их в БД, отображение в админке.
  * accounts - регистрация и авторизация пользователе(вход по email)
 ``` 
  
#### Использовалось в проекте:
```bash
  * Frontend - Bootstrap 4
  * Backend - Django 2.2.13
  ```  
#### Документация по проекту.

Для запуска проекта необходимо:

* Установить зависимости:
```bash
pip install -r requirements.txt
```

Выполнить следующие команды:

* Команда для создания миграций приложения для базы данных
```bash
python manage.py migrate
```

* Команда для запуска приложения:
```bash
python manage.py runserver
```

* При создании моделей или их изменении необходимо выполнить следующие команды:
```bash
python manage.py makemigrations
python manage.py migrate
```
* Дамп данных с тестовым наполнением:
```bash
fixtures.json
```


* Мой Telegram:
```bash 
@Andron79
```
