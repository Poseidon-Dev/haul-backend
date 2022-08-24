
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from transfers import views

app_name = 'transfers'

router = DefaultRouter()
router.register('transfers', views.TransfersViewSet)
router.register('scheduled', views.ScheduledTransfersViewSet)
router.register('history', views.HistoryTransfersViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
