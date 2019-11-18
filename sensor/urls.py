from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
     path('sensor/retrieve', views.retrieve_page, name='retrieve_page'),
     path('api/sensor', views.InstrumentRetrieveAPI.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
