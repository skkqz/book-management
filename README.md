# Django Book Management

Это Django-приложение для управления библиотекой книг. Позволяет добавлять, редактировать и удалять книги, а также регистрировать пользователей.

## Подготовка к запуску API

### Клонировать репозиторий 

* Клонируйте этот репозиторий с помощью команды: `https://github.com/skkqz/book-management.git`
* Перейдите в папку с проектом
~~~
cd book-management
~~~

### Запуск контейнеров

Убедитесь, что у вас установлен Docker на вашем компьютере. Если его нет, установите Docker с официального сайта: [Docker](https://www.docker.com/get-started).

#### Сборка контейнеров:

~~~
docker-compose build
~~~

#### Запуск сервера:

~~~
docker-compose up
~~~
* Для запуска в фоновом режиме
~~~
docker-compose up -d
~~~
#### Остановка контейнеров:
~~~
docker-compose down
~~~
#### Создание суперпользователя:
~~~
docker-compose run web python manage.py createsuperuser

~~~

## Работа с API

### Получение списка книг.

#### Request
~~~
GET /api/book/all/

http://localhost:8000/api/book/all/
~~~

#### Response
~~~
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "title": "Герой нашего времени ",
        "author": "Михаил Лермонтов ",
        "year": "2023-11-25",
        "isbn": 998866773,
        "rating": 5
    },
    {
        "id": 2,
        "title": "Война и мир ",
        "author": "Лев Толстой ",
        "year": "2023-11-25",
        "isbn": 265589525,
        "rating": 5
    }
]
~~~

### Добавить книгу.

#### Request
~~~
POST /api/book/all/

http://localhost:8000/api/book/all/
~~~

#### Response
~~~
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "title": "Хмурые люди",
    "author": "Антон Павлович Чехов ",
    "year": "2023-11-25",
    "isbn": 565584555,
    "rating": 5
}
~~~

### Детальное отображение книги.

#### Request
~~~
POST /api/book/3/

http://localhost:8000/api/book/3/
~~~

#### Response
~~~
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{   
    "id": 3,
    "title": "Хмурые люди",
    "author": "Антон Павлович Чехов ",
    "year": "2023-11-25",
    "isbn": 565584555,
    "rating": 5
}
~~~

### Изменения данных книги.

#### Request
~~~
PUT /api/book/3

http://localhost:8000/api/book/3/
~~~

#### Response
~~~
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{   
    "id": 3,
    "title": "Хмурые люди",
    "author": "Антон Павлович Чехов ",
    "year": "2023-11-25",
    "isbn": 565584555,
    "rating": 4
}
~~~

### Удаление книги.

#### Request
~~~
DELETE /api/book/2

http://localhost:8000/api/book/3/
~~~

#### Response
~~~
HTTP 204 No Content
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
~~~

### Список пользователей.

#### Request
~~~
GET /api/user/all/

http://localhost:8000/api/user/all/
~~~

#### Response
~~~
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "username": "Gena",
        "email": "gena@gmail.com",
        "registration_date": "2023-11-25T09:52:55.016914Z"
    },
    {
        "id": 2,
        "username": "Dasha",
        "email": "dasha@gmail.com",
        "registration_date": "2023-11-25T09:52:55.016914Z"
    },
]
~~~

### Создание пользователей.

#### Request
~~~
POST /api/user/registration/

http://localhost:8000/api/user/registration/
~~~

#### Response
~~~
HTTP 405 Method Not Allowed
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "username": "dasha",
    "email": "dasha@gmail.com",
    "password": "password",
    "password2": "password"
}
~~~

### Участники проекта
* [skkqz](https://github.com/skkqz/)

Вы можете внести свой вклад в этот проект, создавая issues или pull requests.