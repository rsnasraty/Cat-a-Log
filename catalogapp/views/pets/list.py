import sqlite3
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from catalogapp.models import Pet


@login_required
def pet_list(request):
    if request.method == 'GET':
        pet_list = Pet.objects.all()

        template = 'pets/list.html'
        context = {
            'all_pets': pet_list
        }
        

        return render(request, template, context)


        return redirect(reverse('catalogapp:pets'))