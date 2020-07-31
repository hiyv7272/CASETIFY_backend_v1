from django.db import models

from user.models import User
from artwork.models import Artwork, ArtworkColor, ArtworkPrice


class Cart(models.Model):
    USER = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    ARTWORK = models.ForeignKey(Artwork, on_delete=models.SET_NULL, null=True)
    ARTWORK_COLOR = models.ForeignKey(ArtworkColor, on_delete=models.SET_NULL, null=True)
    ARTWORK_PRICE = models.ForeignKey(ArtworkPrice, on_delete=models.SET_NULL, null=True)
    is_customed = models.BooleanField(null=True)
    is_checkout = models.BooleanField(default=False, null=True)
    custom_info = models.TextField(max_length=3000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'CART'


class Order(models.Model):
    CART = models.ForeignKey('Cart', on_delete=models.SET_NULL, null=True)
    USER = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    ORDER_STATUS = models.ForeignKey('OrderStatus', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ORDER'


class OrderStatus(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'ORDER_STATUS'
