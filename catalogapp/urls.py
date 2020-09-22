from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from catalogapp.views.photos.list import photo_list
from .views.auth.home import home
from django.contrib.auth import logout, login

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
    path('pets/', pet_details, name='pet_details')
    # path('accounts/', login, name='login'),
    # path('accounts/', logout, name='logout')
    
    
]