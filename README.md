GET /api/certificates/ — список всех сертификатов.
POST /api/certificates/ — создание нового сертификата.
GET /api/certificates/<id>/ — просмотр конкретного сертификата.
PUT /api/certificates/<id>/ — обновление сертификата.
DELETE /api/certificates/<id>/ — удаление сертификата.

# Сервис генерации сертификатов

## Docker desktop
Скачать и установить:
[https://www.docker.com/products/docker-desktop/](URL)

Перезагрузить компьютер.
Запустить Docker desktop. При первом запуске потребуется выполнить некоторые настройки.

## Виртуальное окружение
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

## Создание и запуск контейнеров
```bash
docker-compose up
```

## Пересборка и запуск контейнеров (при изменении кода)
```bash
docker-compose up --build
```

## Остановка и удаление контейнеров
```bash
docker-compose down
```

## Зависимости

Зависимости установит докер после запуска контейнеров.

При изменении зависимостей фиксировать их в файл:
```bash
pip freeze > requirements.txt
```

## Создать миграции при запущенных контейнерах
```bash
docker-compose exec web python manage.py makemigrations
```

## Запустить миграции при запущенных контейнерах
```bash
docker-compose exec web python manage.py migrate
```

## Создать суперпользователя
```bash
docker-compose exec web python manage.py createsuperuser
```


## Загрузить данные в БД из файла data.json
```bash
docker-compose exec web python manage.py loaddata /usr/src/app/CGS/data/data.json
```
