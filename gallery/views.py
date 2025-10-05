from django.views.generic import ListView, CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin 
from .models import Photo

class GalleryListView(LoginRequiredMixin, ListView):
    model = Photo
    template_name = 'gallery/gallery_list.html'
    context_object_name = 'photos'

class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['title', 'image', 'description']
    template_name = 'gallery/photo_form.html'
    success_url = reverse_lazy('gallery_list')

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)
    
class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    template_name = 'gallery/photo_confirm_delete.html' 
    success_url = reverse_lazy('gallery_list') 