# recipes/models.py
from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.TextField(help_text="सामग्री को हर लाइन में एक-एक करके लिखें")
    instructions = models.TextField()
    prep_time = models.CharField(max_length=50, null=True, blank=True)
    shared_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title