from django import forms
from .models import *

class BoardForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)

class CommentForm(forms.Form):
    cotent = forms.CharField(widget=forms.Textarea)