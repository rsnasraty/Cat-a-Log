from django.db import models
from .pet import Pet
from .photo import Photo

#based off book model 

class PetPhoto(models.Model):
    pet = models.ForeignKey(
        Pet, null=True, default=None,on_delete=models.DO_NOTHING)
    photo = models.ForeignKey(
        Photo, null=True,default=None, on_delete=models.DO_NOTHING, related_name="gallery")
    class Meta:
        verbose_name = ("pet photo")
        verbose_name_plural = ("pets photos")

