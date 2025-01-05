from django.contrib import admin
from .models import AccountInfo
# Register your models here.
@admin.register(AccountInfo)
class AccountInfo(admin.ModelAdmin):
    list_display = ["gender","user"]