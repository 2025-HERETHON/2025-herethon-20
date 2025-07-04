from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('search/', views.post_search, name='post_search'),
    path('my_questions/', views.my_questions, name='my_questions'),
    path('<int:post_id>/scrap/', views.toggle_scrap, name='toggle_scrap'),
    path('', views.post_list, name='post_list'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),  # 클릭한 글 상세페이지
    path('<slug:category_slug>/', views.post_list, name='post_list_by_category'),  # 선택한 카테고리 게시글만 표시
]