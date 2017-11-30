from django.db import models
from django.contrib.auth.models import AbstractUser

from shopping_carts.models import ShoppingCart

class User(AbstractUser):
      birthday = models.DateField(null=True, blank=True)
      shopping_cart = models.OneToOneField(ShoppingCart, null= True, blank=True)
