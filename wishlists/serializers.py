from rest_framework.serializers import ModelSerializer
from .models import Wishlist
from items.serializers import ItemListSerializer


class WishlistSerializer(ModelSerializer):
    items = ItemListSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Wishlist
        fields = (
            "pk",
            "name",
            "items",
        )
