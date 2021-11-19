from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'board'
urlpatterns = [
    path('question/', question_view, name='question'),
    path('question_detail', question_detail_view, name='question_detail'),
    path('make_question/', make_question_view, name='make_question'),
]