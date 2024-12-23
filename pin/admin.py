from django.contrib import admin
from .models import Pin


@admin.register(Pin)
class PinAdmin(admin.ModelAdmin):
    list_display = ["title", "user", "display_boards"]

    # list in which board the pin is pinned
    def display_boards(self,obj):
        x =   " --- ".join([el.name for el in obj.boards.all() ])
        print("xxxxxxxxxxx====",x)
        return  x

    display_boards.short_description = "Boards"

