from django.utils import timezone
from rest_framework import serializers
from .models import Booking


class CreateItemBookingSerializer(serializers.ModelSerializer):
    rent_day = serializers.DateField()
    return_day = serializers.DateField()

    class Meta:
        model = Booking
        fields = (
            "rent_day",
            "return_day",
        )

    def validate_rent_day(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("과거의 날짜입니다.")
        return value

    def validate_return_day(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("과거의 날짜입니다.")
        return value

    def validate(self, data):
        if data["return_day"] <= data["rent_day"]:
            raise serializers.ValidationError("대여일이 반납일보다 빨라야 합니다.")
        if Booking.objects.filter(
            rent_day__lte=data["return_day"],
            return_day__gte=data["rent_day"],
        ).exists():
            raise serializers.ValidationError("이미 예약되어 있는 날짜입니다.")
        return data


class PublicBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = (
            "pk",
            "rent_day",
            "return_day",
        )
