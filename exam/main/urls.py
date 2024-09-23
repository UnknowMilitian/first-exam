from django.urls import path
from .views import (
    ProductList,
    ProductAccessList,
    LessonListCreateView,
    LessonRetrieveUpdateDestroyView,
)

urlpatterns = [
    path("product-list", ProductList.as_view(), name="product-list"),
    path(
        "product-access-list", ProductAccessList.as_view(), name="product-access-list"
    ),
    path("lesson-list", LessonListCreateView.as_view(), name="lesson-list"),
    path(
        "lesson/<int:pk>",
        LessonRetrieveUpdateDestroyView.as_view(),
        name="lesson-update",
    ),
]
