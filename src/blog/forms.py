from .models import Gets
from django import forms


class GetsViewForm(forms.ModelForm):
    class Meta:
        model = Gets
        fields = '__all__'
