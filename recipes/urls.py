# recipes/urls.py
from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.RecipeListView.as_view(), name='recipes_list'), 
    path('new/', views.RecipeCreateView.as_view(), name='recipe_create'),
    path('edit/<int:pk>/', views.RecipeUpdateView.as_view(), name='recipe_update'),
    path('delete/<int:pk>/', views.RecipeDeleteView.as_view(), name='recipe_delete'),
]