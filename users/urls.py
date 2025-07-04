from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('mypage/scraps/', views.my_scrap_post, name='my_scraps'),
]