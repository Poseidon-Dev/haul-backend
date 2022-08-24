
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles import views

app_name = 'profile'

router = DefaultRouter()
router.register('company', views.CompanyViewSet)
router.register('division', views.DivisionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
