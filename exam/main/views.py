from django.shortcuts import render
from .models import Product, ProductAccess
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import permissions


# Inner-Project import
from .models import Product, ProductAccess, Lesson, LessonProgress
from .serializers import (
    ProductSerializer,
    ProductAccessSerializer,
    LessonSerializer,
    LessonWithProgressSerializer,
    ProductStatisticsSerializer,
)


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductAccessList(generics.ListCreateAPIView):
    queryset = ProductAccess.objects.all()
    serializer_class = ProductAccessSerializer
    permission_classes = [permissions.IsAdminUser]


# class LessonListCreateView(generics.ListCreateAPIView):
#     queryset = Lesson.objects.all()
#     serializer_class = LessonSerializer
#     permission_classes = [permissions.IsAuthenticated]


# class LessonRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Lesson.objects.all()
#     serializer_class = LessonSerializer
#     permission_classes = [permissions.IsAuthenticated]


class UserLessonListView(generics.ListAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        # Get all products the user has access to
        products_with_access = ProductAccess.objects.filter(
            user_access=self.request.user, can_view=True
        ).values_list("product", flat=True)

        # Return lessons related to these products
        return Lesson.objects.filter(products__in=products_with_access).distinct()


class ProductLessonListView(generics.ListAPIView):
    serializer_class = LessonWithProgressSerializer

    def get_queryset(self):
        product_id = self.kwargs["product_id"]

        # Check if the user has access to the product
        access = ProductAccess.objects.filter(
            user_access=self.request.user, product_id=product_id, can_view=True
        ).exists()

        if not access:
            return Lesson.objects.none()

        # Return lessons for the specific product
        return Lesson.objects.filter(products__id=product_id).distinct()


class ProductStatisticsListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductStatisticsSerializer
