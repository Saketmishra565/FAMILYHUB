from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin 
from .models import FamilyContact  # केवल आवश्यक मॉडल का उपयोग करें

# Contact मॉडल को हटा दिया गया है क्योंकि यह कोड में इस्तेमाल नहीं हो रहा था।
# from .models import Contact 

class ContactListView(LoginRequiredMixin, ListView):
    model = FamilyContact
    template_name = 'contacts/contact_list.html'
    context_object_name = 'contacts'

class ContactCreateView(LoginRequiredMixin, CreateView):
    model = FamilyContact
    fields = ['name', 'relation', 'phone', 'email', 'address']
    template_name = 'contacts/contact_form.html'
    # Namespacing (app_name:url_name) का उपयोग करके ठीक किया गया
    success_url = reverse_lazy('contacts:contacts_list') 

class ContactUpdateView(LoginRequiredMixin, UpdateView):
    model = FamilyContact
    fields = ['name', 'relation', 'phone', 'email', 'address']
    template_name = 'contacts/contact_form.html'
    # Namespacing का उपयोग करके ठीक किया गया
    success_url = reverse_lazy('contacts:contacts_list')

class ContactDeleteView(LoginRequiredMixin, DeleteView):
    model = FamilyContact
    template_name = 'contacts/contact_confirm_delete.html'
    # Namespacing का उपयोग करके ठीक किया गया
    success_url = reverse_lazy('contacts:contacts_list')