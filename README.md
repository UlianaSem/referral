# Referral project

## Описание проекта
Реализация простой реферальной системы

## Технологии

- Linux
- Python
- Poetry
- Django
- DRF
- PostgreSQL
- Docker
- Docker Compose

## Зависимости

Зависимости, необходимые для работы проекта, указаны в файле pyproject.toml.
Чтобы установить зависимости, используйте команду `poetry install`

## Эндпоинты

1. Эндпойнт получения кода верификации `api/get_code/`
2. Эндпойнт подтверждения кода верификации `api/verify_code/`
3. Эндпойнт просмотрас своего профиля `api/profile/<int:pk>/`
4. Эндпойнт добавления инвайт-кода `api/add_invite_code/<int:pk>/`

## Документация

Документация находится по ссылке:
1. Redoc `api/schema/redoc/`

## Как запустить проект

Для запуска проекта необходимо выполнить следующие шаги:
1. При необходимости установите Docker и Docker Compose на компьютер с помощью инструкции https://docs.docker.com/engine/install/
2. Cклонируйте репозиторий себе на компьютер
3. Создайте файл .env и заполните его, используя образец из файла .env.example
4. Соберите образ с помощью команды `docker-compose build`
5. Запустите контейнеры с помощью команды `docker-compose up`

## Файл .env.example
1. `DATABASES_NAME, DATABASES_USER, DATABASES_PASSWORD, DATABASES_HOST` - данные для подключения к БД
2. `SECRET_KEY, DEBUG, ALLOWED_HOSTS`

## Авторы

UlianaSem

## Связь с авторами

https://github.com/UlianaSem/