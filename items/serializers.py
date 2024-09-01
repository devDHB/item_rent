from rest_framework import serializers
from .models import Item
from users.serializers import TinyUserSerializer
from reviews.serializers import ReviewSerializer
from medias.serializers import PhotoSerializer
from wishlists.models import Wishlist


class ItemDetailSerializer(serializers.ModelSerializer):
    owner = TinyUserSerializer(read_only=True)
    is_owner = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    photos = PhotoSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Item
        fields = "__all__"

    def get_is_owner(self, item):
        request = self.context["request"]
        return item.owner == request.user

    def get_is_liked(self, item):
        request = self.context["request"]
        return Wishlist.objects.filter(
            user=request.user,
            items__id=item.pk,
        ).exists()


class ItemListSerializer(serializers.ModelSerializer):
    is_owner = serializers.SerializerMethodField()
    photos = PhotoSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Item
        fields = (
            "pk",
            "photos",
            "owner",
            "name",
            "price",
            "region",
            "is_owner",
        )

    def get_is_owner(self, item):
        request = self.context["request"]
        return item.owner == request.user
