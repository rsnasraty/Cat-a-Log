from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# blueprint to show what the thing will look like

class Pet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    favorite_toy = models.CharField(max_length=25)
    birthday = models.DateField(("Birthday"), auto_now=False, auto_now_add=False)

@receiver(post_save, sender=User)
def create_pet(sender, instance, created, **kwargs):
    if created:
        Pet.objects.create(user=instance)
        
@receiver(post-save, sender=User)
def save_pet(sender, instance, **kwargs):
    instance.pet.save()
