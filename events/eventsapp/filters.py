from django_filters import rest_framework as filters

from .models import Event, Attendee

class EventFilter(filters.FilterSet):
    owner = filters.CharFilter(field_name='owner__username')
    class Meta:
        model = Event
        fields = {
            'title': ['icontains'],
            'description': ['icontains'],
            'date': ['exact', 'lt', 'gt'],
            'location': ['icontains'],
            'organizer': ['icontains'],
        }