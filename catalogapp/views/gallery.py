import sqlite3
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from catalogapp.models import *
from .connection import Connection

# request is the request a browser made, method attribute is like a fetch call
# Does GET by default, so don't need it unless doing multiple things
def gallery(request):
    if request.method == 'GET':
        # using django ORM
        pets = Pet.objects.all()
        template = 'pet_photos/list.html'
        # pets on left is the label/reference in the template, on right is the data
        context = {
            'pets': pets
        }
        return render(request, template, context)
        # render connects all three MVT pieces together
            