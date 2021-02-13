from django import forms
from django.forms import ModelForm

from.models import *

class todoForm(forms.ModelForm):
    class Meta:
        model = todoItem
        fields = '__all__'