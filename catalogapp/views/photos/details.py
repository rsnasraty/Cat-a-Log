import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from catalogapp.models import Photo
from ..connection import Connection


@login_required
def photo_details(request, photo_id):
    if request.method == 'GET':
        #get one photo and storing that one photo into the photo variable
        photo = Photo.objects.get(pk=photo_id)

        template = 'photos/detail.html'
        
        context = {
            #putting information stored in photo above, here
            'photo': photo
        }
    #return pushes template in detail.html together with context
        return render(request, template, context)

    if request.method == 'POST':
            form_data = request.POST

            # Check if this POST is for deleting a book
            #
            # Note: You can use parenthesis to break up complex
            #       `if` statements for higher readability
            if (
                "actual_method" in form_data
                and form_data["actual_method"] == "DELETE"
                ):
                
                    photo_to_burn = Photo.objects.get(pk=photo_id)
                    photo_to_burn.delete()


                    return redirect(reverse('catalogapp:photos'))