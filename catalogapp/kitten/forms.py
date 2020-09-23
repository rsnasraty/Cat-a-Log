from django import forms 
from catalogapp.models.kitten import Kitten

class KittenForm(forms.ModelForm): 

    class Meta: 
        model = Kitten
        fields = ['name', 'kitten_Main_Img'] 