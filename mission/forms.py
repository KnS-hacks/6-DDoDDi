from django import forms
from django.db.models import fields
from .models import *

class MissionForm(forms.ModelForm):
    #profile = forms.ImageField()
    #user = forms.CharField(max_length=100, blank=True)
    #title = forms.CharField(max_length=100, blank=True)
    #question = forms.TextField()
    #answer = forms.CharField(max_length=100, blank=True)
    #mission_check = forms.BooleanField(default=False)
    #pair =  forms.CharField(max_length=100, blank=True)

    class Meta:
        model = Mission
        fields = ['user_nickname', 'user_pair', 'title', 'question', 'answer', 'mission_check']


class AddMissionForm(forms.Form):
    title = forms.CharField(max_length=100, blank=True)
    question = forms.TextField()
    answer = forms.CharField(max_length=100, blank=True)
