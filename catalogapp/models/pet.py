from django.db import models

class Pet(models.Model):
    
    
    class Meta:
        verbose_name = ("")
        verbose_name_plural = ("s")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
