from django import forms
from .models import WellnessCheck

class WellnessCheckForm(forms.ModelForm):
    class Meta:
        model = WellnessCheck
        fields = [
            'room',
            'employee',
            'inspection_date',
            'security_notes',
            'maintenance_notes',
            'needs_maintenance',
            'follow_up_required',
        ]

