from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from catalogapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalogapp.urls')),
    path('register/', register_user, name="register")
]
