from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('mypage/scraps/', views.my_scrap_post, name='my_scraps'),
    path('select_user/', views.user_selection, name='user_selection'),
    path('login_as/<str:user_type>/', views.login_as_user, name='login_as_user'),
    path('logout/', views.user_logout, name='logout'),
]