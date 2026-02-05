pharmacy-rest-api
REST API для аптеки на FastAPI + PostgreSQL + Docker


Pharmacy REST API

Учебный REST API для управления лекарствами в аптеке.

Проект реализован на Python с использованием FastAPI и PostgreSQL.  
Для запуска используется Docker Compose.

Стек технологий
- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker / Docker Compose
- Swagger (OpenAPI)

Функциональность
Реализован полный CRUD для лекарств:
- получение списка лекарств
- получение лекарства по id
- добавление нового лекарства
- обновление лекарства (PUT, PATCH)
- удаление лекарства

Запуск проекта

В корне проекта выполнить:

docker compose up --build
