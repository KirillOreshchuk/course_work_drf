Курсовая работа: DRF

1. Создать файл '.env', добавить в него:
   DEBUG= #True/False
   SECRET_KEY= #SECRET_KEY
   DB_USER= # Пользователь базы данных
   DB_PASSWORD= #Пароль базы данных
   DB_NAME= #Название базы данных
   DB_ENGINE= # Подключение к базе данных
   CELERY_BROKER_URL= #Брокер celery
   CELERY_RESULT_BACKEND=#URL бэкенда celery
   CELERY_TASK_TRACK_STARTED= #Флаг отслеживания выполнения задач
   TG_BOT_API= #Токен бота telegram 
   CHAT_ID_TG= #id пользователя Telegram

2. Применить миграции командой: python3 manage.py migrate

3. Запустить файл users/management/commands/csu.py командой: python manage.py csu - создать суперпользователя 

4. В админке или через Postman создать примеры привычек

5. Запустить сервер: python3 manage.py runserver

6. Для запуска периодичесой задачи запустить команды:
   celery -A config worker -l info
   celery -A config beat -l info -S django
