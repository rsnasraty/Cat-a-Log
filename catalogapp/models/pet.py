from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# blueprint to show what the thing will look like, based off librarian ORM model

class Pet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    favorite_toy = models.CharField(max_length=20)
    birthday = models.DateField(auto_now=False, auto_now_add=False)

