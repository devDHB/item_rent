from django.db import models
from common.models import Common


class Booking(Common):

    """Booking Model Definition"""

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        verbose_name="예약자",
        related_name="bookings",
    )
    item = models.ForeignKey(
        "items.Item",
        on_delete=models.CASCADE,
        verbose_name="제목",
        related_name="bookings",
    )
    rent_day = models.DateField(
        verbose_name="대여일",
    )
    return_day = models.DateField(
        verbose_name="반납일",
    )

    def __str__(self) -> str:
        return f"{self.item} / 예약자 : {self.user}"
