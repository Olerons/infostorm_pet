from app import app, db
from app.models import User, Post


@app.shell_context_processors
def make_shell_context():
    return {'db' : db, 'User' : User, 'Post' : Post}

# https://habr.com/ru/articles/346344/

# Определение переменной среды, где расположено приложение, в терминале
# set FLASK_APP=main.py

# Запуск:
# flask run

# создание репозитария миграций БД
# flask db init

# миграция бд
# flask db migrate


