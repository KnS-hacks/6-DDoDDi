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
    path('letter/detail/<int:id>', views.letter_detail, name='letter-detail'),
    path('mentor/detail', views.mentor_detail, name='mentor-detail'),
    path('balance/', views.balance, name='balance')
]