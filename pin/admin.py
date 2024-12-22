from django.contrib import admin
from .models import Pin


@admin.register(Pin)
class PinAdmin(admin.ModelAdmin):
    list_display = ["title", "user", ]
