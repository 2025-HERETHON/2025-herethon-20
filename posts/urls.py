from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('search/', views.post_search, name='post_search'),
    path('my_questions/', views.my_questions, name='my_questions'),
    path('my_answers/', views.my_answers, name='my_answers'),
    path('<int:post_id>/toggle_scrap/', views.toggle_scrap, name='toggle_scrap'),
    path('create/', views.create_post, name='create_post'),
    path('<int:post_id>/edit/', views.edit_post, name='edit_post'),
    path('<int:post_id>/delete/', views.delete_post, name='delete_post'),

    path('<int:post_id>/', views.post_detail, name='post_detail'),  # 클릭한 글 상세페이지

    path('<int:post_id>/comments/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('', views.post_list, name='post_list'),
    path('doctor/', views.doctor_post_list, name='doctor_post_list'),
    path('<slug:category_slug>/', views.post_list, name='post_list_by_category'),  # 선택한 카테고리 게시글만 표시
]