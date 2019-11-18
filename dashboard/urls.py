from django.urls import path

from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('list', views.list_all_data, name='list_all_data'),
    path('api/statistics', views.StatisticsAPIView, name='StatisticsAPIView'),
    path('api/dashboard', views.get_dashboard_api, name='get_dashboard_api'),
    path('api/temperature', views.AverageTemperatureAPIView, name='AverageTemperatureAPIView'),
    path('api/pressure', views.AveragePressureAPIView, name='AveragePressureAPIView'),
    path('api/co2', views.AverageCo2PressureAPIView, name='AverageCo2PressureAPIView'),
    path('api/tvoc', views.AverageTVOCAPIView, name='AverageTVOCAPIView'),
    path('api/humidity', views.AverageHumidityAPIView, name='AverageHumidityAPIView'),
]
