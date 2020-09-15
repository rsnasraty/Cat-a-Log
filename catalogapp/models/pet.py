from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User


class Pet(SafeDeleteModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    favorite_toy = models.CharField(max_length=25)
    birthday = models.models.DateField(("Birthday"), auto_now=False, auto_now_add=False)