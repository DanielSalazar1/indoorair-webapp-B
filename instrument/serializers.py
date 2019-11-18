from rest_framework import serializers
from foundations.models import Instrument, Sensor, TimeSeriesDatum

MEMORY_ID=1

# API endpoint where the user inputs serial number and location inside the house.

class UserCommandSerializer(serializers.Serializer):
    value = serializers.FloatField()
    location = serializers.CharField()

    def create(self, validated_data):
        try:
            instrument = Instrument.objects.get(id=MEMORY_ID)
# The staff user CREATE an instrument..
        except Instrument.DoesNotExist:
            instrument = Instrument.objects.create(
                id=MEMORY_ID,
                value=0,
                location=""
            )

        value = validated_data.get('value')
        location = validated_data.get('location')

        instrument.value = instrument.value + value
        instrument.save()

        instrumet.location = instrument.location + location
        instrument.save()

        return instrument
