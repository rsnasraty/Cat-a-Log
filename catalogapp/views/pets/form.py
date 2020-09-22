import sqlite3
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from catalogapp.models import Pet
from ..helpers.get_pet import get_pet
from ..connection import Connection



@login_required
def pet_form(request):

#making a new pet, just need to show the form so you don't need to get a pe
# need the GET in order to define what the method is to get the URL
    if request.method == 'GET':

        template = 'pets/form.html'
        context = {
        }

        return render(request, template, context)
    #if a post request is made, then they want to MAKE a pet. there is no pet to GET on this page.
    elif request.method == 'POST':
        new_pet = Pet.objects.create(
            user=request.user,
            name=request.POST['pet_name'],
            favorite_toy=request.POST['pet_favorite_toy'],
            birthday=request.POST['pet_birthday'],
        )


        return redirect(reverse("catalogapp:pets"))
    
@login_required
def pet_edit_form(request, pet_id):

    if request.method == 'GET':
        pet = Pet.objects.get(pk=pet_id)
        
        template = 'pets/form.html'
        context = {
            'pet': pet,
        }

        return render(request, template, context)