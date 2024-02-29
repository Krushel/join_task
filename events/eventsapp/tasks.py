from celery import shared_task
from .emails import send_event_email

# It looks a little bit odd, but it`s a good practice to keep the tasks in a separate file.
@shared_task
def send_event_email_task(title, email, date, location):
    send_event_email(title, email, date, location)
