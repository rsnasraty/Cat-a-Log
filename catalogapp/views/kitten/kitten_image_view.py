from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from catalogapp.kitten.forms import KittenForm


# Create your views here. 
def kitten_image_view(request): 

    if request.method == 'POST': 
        form = KittenForm(request.POST, request.FILES) 

        if form.is_valid(): 
            form.save()     
            return redirect('/image_upload/success') 
    else: 
        form = KittenForm() 
    return render(request, 'kittens/kitten_image_form.html', {'form' : form}) 


def success(request): 
    return HttpResponse('successfully uploaded') 