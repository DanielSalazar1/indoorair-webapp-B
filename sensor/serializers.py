from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from foundation.models import Instrument, Sensor, TimeSeriesDatum

class SensorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(validators=[
        UniqueValidator(queryset=Sensor.objects.all()))

        def get(self, validated_data):
            name = validated_data.get('name')
            memory = TimeSeriesDatum.objects.create(id=id)

            return memory
