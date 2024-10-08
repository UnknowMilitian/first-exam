from django.urls import path
from .views import (
    ProductList,
    ProductAccessList,
    # LessonListCreateView,
    # LessonRetrieveUpdateDestroyView,
    UserLessonListView,
    ProductLessonListView,
    ProductStatisticsListView,
    RegisterView,
)

urlpatterns = [
    path("api/register/", RegisterView.as_view(), name="register"),
    path("product-list", ProductList.as_view(), name="product-list"),
    path(
        "product-access-list", ProductAccessList.as_view(), name="product-access-list"
    ),
    # path("lesson-list", LessonListCreateView.as_view(), name="lesson-list"),
    # path(
    #     "lesson/<int:pk>",
    #     LessonRetrieveUpdateDestroyView.as_view(),
    #     name="lesson-update",
    # ),
    path("lesson-list/", UserLessonListView.as_view(), name="lesson-list"),
    path(
        "product/<int:product_id>/lessons/",
        ProductLessonListView.as_view(),
        name="product-lesson-list",
    ),
    path(
        "product-statistics/",
        ProductStatisticsListView.as_view(),
        name="product-statistics",
    ),
]
