from django.db import models
from django.contrib.auth.models import User
from .tasks import send_event_email_task
from datetime import datetime, timezone

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    organizer = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'event'
        verbose_name_plural = 'events'

    def __str__(self):
        return f'{self.title} on {self.date} at {self.location} by {self.organizer}'

    def save(self, *args, **kwargs):
        if self.date < datetime.now(timezone.utc):
            raise ValueError('You cannot create an event in the past')
        super(Event, self).save(*args, **kwargs)

class Attendee(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='attendees')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attends')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('event', 'owner')
        verbose_name = 'attendee'
        verbose_name_plural = 'attendees'

    def __str__(self):
        return f'{self.owner} attending {self.event.title}'

    def save(self, *args, **kwargs):
        if self.event.owner == self.owner:
            raise ValueError('You cannot attend your own event')
        if self.event.date < datetime.now(timezone.utc):
            raise ValueError('You cannot attend an event that has already happened')
        super(Attendee, self).save(*args, **kwargs)
        # Start the celery task to send the email asynchronously about the upcoming event
        send_event_email_task.delay(self.event.title, self.owner.email, self.event.date, self.event.location)

