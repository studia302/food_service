# food_service

## Установка и запуск


**Требования:**
- Python 3.9+
- pip

**Команды:**

```bash
# 1. Клонируйте репозиторий
git clone https://github.com/studia302/food_service
cd food_service

# 2. Создайте и активируйте виртуальное окружение
python -m venv .venv

# Для Windows
.venv\Scripts\activate
# Для macOS/Linux
source .venv/bin/activate

# 3. Установите зависимости
pip install -r requirements.txt

# 4. Примените миграции базы данных
python manage.py migrate

# 5. Загружаем тестовые данные
python manage.py load_test_data

# 6. Создайте суперпользователя для доступа в админку
python manage.py createsuperuser

# 7. Запустите сервер разработки
python manage.py runserver
```

Проект будет доступен по адресу: `http://127.0.0.1:8000/`

Админ-панель: `http://127.0.0.1:8000/admin/`

Swagger: `http://127.0.0.1:8000/api/docs/`

Redoc:  `http://127.0.0.1:8000/api/redoc/`

---
