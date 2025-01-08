# Базовый образ
FROM python:3.12

# Рабочая директория
WORKDIR /usr/src/app

# Копирование файлов требований и установка зависимостей
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Копирование всего проекта в контейнер
COPY . .

# Открытие порта, на котором будет работать приложение
EXPOSE 8000

# Команда для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
