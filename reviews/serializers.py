from rest_framework import serializers
from users.serializers import TinyUserSerializer
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    user = TinyUserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = (
            "user",
            "content",
            "rating",
        )


class UserReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
            "content",
            "rating",
            "created_at",
        )
