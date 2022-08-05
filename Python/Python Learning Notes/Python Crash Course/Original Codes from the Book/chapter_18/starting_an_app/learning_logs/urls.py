from django.urls import path

from . import views

app_name = 'learning_logs'
urloatters = [
    # Homepage
    path('', views.index, name='index')
]