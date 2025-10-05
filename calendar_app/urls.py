# calendar_app/urls.py (Correct)

from django.urls import path
from . import views

app_name = 'calendar_app'

urlpatterns = [
    path('', views.EventListView.as_view(), name='calendar_list'), # List View
    path('new/', views.EventCreateView.as_view(), name='event_create'), # Create View
    path('edit/<int:pk>/', views.EventUpdateView.as_view(), name='event_update'), # Update View
    path('delete/<int:pk>/', views.EventDeleteView.as_view(), name='event_delete'), # Delete View
]