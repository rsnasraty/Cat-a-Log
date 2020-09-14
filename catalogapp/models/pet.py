from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE
from django.dispatch import receiver
from .owner import Owner


class Pet(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE
    owner = models.ForeignKey(Owner,on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    birthday = models.models.models.DateField( auto_now=False, auto_now_add=False)
    favorite_toy= models.CharField(max_length=20)
