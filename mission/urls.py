from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'mission'
urlpatterns = [
    path('mission_list/', mList_view, name='mission_list'),
    path('mission_detail/<int:id>', mission_detail, name='mission_detail'),
    path('submit_mission/<int:id>', submit_mission, name="submit_mission"),
    path('add_mission/', add_mission_view, name='add_mission'),
]