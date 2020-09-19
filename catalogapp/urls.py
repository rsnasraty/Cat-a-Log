from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from catalogapp import views
from catalogapp.views.pets.list import pet_list
from .views import login_user, home, logout_user, gallery, register_user, pets

app_name = 'catalogapp'


# first argument defines what the path looks like, second argument is what function should I run/what should show up that has the logic to show the info on the page, third argument is the name aka how you reference it in the future
urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('gallery/', gallery, name='gallery'),
    path('pets/', pet_list, name='pets'),
    path('register/',register_user, name="register"),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    
]