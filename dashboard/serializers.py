from rest_framework import serializers
from foundations.models import Instrument, Sensor, TimeSeriesDatum

MEMORY_ID = 1

class AverageSerializer(serializers.Serializer):
    value = serializers.FloatField()
    name = serializers.CharField()

    def create(self, validated_data):
        try:
            memory = 
