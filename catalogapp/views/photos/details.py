import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from catalogapp.models import Photo
from ..connection import Connection


@login_required
def photo_details(request, photo_id):
    if request.method == 'GET':
        photo = Photo.objects.get(pk=photo_id)

        template = 'photos/detail.html'
        context = {
            'photo_details': photo_details
        }

        return render(request, template, context)


    if request.method == 'POST':
        form_data = request.POST

        # Check if this POST is for editing a photo
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):

            # First, get the istance from the db, then update its properties

            photo_to_update = Photo.objects.get(pk=photo_id)

            # Second, set the updated values on the instance object from the db with the form values
            photo_to_update.name = form_data["name"]
            photo_to_update.favorite_toy = form_data["favorite_toy"]
            photo_to_update.birthday = form_data["birthday"]

            #Third, save the newly updated object back to the db
            # The photo_to_update object has its id on it, since we pulled it out of the db, so when we call save() Django knows to update, not create a new row. Awesome!
            photo_to_update.save()

            return redirect(reverse('catalogapp:photos'))