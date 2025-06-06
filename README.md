# Elektro

Проєкт **Elektro** — це веб-додаток для управління показниками двофазних лічильників, розрахунку рахунків за електроенергію та перегляду тарифів.

## Функціональність

- **Подання показників**: Користувач може подати показники для двофазного лічильника (день/ніч).
- **Розрахунок рахунків**: Автоматичний розрахунок вартості електроенергії на основі тарифів.
- **Перегляд рахунків**: Сторінка з таблицею, яка відображає всі рахунки.
- **Перегляд лічильників**: Сторінка з таблицею, яка відображає всі лічильники, їх поточні показники та загальну суму до сплати.
- **Управління тарифами**: Можливість перегляду та зміни тарифів.

## Структура проєкту
```bash
elektro/
├── db.sqlite3                # База даних SQLite
├── manage.py                 # Django management script
├── elektro/                  # Головна конфігурація Django
│   ├── __init__.py           # Ініціалізація пакета
│   ├── asgi.py               # ASGI конфігурація
│   ├── settings.py           # Налаштування проєкту
│   ├── urls.py               # Головні маршрути
│   ├── wsgi.py               # WSGI конфігурація
├── main/                     # Головний додаток
│   ├── __init__.py           # Ініціалізація пакета
│   ├── admin.py              # Реєстрація моделей в адмінпанелі
│   ├── apps.py               # Конфігурація додатка
│   ├── forms.py              # Форми
│   ├── models.py             # Моделі бази даних
│   ├── tests.py              # Тести
│   ├── views.py              # Представлення
│   ├── migrations/           # Міграції бази даних
│   │   ├── __init__.py       # Ініціалізація пакета
│   └── templates/            # Шаблони HTML
│       ├── main/
│           ├── index.html    # Головна сторінка
│           ├── bills.html    # Сторінка рахунків
│           ├── meters.html   # Сторінка лічильників
│           ├── tariffs.html  # Сторінка тарифів
│           └── success.html  # Сторінка успіху
│   └── static/               # Статичні файли
│       ├── css/              # CSS стилі
│       ├── js/               # JavaScript файли
│       └── images/           # Зображення
└── requirements.txt          # Залежності проєкту
```


## Встановлення

1. **Клонування репозиторія**:
   ```bash
   git clone <URL_репозиторія>
   cd elektro
   ```

2. **Створення та активація віртуального середовища**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Для Linux/MacOS
    venv\Scripts\activate     # Для Windows
    ```

3. **Встановлення залежностей**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Міграція бази даних**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Запуск сервера**:
    ```bash
    python manage.py runserver
    ```

6. **Відкрийте у браузері: Перейдіть за адресою http://localhost:8000/**.

## Використання

**Головна сторінка**: Подання показників лічильника.

**Сторінка рахунків**: Перегляд усіх рахунків (http://127.0.0.1:8000/bills/).

**Сторінка лічильників**: Перегляд усіх лічильників (http://127.0.0.1:8000/meters/).

**Сторінка тарифів**: Перегляд та зміна тарифів (http://127.0.0.1:8000/tariffs/).

## Тестування
Для запуску тестів виконайте:
```bash
python manage.py test
```

## Автор
**Розроблено Буряківською Анастасією.**