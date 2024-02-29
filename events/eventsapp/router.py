from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *
from .openapi_schema_settings import schema_view

# Create a router and register viewsets
router = DefaultRouter()
router.register('events', EventViewSet, basename='events')
router.register('attendees', AttendeeViewSet, basename='attendees')
urlpatterns = router.urls

# Add the register endpoint to the list of urlpatterns
urlpatterns += [
    path('register/', UserCreate.as_view(), name='register'),
]

# Add the schema view to the list of urlpatterns
urlpatterns += [
    path('swagger<format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]