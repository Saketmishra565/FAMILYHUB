# calendar_app/views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin 
from .models import Event
from datetime import date

class EventListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'calendar_app/event_list.html'
    context_object_name = 'events'

    def get_queryset(self):
        # आज या भविष्य में होने वाले इवेंट्स
        return Event.objects.filter(date__gte=date.today()).order_by('date')

class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['title', 'date', 'description']
    template_name = 'calendar_app/event_form.html'
    success_url = reverse_lazy('calendar_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    fields = ['title', 'date', 'description']
    template_name = 'calendar_app/event_form.html'
    success_url = reverse_lazy('calendar_list')

class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    template_name = 'calendar_app/event_confirm_delete.html'
    success_url = reverse_lazy('calendar_list')