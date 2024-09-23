from django.urls import path
from .views import ProductList, ProductAccessList

urlpatterns = [
    path("product-list", ProductList.as_view(), name="product-list"),
    path(
        "product-access-list", ProductAccessList.as_view(), name="product-access-list"
    ),
]
