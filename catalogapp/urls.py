from django.urls import path, include
from . import views
from .views import *

app_name = 'catalogapp'

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('gallery', views.gallery, name='gallery'),
    path('register/',register_user, name="register")
]