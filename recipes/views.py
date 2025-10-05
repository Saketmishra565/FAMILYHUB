# recipes/views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin 
from .models import Recipe

class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recipes'

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['title', 'ingredients', 'instructions', 'prep_time'] 
    template_name = 'recipes/recipe_form.html'
    success_url = reverse_lazy('recipes_list')

    def form_valid(self, form):
        # रेसिपी साझा करने वाले यूज़र को सेट करें
        form.instance.shared_by = self.request.user
        return super().form_valid(form)

class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    fields = ['title', 'ingredients', 'instructions', 'prep_time']
    template_name = 'recipes/recipe_form.html'
    success_url = reverse_lazy('recipes_list')

class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    template_name = 'recipes/recipe_confirm_delete.html'
    success_url = reverse_lazy('recipes_list')