from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<slug:category_slug>/', views.post_list, name='post_list_by_category'),  # 선택한 카테고리 게시글만
]