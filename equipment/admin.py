from django.contrib import admin

from core.admin import BaseAdmin
from .models import Equipment


@admin.register(Equipment)
class EquipmentAdmin(BaseAdmin):
    pass
