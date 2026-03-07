from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
 # Note: Not really needed but part of default
    path('', include('detective.urls')),
]
