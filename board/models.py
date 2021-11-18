from django.db import models
from users.models import *

# Create your models here.

class Board(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title    

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    uauthor= models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    cotent = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
