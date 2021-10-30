from django.contrib import admin

from .models import Shawarma

@admin.register(Shawarma)
class ShawarmaAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
