from django.db import models
from .pet import Pet

class Photo(models.Model):
    pet = models.ForeignKey(
    Pet, on_delete=models.DO_NOTHING)
    caption = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    imagePath = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name = ("photo")
        verbose_name_plural = ("photos")


