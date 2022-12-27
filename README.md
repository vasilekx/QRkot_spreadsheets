# Проект QRKot на FastAPI


## Описание
Приложение благотворительного фонда поддержки котиков QRKot собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.

## Применяемые технологи

[![Python](https://img.shields.io/badge/Python-3.7-blue?style=flat-square&logo=Python&logoColor=3776AB&labelColor=d0d0d0)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.78.0-blue?style=flat-square&logo=FastAPI&logoColor=3776AB&labelColor=d0d0d0)](https://fastapi.tiangolo.com)

[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1.4.36-blue?style=flat-square&logoColor=3776AB&labelColor=d0d0d0)](https://www.sqlalchemy.org/docs/)
[![FastAPI Users](https://img.shields.io/badge/FastAPI_Users-10.0.4-blue?style=flat-square&logoColor=3776AB&labelColor=d0d0d0)](https://fastapi-users.github.io/fastapi-users/)
[![Pydantic](https://img.shields.io/badge/Pydantic-1.9.1-blue?style=flat-square&logoColor=3776AB&labelColor=d0d0d0)](https://pydantic-docs.helpmanual.io)
[![Alembic](https://img.shields.io/badge/Alembic-1.7.7-blue?style=flat-square&logoColor=3776AB&labelColor=d0d0d0)](https://alembic.sqlalchemy.org/)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-0.17.6-blue?style=flat-square&logoColor=3776AB&labelColor=d0d0d0)](https://www.uvicorn.org)
[![Google API Client](https://img.shields.io/badge/Google_API-2.0-blue?style=flat-square&logoColor=3776AB&labelColor=d0d0d0)](https://github.com/googleapis/google-api-python-client/)

---

## Запуск сервиса

Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone git@github.com:vasilekx/cat_charity_fund.git
```

```bash
cd cat_charity_fund
```

Создать файл .env

* Если у вас Linux/MacOS
    ```bash
    touch .env
    ```

* Если у вас Windows

    ```bash
    type nul > .env
    ```

Заполнить файл .env:

```
APP_TITLE=Пожертвование в благотворительный фонд поддержки котиков QRKot
DESCRIPTION=Пожертвования на цели связанные с поддержкой кошачьей популяции.
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET=your_secret
FIRST_SUPERUSER_EMAIL=admin@test.com
FIRST_SUPERUSER_PASSWORD=your_password
# Переменные Google API
DATABASE_URL=
FIRST_SUPERUSER_EMAIL=
FIRST_SUPERUSER_PASSWORD=
TYPE=
PROJECT_ID=
PRIVATE_KEY_ID=
PRIVATE_KEY=
CLIENT_EMAIL=
CLIENT_ID=
AUTH_URI=
TOKEN_URI=
AUTH_PROVIDER_X509_CERT_URL=
CLIENT_X509_CERT_URL=
EMAIL=
```

Создать и активировать виртуальное окружение:

```bash
python3 -m venv venv
```

* Если у вас Linux/MacOS

    ```bash
    source venv/bin/activate
    ```

* Если у вас windows

    ```bash
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```bash
python3 -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

Создать базу данных:
```bash
alembic upgrade head
```

Выполнить запуск сервиса:

```bash
uvicorn app.main:app --reload
```

---

## Доступ к спецификаций API сервиса
```http
http://127.0.0.1:5000/docs
```

### Примеры запросов к API

---

#### Создание пожертвования:
###### Доступно только авторизированным пользователям

**POST**-запрос:

```http
http://127.0.0.1:8000/donation/
```

Тело запроса:

```json
{
  "full_amount": 500,
  "comment": "Всем добра!",
  "id": 22,
  "create_date": "2022-12-05T20:56:48.224985"
}
```

Ответ:

```json
{
    "short_link": "http://127.0.0.1:5000/myshorturl",
    "url": "https://flask.palletsprojects.com/en/latest/"
}
```

---

#### Получение списка всех проектов:
###### Доступно всем

**GET**-запрос:

```http
http://127.0.0.1:8000/charity_project/
```

Ответ:

```json
[
  {
    "name": "pro01",
    "description": "desc01",
    "full_amount": 1000,
    "id": 1,
    "create_date": "2022-12-04T01:37:22.647044",
    "invested_amount": 1000,
    "fully_invested": true,
    "close_date": "2022-12-05T15:22:01.916035"
  },
  {
    "name": "pro02",
    "description": "desc02",
    "full_amount": 2050,
    "id": 2,
    "create_date": "2022-12-05T15:26:08.314071",
    "invested_amount": 2050,
    "fully_invested": true,
    "close_date": "2022-12-05T15:26:08.323403"
  }
]
```

---

#### Получение списка всех пожертвований:
###### Доступно только для суперюзеров

**GET**-запрос:

```http
http://127.0.0.1:8000/donation/
```

Ответ:

```json
[
  {
    "full_amount": 700,
    "comment": "comment 7",
    "id": 7,
    "create_date": "2022-12-05T12:20:14.075869",
    "invested_amount": 700,
    "fully_invested": true,
    "close_date": "2022-12-05T15:26:08.323364",
    "user_id": 2
  },
  {
    "full_amount": 800,
    "comment": "comment 8",
    "id": 8,
    "create_date": "2022-12-05T13:19:12.176741",
    "invested_amount": 450,
    "fully_invested": false,
    "user_id": 2
  },
  {
    "full_amount": 900,
    "comment": "comment 9",
    "id": 9,
    "create_date": "2022-12-05T13:21:13.708572",
    "invested_amount": 0,
    "fully_invested": false,
    "user_id": 2
  }
]
```

---

## Автор проекта
[Владислав Василенко](https://github.com/vasilekx)
