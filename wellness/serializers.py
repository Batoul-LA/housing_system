from rest_framework import serializers
from .models import WellnessCheck

class WellnessCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = WellnessCheck
        fields = '__all__'
