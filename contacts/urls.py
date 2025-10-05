# contacts/urls.py (Correct)

from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('', views.ContactListView.as_view(), name='contacts_list'), 
    # नया कांटेक्ट जोड़ने के लिए सही URL पैटर्न:
    path('new/', views.ContactCreateView.as_view(), name='contact_create'), 
    path('edit/<int:pk>/', views.ContactUpdateView.as_view(), name='contact_update'),
    path('delete/<int:pk>/', views.ContactDeleteView.as_view(), name='contact_delete'),
]