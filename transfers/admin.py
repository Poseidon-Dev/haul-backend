from django.contrib import admin
from core.admin import BaseAdmin
from .models import Transfers, TransferHistory


@admin.register(Transfers)
class TransfersAdmin(BaseAdmin):
    pass


@admin.register(TransferHistory)
class TransferHistoryAdmin(BaseAdmin):
    pass
