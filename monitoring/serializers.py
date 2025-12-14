from rest_framework import serializers
from .models import Camera, CameraRecord

class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = '__all__'

class CameraRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CameraRecord
        fields = '__all__'
