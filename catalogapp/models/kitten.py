from django.db import models

class Kitten(models.Model): 
    name = models.CharField(max_length=50) 
    kitten_Main_Img = models.ImageField(upload_to='images/') 