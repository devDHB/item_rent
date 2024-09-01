from django.urls import path
from . import views


urlpatterns = [
    path("", views.Items.as_view()),
    path("<int:pk>", views.ItemDetail.as_view()),
    path("<int:pk>/reviews", views.ItemReview.as_view()),
    path("<int:pk>/photos", views.ItemPhotos.as_view()),
    path("<int:pk>/bookings", views.ItemBookings.as_view()),
]
