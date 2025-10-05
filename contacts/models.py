# contacts/models.py
from django.db import models
from django.contrib.auth.models import User

class FamilyContact(models.Model):
    name = models.CharField(max_length=100)
    relation = models.CharField(max_length=100, help_text="जैसे: माँ, भाई, चाचा")
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name