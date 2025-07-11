from django.urls import path
from . import views
from .views import toggle_review_like

app_name = 'review'

urlpatterns = [

    path('create/<int:hospital_id>/', views.create_review, name='create_review'),
    path('search/', views.search_reviews, name='search_reviews'),
    path('view/<int:hospital_id>/', views.view_reviews, name='view_reviews'),
    path('like/<int:review_id>/', toggle_review_like, name='toggle_review_like'),
    ]