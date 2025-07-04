# hospital/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('hospital_list/', views.hospital_list, name='hospital_list'),
]
