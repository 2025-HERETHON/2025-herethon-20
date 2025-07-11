from django.urls import path
from . import views
from .views import toggle_review_like

app_name = 'review'

urlpatterns = [

    path('create/<int:hospital_id>/', views.create_review, name='create_review'),
    path('search/', views.search_reviews, name='search_reviews'),
    path('like/<int:review_id>/', toggle_review_like, name='toggle_review_like'),   
    path('my_reviews/', views.my_reviews, name='my_reviews'),
    path('edit/<int:review_id>/', views.edit_review, name='edit_review'),
    path('delete/<int:review_id>/', views.delete_review, name='delete_review'),
    path('hospital/<int:hospital_id>/', views.hospital_reviews, name='hospital_reviews'),
    ]