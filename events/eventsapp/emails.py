from django.core.mail import send_mail
import os

sender_email = os.environ.get('SENDER_EMAIL')
sender_email_password = os.environ.get('SENDER_EMAIL_PASSWORD')

def send_event_email(title, email, date, location):
    subject = f'Event: {title}'
    message = f'Hi, you have an event coming up on {date} at {location}.'
    send_mail(
        subject,
        message,
        sender_email,
        [email],
        fail_silently=True,
        auth_user=sender_email,
        auth_password=sender_email_password)
