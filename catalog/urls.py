from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from catalogapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalogapp.urls'))
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)