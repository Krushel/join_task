from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import EventSerializer, AttendeeSerializer, UserCreateSerializer
from .models import Event, Attendee
from .permissions import IsOwnerOrReadOnly
from .filters import EventFilter
from django.contrib.auth.models import User

class UserCreate(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EventFilter
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class AttendeeViewSet(viewsets.ModelViewSet):
    queryset = Attendee.objects.all()
    serializer_class = AttendeeSerializer
    permission_classes = [IsOwnerOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

