Django Rest Framework based API for events management.

## Installation
1. Install Python 3.11
2. Install and start Redis server on default port 6379, or change the `CELERY_BROKER_URL` in `events/settings.py` to point to your Redis server. (Celery is used for sending email notifications asynchronously.)
3. Add your email settings to environment variables or modify settings in `eventsapp/emails.py` to use your email server for sending email notifications.
4. Install requirements
```bash
pip install -r requirements.txt
```
5. Run migrations
```bash
python manage.py migrate
```
6. Create superuser
```bash
python manage.py createsuperuser
```
7. Run server
```bash
python manage.py runserver
```
8. Open the browser and go to `http://localhost:8000/api/v1/swagger/` to see the API documentation.

This project uses SQLite as the database. You can change it to any other database by modifying the `DATABASES` setting in `events/settings.py`.