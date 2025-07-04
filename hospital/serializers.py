# hospital/serializers.py
from rest_framework import serializers
from .models import Hospital

class HospitalSerializer(serializers.ModelSerializer):
    average_rating = serializers.FloatField(read_only=True)
    cost_reasonable_count = serializers.IntegerField(read_only=True)
    teen_friendly_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Hospital
        fields = [
            'id', 'name', 'address', 'tel', 'is_female_doctor',
            'average_rating', 'cost_reasonable_count', 'teen_friendly_count'
        ]
