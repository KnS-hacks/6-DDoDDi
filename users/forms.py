from django import forms
from .models import Letter
from django.utils.translation import gettext_lazy as _

class LetterForm(forms.ModelForm):
    class Meta:
        model = Letter
        fields = ['recipient', 'title', 'comment']
        labels = {
            'recipient':_('받는이'),
            'title':_('쪽지 제목'),
            'comment':_('쪽지 내용'),
        }