from django.db import models

class User(models.Model):
    nickname = models.CharField(max_length=100, blank=True)
    school = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=100, blank=True)
    mbti = models.CharField(max_length=100, blank=True)
    number = models.CharField(max_length=100, blank=True)
    check = models.BooleanField(default=False)
