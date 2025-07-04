from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('mypage/', views.my_page, name='my_page'),

    path('mypage/scraps/', views.my_scrap_post, name='my_scraps'),
    path('mypage/notifications/', views.notification_settings, name='notification_settings'),
    path('mypage/customer_service/', views.customer_service, name='customer_service'),
    path('mypage/user_guide/', views.user_guide, name='user_guide'),
    path('select_user/', views.user_selection, name='user_selection'),
    path('login_as/<str:user_type>/', views.login_as_user, name='login_as_user'),
    path('logout/', views.user_logout, name='logout'),
]