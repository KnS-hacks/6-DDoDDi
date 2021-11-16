from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *

app_name = 'main'
urlpatterns = [
    path('', views.home, name='home'),
]