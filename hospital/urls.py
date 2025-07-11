# hospital/urls.py
from django.urls import path
from . import views
from .views import hospital_list

urlpatterns = [
        path('list/', views.hospital_list, name='hospital_list'),  # ✅ 이 줄이 반드시 필요!
    # 임시 작성
    path('hospital_search/', views.hospital_search, name='hospital_search'),
    path('hospital_detail/<int:hospital_id>/', views.hospital_detail, name='hospital_detail'),
    path('hospital_reviews/<int:hospital_id>/', views.hospital_reviews, name='hospital_reviews'),
    path('hospital_reviews/<int:hospital_id>/review_search/', views.review_search, name='review_search'),
    path('hospital_reserve_search/', views.hospital_reserve_search, name='hospital_reserve_search'),
    path('my_reviews/', views.my_reviews, name='my_reviews'),
    path('my_page/', views.my_page, name='my_page'),
]
