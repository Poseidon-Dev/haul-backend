from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/equipment/', include('equipment.urls')),
    path('api/profiles/', include('profiles.urls')),
    path('api/transfers/', include('transfers.urls')),
]
