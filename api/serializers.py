# from rest_framework import serializers
# from rest_framework.validators import UniqueValidator
#
# from foundations.models import Instrument, Sensor, TimeSeriesDatum
#
#
# class InstrumentSerializer(serializers.Serializer):



# class ArchivedWebpageSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     url = serializers.URLField(
#         validators=[
#             UniqueValidator(queryset=ArchivedWebpage.objects.all())
#         ]
#
#     )
#
#     def create(self, validated_data):
#         # """
#         # Create and return a new `Snippet` instance, given the validated data.
#         # """
#         url = validated_data.get('url', None)
#         archived_webpage = ArchivedWebpage.objects.create(url=url)
#
#
#         return archived_webpage
