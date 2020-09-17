from django.db import models
from .pet import Pet
from .photo import Photo

class PetPhoto(models.Model):
    pet = models.ForeignKey(
        Pet, on_delete=models.DO_NOTHING)
    photo = models.ForeignKey(
        Photo, on_delete=models.DO_NOTHING, related_name="craycrayphotos")
    class Meta:
        verbose_name = ("pet photo")
        verbose_name_plural = ("pets photos")

