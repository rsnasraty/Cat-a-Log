from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from catalogapp.views.photos.list import photo_list
from .views.auth.home import home
from django.contrib.auth import logout, login
from catalogapp.views.pets.form import pet_edit_form

app_name = 'catalogapp'


# first argument defines what the path looks like, second argument is what function should I run/what should show up that has the logic to show the info on the page, third argument is the name aka how you reference it in the future
urlpatterns = [
    path('home/', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('gallery/', gallery, name='gallery'),
    path('pets/', pet_list, name='pets'),
    path('register/',register_user, name="register"),
    path('photos/', photo_list, name='photos'),
    path('pets/', pet_form, name='pet_form'),
    path('pets/<int:pet_id>/', pet_details, name='pet'),
    path('pets/<int:pet_id>/form/', pet_edit_form, name='pet_edit_form'),
    
    
]