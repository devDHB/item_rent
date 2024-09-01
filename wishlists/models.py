from django.db import models
from common.models import Common


class Wishlist(Common):

    """Wishlist Model Definition"""

    name = models.CharField(
        max_length=150,
    )
    items = models.ManyToManyField(
        "items.Item",
        related_name="wishlists",
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="wishlists",
    )

    def __str__(self) -> str:
        return self.name
