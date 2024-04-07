"""Defines URL patterns for users."""

from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    # Include defualt URL for identity validation
    path('', include('django.contrib.auth.urls')),
    # Registeration Page
    path('register/', views.register, name='register'),
]