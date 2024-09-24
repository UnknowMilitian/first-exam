from django.shortcuts import render
from .models import Product, ProductAccess
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework import status


# Inner-Project import
from .models import Product, ProductAccess, Lesson, LessonProgress
from .serializers import (
    ProductSerializer,
    ProductAccessSerializer,
    LessonSerializer,
    LessonWithProgressSerializer,
    ProductStatisticsSerializer,
    UserSerializer,
)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Optionally, create a token for the user upon registration
        from rest_framework_simplejwt.tokens import AccessToken

        token = AccessToken.for_user(user)
        return Response(
            {"user": serializer.data, "token": str(token)},
            status=status.HTTP_201_CREATED,
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
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            products_with_access = ProductAccess.objects.filter(
                user_access=self.request.user, can_view=True
            ).values_list("product", flat=True)

            # Return lessons related to these products
            return Lesson.objects.filter(products__in=products_with_access).distinct()
        else:
            return Lesson.objects.none()  # or raise an exception


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
