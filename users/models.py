from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    """User Model Definition"""

    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")

    class LanguagueChoices(models.TextChoices):
        KR = ("kr", "Korean")
        EN = ("en", "English")

    avatar = models.URLField(blank=True)
    name = models.CharField(
        max_length=100,
        default="",
    )
    is_host = models.BooleanField(default=False)
    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
    )
    languague = models.CharField(
        max_length=2,
        choices=LanguagueChoices.choices,
    )

    def rating(user):
        count = user.reviews.count()
        if count == 0:
            return 0
        else:
            total_rating = 0
            for review in user.reviews.all().values("rating"):
                total_rating += review["rating"]
            return round(total_rating / count, 2)
