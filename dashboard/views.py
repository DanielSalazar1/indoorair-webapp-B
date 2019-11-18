from django.shortcuts import render
from django.http import JsonResponse
from foundations.models import TimeSeriesDatum
import statistics

from rest_framework import status, response, views

def dashboard(request):
    user = request.user
    print("THE USER IS", user)

    if user.is_authenticated == False:
        return HttpResponse("Cannot view page - you must log in first!")

    context = {
        'user': user,
    }

    return render(request, "dashboard/dashboard.html", context)

# List all instruments we have

def list_all_data(request):
    result = ""
    data = TimeSeriesDatum.objects.all().order_by('id')
    for datum in data:
        result += str(datum.id) + ", "

    return HttpResponse(result)

class StatisticsAPIView(views.APIView):
    def get(self, request):

        try:
            values = CalculatorMemory.objects.all().values_list('value', flat=True)

            return response.Response(
                status=status.HTTP_200_OK,
                data={
                    'values': values,
                    'mean' : statistics.mean(values),
                    'median' : statistics.median(values),
                    'mode' : statistics.mode(values),

                }
            )
        except Exception as e:

            return response.Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    'message': 'Server couldnt complete your request',
                }
            )

def get_dashboard_api(request):
    return JsonResponse({
    "average_temperature": get_average_temperature(),
    "average_pressure": get_average_pressure(),
    "average_co2": get_average_co2(),
    "average_tvoc": get_average_tvoc(),
    "average_humidity": get_average_humidity(),
    })


class AverageTemperatureAPIView(views.APIView):
    def get(self, request):
         items = TimeSeriesDatum.objects.filter(sensor__name = "Temperature").values('value')
         length = CalculatorMemory.objects.count("Temperature")

         sum = 0

         for item in items:
             value = item['value']
             sum = sum + value

             average = sum/length

             return response.Response(
                 status=status.HTTP_200_OK,
                 data={
                     'average temperature': str(average), # str(average) to casting as a string value.
                 }
             )

class AveragePressureAPIView(views.APIView):
    def get(self, request):
         items = TimeSeriesDatum.objects.filter(sensor__name = "Pressure").values('value')
         length = CalculatorMemory.objects.count("Pressure")

         sum = 0

         for item in items:
             value = item['value']
             sum = sum + value

             average = sum/length

             return response.Response(
                 status=status.HTTP_200_OK,
                 data={
                     'average pressure': str(average), # str(average) to casting as a string value.
                 }
             )

class AverageCo2PressureAPIView(views.APIView):
    def get(self, request):
         items = TimeSeriesDatum.objects.filter(sensor__name = "co2").values('value')
         length = CalculatorMemory.objects.count("co2")

         sum = 0

         for item in items:
             value = item['value']
             sum = sum + value

             average = sum/length

             return response.Response(
                 status=status.HTTP_200_OK,
                 data={
                     'average co2': str(average), # str(average) to casting as a string value.
                 }
             )

class AverageTVOCAPIView(views.APIView):
    def get(self, request):
         items = TimeSeriesDatum.objects.filter(sensor__name = "tvoc").values('value')
         length = CalculatorMemory.objects.count("tvoc")

         sum = 0

         for item in items:
             value = item['value']
             sum = sum + value

             average = sum/length

             return response.Response(
                 status=status.HTTP_200_OK,
                 data={
                     'average tvoc': str(average), # str(average) to casting as a string value.
                 }
             )

class AverageHumidityAPIView(views.APIView):
    def get(self, request):
         items = TimeSeriesDatum.objects.filter(sensor__name = "Humidity").values('value')
         length = CalculatorMemory.objects.count("Humidity")

         sum = 0

         for item in items:
             value = item['value']
             sum = sum + value

             average = sum/length

             return response.Response(
                 status=status.HTTP_200_OK,
                 data={
                     'average humidity': str(average), # str(average) to casting as a string value.
                 }
             )
