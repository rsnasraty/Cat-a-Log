from django.urls import path, include
from . import views

app_name = 'catalogapp'

urlpatterns = [
    path('gallery', views.gallery, name='gallery')
]