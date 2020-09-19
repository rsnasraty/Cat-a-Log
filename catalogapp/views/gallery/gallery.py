import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from catalogapp.models import PetPhoto

@login_required
def gallery(request):
    if request.method == "GET":

        all_pet_photos = PetPhoto.objects.all()

        template_name = 'pet_photos/list.html'

        context = {
            'all_pet_photos': all_pet_photos
        }

        return render(request, template_name, context)
