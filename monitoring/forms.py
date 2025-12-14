from django import forms
from .models import Camera
from .models import CameraRecord

class CameraForm(forms.ModelForm):
    class Meta:
        model = Camera
        fields = ['location']
class CameraRecordForm(forms.ModelForm):
    class Meta:
        model = CameraRecord
        fields = ['camera', 'start_time', 'end_time', 'description', 'video']
