from django import forms
from .models import *


class Info(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['product']

