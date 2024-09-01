from django.contrib import admin
from .models import Review


class RatingFilter(admin.SimpleListFilter):
    title = "Good Or Bad Rating"

    parameter_name = "ratingfilter"

    def lookups(self, request, model_admin):
        return [
            ("good", "3~5👍"),
            ("bad", "1~2👎"),
        ]

    def queryset(self, request, reviews):
        rating_score = self.value()
        if rating_score == "good":
            return reviews.filter(rating__gte=3)
        elif rating_score == "bad":
            return reviews.filter(rating__lt=3)
        else:
            reviews


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "user",
        "item",
        "content",
    )
    list_filter = (
        RatingFilter,
        "rating",
        "user__is_host",
    )
