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
            caption=request.POST['caption'],
            description=request.POST['description'],
            imagePath=request.POST['imagePath'],
            created_at=request.POST['created_at']
        )

        return redirect(reverse("catalogapp:photos"))
    
@login_required
def photo_edit_form(request, photo_id):

    if request.method == 'GET':
        photo = Photo.objects.get(pk=photo_id)
        
        template = 'photos/form.html'
        context = {
            'photo': photo,
        }

        return render(request, template, context)