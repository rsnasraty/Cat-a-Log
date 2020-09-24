import sqlite3
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from catalogapp.models import Photo
# from ..helpers.get_photo import get_photo
from ..connection import Connection


@login_required

def photo_form(request):

    if request.method == 'GET':

        template = 'photos/form.html'
        context = {
        }

        return render(request, template, context)
    
    elif request.method == 'POST':
        new_photo = Photo.objects.create(
            user=request.user,
            imagePath=request.POST['imagePath'],
            caption=request.POST['photo_caption'],
            description=request.POST['photo_description'],
            created_at=request.POST['created_at'],
        )

        return redirect(reverse("catalogapp:photos"))
    
@login_required
def photo_edit_form(request, photo_id):
#GET brings back that specific photo by its id and stores it under photo_details
    if request.method == 'GET':
        photo_details = Photo.objects.get(pk=photo_id)
        
        template = 'photos/photo_edit_form.html'
        context = {
            'photo_details': photo_details,
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
            photo_to_update.caption = form_data["photo_caption"]
            photo_to_update.description = form_data["photo_description"]
            # photo_to_update.imagePath= form_data["imagePath"]
            # photo_to_update.created_at= form_data["created_at"]

            #Third, save the newly updated object back to the db
            # The photo_to_update object has its id on it, since we pulled it out of the db, so when we call save() Django knows to update, not create a new row. Awesome!
            photo_to_update.save()

            return redirect(reverse('catalogapp:photos'))
    
  