from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def login(request):

    if request.method == "POST":
        
        authenticated_user = authenticate(username=request.POST['username'], password=request.POST['password'])

        if authenticated_user is not None:
            login(request, authenticated_user)

            # Redirect the browser to wherever you want to go 
            return redirect(reverse('catalogapp:home'))


