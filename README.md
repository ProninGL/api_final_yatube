# Api YaTube
## Описание ***API*** 


Документация к API доступна по адресу [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

**API** позволяет:

- Обрабатывать GET, POST, PATCH, PUT и DELETE запросы к  публикациям и коментариям.<br>
- Получать списки сообществ, и подписок.<br>
- Работа с токенами JWT, получить, обновить, проверить.



### Потребуется:

[![Python](https://img.shields.io/badge/-Python_3.7.12-464646??style=flat-square&logo=Python)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/-Django-464646??style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django](https://img.shields.io/badge/-Django_rest_framework_3.12.4-464646??style=flat-square&logo=Django)] (https://www.django-rest-framework.org)
[![Django](https://img.shields.io/badge/-djoser_2.1.0-464646??style=flat-square&logo=Django)] (https://djoser.readthedocs.io/en/latest/getting_started.html#installation)


## Установка:

- Клонируем репозиторий на локальную машину:<br>
```
  git clone https://github.com/ProninGL/api_final_yatube
```
- Создаем виртуальное окружение:<br>
```
  python -m venv venv
```
- Активируем виртуальное окружение:<br>
```
  source venv/bin/activate
```
- Устанавливаем зависимости:<br>
```
  python3 -m pip install --upgrade pip
```<br>
```
	pip install -r requirements.txt
```
- Создание и применение миграций:<br>
```
  $ python manage.py makemigrations и $ python manage.py migrate
```
- Запускаем django сервер:<br>
```
  $ python manage.py runserver
```

Все готово к использованию проекта у себя на локальной машине.<br>
**API** будет доступен по адресу [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Пример работы:

#### Для полноценной работы необходимо получть токен:

- /api/v1/jwt/create/<br>
```
{
"username": "string",
"password": "string"
}
```

#### Для неаутентифицированных пользователей дуступно:

- /api/v1/posts/
- /api/v1/posts/{post_id}/
- /api/v1/groups/
- /api/v1/groups/{group_id}/
- /api/v1/posts/{post_id}/comments/{comment_id}/