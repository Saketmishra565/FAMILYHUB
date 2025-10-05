# blog/urls.py (Corrected/Confirmed)

from django.urls import path
from . import views

# --- ये हिस्सा बिल्कुल सही है ---
app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog_list'), 
    path('new/', views.PostCreateView.as_view(), name='post_create'), # CREATE
    path('edit/<int:pk>/', views.PostUpdateView.as_view(), name='post_update'), # UPDATE
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='post_delete'),
]
