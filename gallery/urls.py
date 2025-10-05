# gallery/urls.py

from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.GalleryListView.as_view(), name='gallery_list'), 
    path('upload/', views.PhotoCreateView.as_view(), name='photo_upload'),
    path('delete/<int:pk>/', views.PhotoDeleteView.as_view(), name='photo_delete'),
]