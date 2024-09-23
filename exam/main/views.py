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
    LessonProgressSerializer,
)


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductAccessList(generics.ListCreateAPIView):
    queryset = ProductAccess.objects.all()
    serializer_class = ProductAccessSerializer
    permission_classes = [permissions.IsAdminUser]


class LessonListCreateView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]


class LessonRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]
