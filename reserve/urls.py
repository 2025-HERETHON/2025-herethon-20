# reserve/urls.py

from django.urls import path
from . import views

app_name = 'reserve'

urlpatterns = [
    path('list/', views.recommended_doctors, name='recommended_doctors'),
]
