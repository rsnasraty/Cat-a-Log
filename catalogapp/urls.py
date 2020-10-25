from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from catalogapp.views.photos.list import gallery
from catalogapp.views.auth.logout import logout_user
from .views.auth.home import home
from django.contrib.auth import logout, login
from catalogapp.views.pets.form import pet_edit_form
from catalogapp.views.photos.form import photo_edit_form, photo_form
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView


app_name = 'catalogapp'


# first argument: defines what the path looks like
# second argument: is what function should I run/what should show up that has the logic to show the info on the page
# third argument: is the name aka how you reference it in the future
urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('static/images/favicon.ico'))),
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('photos/', gallery, name='photos'),
    path('register/',register_user, name="register"),
    path('photos/<int:photo_id>', photo_details, name='photos'),
    path('photos/<int:photo_id>/form/', photo_edit_form, name='photo_edit_form'),
    path('photos/addnewphoto', photo_form, name='photo_form'),
    path('pets/', pet_list, name='pets'),
    path('pets/<int:pet_id>/', pet_details, name='pet'),
    path('pets/<int:pet_id>/form/', pet_edit_form, name='edit_form'),
    path('pets/addnewpet', pet_form, name='pet_form'),
    path('logout', logout_user, name='logout'),
    
]
