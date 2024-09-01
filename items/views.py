from django.conf import settings
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Item
from .serializers import ItemListSerializer, ItemDetailSerializer
from reviews.serializers import ReviewSerializer
from medias.serializers import PhotoSerializer
from bookings.models import Booking
from bookings.serializers import PublicBookingSerializer, CreateItemBookingSerializer


class Items(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        all_items = Item.objects.all()
        serializer = ItemListSerializer(
            all_items,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = ItemDetailSerializer(data=request.data)
        if serializer.is_valid():
            item = serializer.save(owner=request.user)
            serializer = ItemDetailSerializer(
                item,
                context={"request": request},
            )
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )


class ItemDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        item = self.get_object(pk)
        serializer = ItemDetailSerializer(
            item,
            context={"request": request},
        )
        return Response(serializer.data)

    def put(self, request, pk):
        item = self.get_object(pk)
        if item.owner != request.user:
            raise PermissionDenied
        serializer = ItemDetailSerializer(
            item,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
        return Response(serializer.errors)

    def delete(self, request, pk):
        item = self.get_object(pk)
        if item.owner != request.user:
            raise PermissionDenied
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ItemReview(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        try:
            page = request.query_params.get("page", 1)
            page = int(page)
            if page == 0:
                page = 1
        except ValueError:
            page = 1
        page_size = settings.PAGE_SIZE
        start = (page - 1) * page_size
        end = start + page_size
        item = self.get_object(pk)
        serializer = ReviewSerializer(
            item.reviews.all()[start:end],
            many=True,
        )
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            review = serializer.save(
                user=request.user,
                item=self.get_object(pk),
            )
            serializer = ReviewSerializer(review)
            return Response(serializer.data)


class ItemPhotos(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            raise NotFound

    def post(self, request, pk):
        item = self.get_object(pk)
        if item.owner != request.user:
            raise PermissionDenied
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            photo = serializer.save(item=item)
            serializer = PhotoSerializer(photo)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class ItemBookings(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Item.objects.get(pk=pk)
        except:
            raise NotFound

    def get(self, request, pk):
        item = self.get_object(pk)
        now = timezone.localtime(timezone.now()).date()

        bookings = Booking.objects.filter(
            item=item,
            rent_day__gt=now,
        )
        serializer = PublicBookingSerializer(
            bookings,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request, pk):
        item = self.get_object(pk)
        serializer = CreateItemBookingSerializer(data=request.data)
        if serializer.is_valid():
            booking = serializer.save(
                item=item,
                user=request.user,
            )
            serializer = PublicBookingSerializer(booking)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
