from django.db import models

class User(models.Model):
    nickname = models.CharField(max_length=100, blank=True, unique=True)
    school = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=100, blank=True)
    mbti = models.CharField(max_length=100, blank=True)
    number = models.CharField(max_length=100, blank=True)
    matching_check = models.BooleanField(default=False)
    pair = models.CharField(max_length=100, blank=True)
    balance_game = models.BooleanField(default=False)
    stamp = models.IntegerField(default=0)

    def __str__(self):
        return self.nickname


class Letterbox(models.Model):
    box_name = models.CharField(max_length=200, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.box_name


class Letter(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    # letter_box = models.ForeignKey(Letterbox, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=200, blank=True)
    comment = models.TextField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
