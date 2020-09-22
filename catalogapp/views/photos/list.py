import sqlite3
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from catalogapp.models import Photo
from django.contrib.auth.models import User



@login_required
def photo_list(request):
    if request.method == 'GET':
        photos = Photo.objects.all()

        template = 'photos/list.html'
        context = {
            'photos': photos
        }
        
        

        return render(request, template, context)
