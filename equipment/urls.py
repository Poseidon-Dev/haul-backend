
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from equipment import views

app_name = 'equipment'

router = DefaultRouter()
router.register('equipment', views.ActiveEquipmentViewSet)
router.register('equipmentTransfers', views.TransferEquipmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
