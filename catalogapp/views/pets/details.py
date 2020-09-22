import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from catalogapp.models import Pet
from ..connection import Connection


@login_required
def pet_details(request, pet_id):
    if request.method == 'GET':
        pet = Pet.objects.get(pk=pet_id)

        template = 'pets/detail.html'
        context = {
            'pet_details': pet_details
        }

        return render(request, template, context)


    if request.method == 'POST':
        form_data = request.POST

        # Check if this POST is for editing a pet
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):

            # First, get the istance from the db, then update its properties

            pet_to_update = Pet.objects.get(pk=pet_id)

            # Second, set the updated values on the instance object from the db with the form values
            pet_to_update.name = form_data["name"]
            pet_to_update.favorite_toy = form_data["favorite_toy"]
            pet_to_update.birthday = form_data["birthday"]

            #Third, save the newly updated object back to the db
            # The pet_to_update object has its id on it, since we pulled it out of the db, so when we call save() Django knows to update, not create a new row. Awesome!
            pet_to_update.save()

            return redirect(reverse('catalogapp:pets'))
