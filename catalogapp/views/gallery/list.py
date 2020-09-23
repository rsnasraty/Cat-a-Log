import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from catalogapp.models import Photo
from ..connection import Connection

@login_required
def gallery(request):
    if request.method == "GET":

        all_photos = Photo.objects.filter(user=request.user)

        template_name = 'gallery/list.html'

        context = {
            'all_photos': all_photos
        }

        return render(request, template_name, context)
