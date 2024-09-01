from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class Booking(admin.ModelAdmin):
    list_display = (
        "user",
        "item",
        "rent_day",
        "return_day",
    )

    list_filter = ("rent_day",)
