from django.urls import path, include
from . import views
from .views import *

app_name = 'catalogapp'


# first argument defines what the path looks like, second argument is what function should I run/what should show up that has the logic to show the info on the page, third argument is the name aka how you reference it in the future
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('gallery', views.gallery, name='gallery'),
    path('register/',register_user, name="register"),
    path('pets/', pet_list, name="pets")
]