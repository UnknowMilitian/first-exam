from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="product")
    title = models.CharField(_("Product title"), max_length=255)
    created_at = models.DateTimeField(_("Product created date"), auto_now_add=True)

    def __str__(self):
        return f"Product - {self.title}"


class ProductAccess(models.Model):
    user_access = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    can_edit = models.BooleanField(_("Can edit"), default=False)
    can_view = models.BooleanField(_("Can view"), default=True)
    granted_at = models.DateTimeField(_("Granted at"), auto_now_add=True)

    def __str__(self):
        return f"User '{self.user_access}' has access to product '{self.product.title}'"
