import sqlite3
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from catalogapp.models import *

# request is the request a browser made, method attribute is like a fetch call
# Does GET by default, so don't need it unless doing multiple things
@login_required
def gallery(request):
    if request.method == 'GET':
        # # using django ORM
        pets = Pet.objects.all()
    
        # for pet_photo in pet_photos:
        #     for pet in pets:
        #         pet.photos = list()
        #         for photo in photos:
        #             if pet.id == photo.pet_id:
        #                 pet.photos.append(photo)
        
        template = 'pet_photos/list.html'
        # pets on left is the label/reference in the template, on right is the data
        context = {
            'pets': pets
        }
        return render(request, template, context)
        # render connects all three MVT pieces together
            