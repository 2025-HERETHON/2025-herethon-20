# hospital/urls.py
from django.urls import path
from . import views
from .views import HospitalListAPIView, hospital_list

urlpatterns = [
    path('', views.hospital_list, name='hospital_list'),
    path('api/hospitals/', HospitalListAPIView.as_view(), name='hospital_list_api'),
]
