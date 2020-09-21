from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from catalogapp.models import Pet
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def register_user(request):
    """Handles creation of a new user for auth

        Args:
        request = full http object
    """

    # For handling when user submits the form data
    if request.method == "POST":
#create_user is specifically a built-in method, create method brings back the entire created object
        print(request.POST['pet_birthday'])
        new_user = User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            password=request.POST['password'],
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name']
        )
        #Adding a new pet to the Pet table so pet.objects.create
        new_pet = Pet.objects.create (
            #Grabs the entire user object created on line 19, don't need to use the brackets to name a key, since user is created you don't need to reference the client side 
            user=new_user,
            #request comes from the client side
            name=request.POST['pet_name'],
            birthday=request.POST['pet_birthday'],
            favorite_toy=request.POST['pet_favorite_toy']
        )
        
        
        
        authenticated_user = authenticate(username=request.POST['username'], password=request.POST['password'])

        if authenticated_user is not None:
            login(request, authenticated_user)

            # Redirect the browser to wherever you want to go after registering
            return redirect(reverse('catalogapp:home'))

    # handles a request to load the empty form for the user to fill out
    else:
        template = 'registration/register.html'

    return render(request, template, {})
