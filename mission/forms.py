from django import forms
from django.db.models import fields
from .models import *

#class MissionForm(forms.Form):
    #profile = forms.ImageField()
    #user = forms.CharField(max_length=100)
    #title = forms.CharField(max_length=100, blank=True)
    #question = forms.TextField()
    #answer = forms.CharField(max_length=100, blank=True)
    #mission_check = forms.BooleanField(default=False)
    #pair =  forms.CharField(max_length=100, blank=True)


class AddMissionForm(forms.Form):
    title = forms.CharField(max_length=100)
    question = forms.CharField(widget=forms.Textarea)
    answer = forms.CharField(max_length=100)
