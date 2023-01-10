from django.contrib import admin
from core.admin import BaseAdmin
from .models import Company, Division


@admin.register(Company)
class CompanyAdmin(BaseAdmin):
    pass


@admin.register(Division)
class DivisionAdmin(BaseAdmin):
    pass
