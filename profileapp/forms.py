from django import forms
from .models import promodel


class proForm(forms.ModelForm):
    class Meta:
        model = promodel
        fields = '__all__'