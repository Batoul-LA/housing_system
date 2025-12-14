from django import forms
from .models import AccessLog

class AccessLogForm(forms.ModelForm):
    class Meta:
        model = AccessLog
        fields = ['qr', 'employee', 'status']
