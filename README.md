# FastAPI + Docker + PostgreSQL + Redis

## Описание
Этот проект демонстрирует использование FastAPI, PostgreSQL и Redis в контейнерах Docker, а также организацию кода с использованием Poetry.

## Стек технологий
- Python + FastAPI
- PostgreSQL
- Redis
- Docker + Docker Compose
- Poetry

## Установка и запуск

1. Клонируйте репозиторий:
   ```sh
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```

2. Запустите контейнеры:
   ```sh
   docker-compose up --build
   ```

3. Приложение будет доступно по адресу:
    - API: `http://localhost:8000`
    - Документация Swagger UI: `http://localhost:8000/docs`
    - PostgreSQL: `localhost:5432`
    - Redis: `localhost:6379`

## Эндпоинты API
- `GET /` — Возвращает `{"message": "Hello World"}`.
- `GET /create_tables` — Создает таблицы в базе данных.
- `GET /create_profiles/{number}` — Добавляет N профилей в базу данных.
- `GET /heroes` — Возвращает список героев.
- `GET /get_random_profile` — Возвращает случайный профиль из базы данных.
- `GET /profiles` — Возвращает список профилей.
- `GET /profiles/{id}` — Возвращает профиль по ID (использует кэш Redis).
- `POST /profiles` — Создает профиль.
- `DELETE /profiles/{id}` — Удаляет профиль по ID.

## Работа с базой данных
Подключение к PostgreSQL в контейнере:
```sh
docker exec -it <postgres_container_name> psql -U postgres -d mydatabase
```

## Работа с Redis
Подключение к Redis:
```sh
docker exec -it <redis_container_name> redis-cli
```
Просмотр кэша:
```sh
KEYS *
```

## Разработка
1. Установите Poetry:
   ```sh
   pip install poetry
   ```
2. Установите зависимости:
   ```sh
   poetry install
   ```
3. Запустите сервер локально:
   ```sh
   poetry run uvicorn app.main:app --reload
   ```

## Развертывание
Для развертывания проекта просто используйте:
```sh
docker-compose up -d
```

## Лицензия
Этот проект распространяется под лицензией MIT.

