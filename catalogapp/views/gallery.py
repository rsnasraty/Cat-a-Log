import sqlite3
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from catalogapp.models import *

# request is the request a browser made, method attribute is like a fetch call
# Does GET by default, so don't need it unless doing multiple things
def gallery(request):
    if request.method == 'GET':
        # # using django ORM
        pets = Pet.objects.all()
     
            # pet_id=1 is Mellie, pet_id=2 is Cocoa
            # id is just the join table incrementing
            # photo is the photo id
            # id=1, pet_id=1, photo_id=1
            # id=2, pet_id=1, photo_id=2
            # id=3, pet_id=1, photo_id=3
            # id=4, pet_id=2, photo_id=4
            # id=4, pet_id=2, photo_id=5
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
            