from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.home, name='home'),
    path('mypage/', views.mypage, name='mypage'),
    path('letter/', views.letter_list, name='letter-list'),
    path('letter/create', views.letter_create, name='letter-create'),
    path('matching/', views.matching, name='matching'),
]