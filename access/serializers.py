from rest_framework import serializers
from .models import QR, AccessLog

class QRSerializer(serializers.ModelSerializer):
    class Meta:
        model = QR
        fields = '__all__'

class AccessLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessLog
        fields = '__all__'
