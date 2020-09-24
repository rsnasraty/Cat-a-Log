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
        photo_details = Photo.objects.get(pk=photo_id)
        
        template = 'photos/photo_edit_form.html'
        context = {
            'photo_details': photo_details,
        }

        return redirect(reverse("catalogapp:photos",args=[photo_id]))