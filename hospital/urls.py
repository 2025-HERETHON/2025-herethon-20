# hospital/urls.py
from django.urls import path
from . import views
from .views import HospitalListAPIView, hospital_list

urlpatterns = [
    path('hospital_list/', views.hospital_list, name='hospital_list'),
    path('api/hospitals/', HospitalListAPIView.as_view(), name='hospital_list_api'),
    # 임시 작성
    path('hospital_search/', views.hospital_search, name='hospital_search'),
    path('review/create/', views.review_create, name='review_create'),]