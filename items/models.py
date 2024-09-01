from django.db import models
from common.models import Common


class Item(Common):

    """Item Model Definition"""

    name = models.CharField(
        verbose_name="제목",
        max_length=100,
    )
    price = models.PositiveIntegerField(
        verbose_name="가격(일)",
        help_text="원 으로 적어주세요",
    )
    description = models.TextField(
        verbose_name="내용",
    )
    region = models.CharField(
        verbose_name="지역",
        max_length=120,
        help_text="시, 구 로 적어주세요",
    )
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="items",
    )

    def __str__(self) -> str:
        return self.name
