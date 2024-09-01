from django.contrib import admin
from .models import Item


@admin.action(description="모두 0원으로")
def reset_prices(model_admin, request, items):
    for item in items.all():
        item.price = 0
        item.save()


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    actions = (reset_prices,)

    list_display = (
        "name",
        "price",
        "region",
        "owner",
        "updated_at",
    )
    list_filter = (
        "price",
        "updated_at",
    )
    search_fields = (
        "name",
        "owner__username",
    )
