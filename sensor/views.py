from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from rest_framework import status, views, response

from foundations.models import Instrument, TimeSeriesDatum, Sensor
from .serializers import SensorSerializer

def retrieve_page(request, id):
    return render(request, "sensor/retrieve.html", {
        "instrument_id": int(id),
    })


class InstrumentRetrieveAPI(views.APIView):
   def get(self, request):

       serializer = AddSerializer(data = request.data)
       serializer.is_valid(raise_exception=True)
       serializer.save()

       return response.Response(
        status=status.HTTP_200_OK,
        data = {
            'time series data' : serializer.data,
        }
       )


# def get_instruments_list_api(request):
#     instruments = Instrument.objects.filter(user=request.user)
#     output = []
#     for instrument in instruments.all():
#         output.append({
#             'id': instrument.id,
#             'name': instrument.name,
#         })
#     return JsonResponse({
#         'instruments': output
#     })
