# Тестовое задание для Bewise.ai

Этот проект представляет собой простое веб-приложение для создания и хранения вопросов для викторины. Он использует FastAPI для создания REST API и PostgreSQL для хранения данных.

## Установка и запуск

Убедитесь, что у вас установлены Docker и docker-compose.

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/MikhalchenkoD/Bewise.ai.git
    cd Bewise.ai
    ```

2. Сборка и запуск контейнеров с приложением и базой данных:

    ```bash
    docker-compose up --build
    ```

   Приложение будет доступно по адресу [http://localhost:8000](http://localhost:8000).

## Использование

1. **Создание вопросов**: Отправьте POST запрос на эндпоинт `/question` с параметром `questions_num`, указывающим количество вопросов для создания. Ответ:

    ```
    {
    "created_at": "2022-12-30T18:37:57.668000",
    "id": 72,
    "question_answer": "the blimp",
    "question_id": 814,
    "question_text": "Goodyear's gasbag"
    }
    ```

2. **Получение вопросов**: Чтобы получить все сохраненные вопросы, отправьте GET запрос на `/question/all`. Ответ:

    ```
    [
        {
            "created_at": "2022-12-30T21:54:13.899000",
            "id": 1,
            "question_answer": "<i>The Far Side</i>",
            "question_id": 206658,
            "question_text": "In this comic, Gary Larson had a fish named Carl \"embedded in Styrofoam shoes\", sent to sleep with the humans"
        },
        {
            "created_at": "2022-12-30T21:53:25.137000",
            "id": 2,
            "question_answer": "cuter & cutter",
            "question_id": 206047,
            "question_text": "More attractive & a single-masted sailing vessel"
        },
        {
            "created_at": "2022-12-30T21:05:24.393000",
            "id": 3,
            "question_answer": "memorandum",
            "question_id": 171365,
            "question_text": "Memo,a short note or reminder"
        }
    ]
    ```

## Структура проекта

- `app/`: Код приложения.
  - `app.py`: Основной файл с FastAPI приложением.
  - `Dockerfile`: Dockerfile для сборки образа приложения.
  - `requirements.txt`: Зависимости Python.
  - `models.py`: Модели SQLAlchemy для работы с базой данных PostgreSQL.
- `docker-compose.yml`: Файл для запуска и настройки Docker контейнеров.
- `README.md`: Инструкции и описание проекта.

## Авторы

Михальченко Дмитрий (https://t.me/DmitriyMikhalchenko)
