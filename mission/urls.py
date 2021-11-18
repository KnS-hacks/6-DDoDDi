from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'mission'
urlpatterns = [
    path('mission_list/', mList_view, name="mission_list"),
    path('add_mission/', add_mission_view, name='add_mission'),
    path('perform_mission/', perform_mission_view, name='perform_mission'),
]