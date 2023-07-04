# Study App 📚

### Веб сервис, для помощи первокурсникам, поступившим в УрФУ

### Инструкция по локальному запуску

- Склонируйте репозиторий `git clone https://github.com/mexoil1/study-backend.git`
- Перейдите в директорию с проектом, установите и активируйте виртуальное окружение
`python -m venv venv` и `source venv/bin/activate`
- Установите зависимости `pip install -r requirements.txt`
- Перейдите в директорию с файлом `manage.py`
- Выполните миграции
`python manage.py makemigrations` и `python manage.py migrate`
- Запустите проект `python manage.py runserver`

### Документация

Документация доступна по адресу `http://localhost:8000/api/docs`

### Автор

[Слукин Михаил](https://github.com/mexoil1)
