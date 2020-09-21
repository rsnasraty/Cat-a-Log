# id
# petid
# description 
# caption

import sqlite3
from django.shortcuts import render
from catalogapp.models import Photo, Pet
# from ..connection import Connection

def create_photo(cursor, row):
    _row = sqlite3.Row(cursor, row)

    Photo = Photo()
    photo.id = _row["photo_id"]
    photo.description = _row["description"]
    photo.caption = _row["caption"]

    # Note: You are adding a blank pet list to the Photo object
    # This list will be populated later (see below)
    photo.pets = []

    pet = Pet()
    pet.id = _row["pet_id"]
    pet.name = _row["name"]
    pet.birthday = _row["birthday"]
    pet.favorite_toy = _row["favorite_toy"]

    # Return a tuple containing the photo and the
    # pet built from the data in the current row of
    # the data set
    return (photo, pet)

def photo_list(request):

    photo_list = Photo.objects.all()
    template_name = 'photos/list.html'

    # photo_groups.values()
    context = {
        'all_photos': photo_list
    }

    return render(request, template_name, context)