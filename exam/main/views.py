from django.shortcuts import render
from .models import Product, ProductAccess
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# Inner-Project import
from .models import Product, ProductAccess
from .serializers import ProductSerializer, ProductAccessSerializer


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ProductAccessList(generics.ListCreateAPIView):
    queryset = ProductAccess.objects.all()
    serializer_class = ProductAccessSerializer
    permission_classes = [IsAdminUser]
