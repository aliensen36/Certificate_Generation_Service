# Сервис генерации сертификатов

С помощью этого API можно генерировать сертификаты о прохождении курсов (стажировок) для участников.

## Использованные технологии

- Django REST Framework
- PostgreSQL
- Git

## Установка и настройка

### Клонирование репозитория

Для начала клонируйте репозиторий на свою локальную машину:

```bash
git clone https://github.com/aliensen36/Certificate_Generation_Service.git
```

### Docker desktop

Скачать и установить:
[https://www.docker.com/products/docker-desktop/](URL)

Перезагрузить компьютер.
Запустить Docker desktop. При первом запуске потребуется выполнить некоторые настройки.

### Виртуальное окружение
Создать:
```bash
python -m venv venv
```  
Активировать:
```bash
venv\Scripts\activate
```

В итоге в терминале появится префикс `(venv)`, например:
`(venv) PS C:\Users\user\PycharmProjects\CGS>`

### Создать миграции
```bash
python manage.py makemigrations
```
Миграции применятся при пересборке контейнеров.

### Создание и запуск контейнеров
```bash
docker-compose up
```

### Пересборка и запуск контейнеров (при изменении кода)
```bash
docker-compose up --build
```

### Остановка и удаление контейнеров
```bash
docker-compose down
```

### Зависимости

Зависимости установит докер после запуска контейнеров.

При изменении зависимостей фиксировать их в файл:
```bash
pip freeze > requirements.txt
```
В корень проекта добавить файл .env со своими данными на основе файла .env.example.


### Создать суперпользователя
```bash
docker-compose exec web python manage.py createsuperuser
```

### Загрузить данные в БД из файла data.json
```bash
docker-compose exec web python manage.py loaddata /usr/src/app/CGS/data/data.json
```

### Запуск сервера
Докер запускает сервер.
API доступны по адресу: http://127.0.0.1:8000/api/.

### Административная панель
http://127.0.0.1:8000/admin/.
Вход с логином и паролем суперпользователя.


## Структура проекта
1.	models.py — модели для владельцев сертификатов, ролей, категорий навыков и сертификатов.
2.	serializers.py — сериализаторы для каждой модели.
3.	views.py — представления для работы с API.
4.	urls.py — маршруты для API.
5.	settings.py — настройки проекта Django.
6.	data.json – фикстуры для заполнения БД.



## Эндпойнты API

Владелец сертификата
GET /api/owners/ — Список владельцев
POST /api/owners/ — Создание нового владельца
GET /api/owners/{id}/ — Получение информации о владельце
PUT /api/owners/{id}/ — Обновление информации о владельце
DELETE /api/owners/{id}/ — Удаление владельца

Роли
GET /api/roles/ — Список ролей.
POST /api/roles/ — Создание новой роли.
GET /api/roles/{id}/ — Получение информации о роли.
PUT /api/roles/{id}/ — Обновление информации о роли.
DELETE /api/roles/{id}/ — Удаление роли.

Категории навыков
GET /api/skill-categories/ — Список категорий навыков.
POST /api/skill-categories/ — Создание новой категории.
GET /api/skill-categories/{id}/ — Получение информации о категории.
PUT /api/skill-categories/{id}/ — Обновление информации о категории.
DELETE /api/skill-categories/{id}/ — Удаление категории.

Навыки
GET /api/skills/ — Список навыков.
POST /api/skills/ — Создание нового навыка.
GET /api/skills/{id}/ — Получение информации о навыке.
PUT /api/skills/{id}/ — Обновление информации о навыке.
DELETE /api/skills/{id}/ — Удаление навыка.

Сертификаты
GET /api/certificates/ — Список сертификатов.
POST /api/certificates/ — Создание нового сертификата.
GET /api/certificates/{id}/ — Получение информации о сертификате.
PUT /api/certificates/{id}/ — Обновление информации о сертификате.
DELETE /api/certificates/{id}/ — Удаление сертификата.



# Документация

Для более подробной документации и взаимодействия с API используйте OpenAPI:
Swagger UI http://127.0.0.1:8000/api/docs/swagger/
ReDoc UI http://127.0.0.1:8000/api/docs/redoc/
JSON схема http://127.0.0.1:8000/api/schema/

## Лицензия
Этот проект распространяется под лицензией MIT. Для подробной информации см. файл LICENSE.


