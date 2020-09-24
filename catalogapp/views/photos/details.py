import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from catalogapp.models import Photo
from ..connection import Connection


@login_required
def photo_details(request, photo_id):
    if request.method == 'GET':
        #get one photo and storing that one photo into the photo variable
        photo = Photo.objects.get(pk=photo_id)

        template = 'photos/detail.html'
        
        context = {
            #putting information stored in photo above, here
            'photo': photo
        }
    #return pushes template in detail.html together with context
        return render(request, template, context)


    # if request.method == 'POST':
    #     form_data = request.POST

    #     # Check if this POST is for editing a photo
    #     if (
    #         "actual_method" in form_data
    #         and form_data["actual_method"] == "PUT"
    #     ):

    #         # First, get the istance from the db, then update its properties

    #         photo_to_update = Photo.objects.get(pk=photo_id)

    #         # Second, set the updated values on the instance object from the db with the form values
    #         photo_to_update.caption = form_data["photo_caption"]
    #         photo_to_update.description = form_data["photo_description"]
    #         photo_to_update.imagePath= form_data["imagePath"]
    #         photo_to_update.created_at= form_data["created_at"]

    #         #Third, save the newly updated object back to the db
    #         # The photo_to_update object has its id on it, since we pulled it out of the db, so when we call save() Django knows to update, not create a new row. Awesome!
    #         photo_to_update.save()

    #         return redirect(reverse('catalogapp:photos'))

    