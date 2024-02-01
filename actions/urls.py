from django.urls import path
from . import views

app_name = 'actions'

urlpatterns = [
    path('actions/', views.actions, name='actions'),
    ]