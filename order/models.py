from django.db import models

from user.models import User
from artwork.models import Phonecase, PhonecasePrice


class Orderer(models.Model):
    USER = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    zipcode = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=11)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ORDERER'


class Cart(models.Model):
    USER = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    PHONECASE = models.ForeignKey(Phonecase, on_delete=models.SET_NULL, null=True)
    PHONECASE_PRICE = models.ForeignKey(PhonecasePrice, on_delete=models.SET_NULL, null=True)
    is_custom = models.BooleanField(null=True)
    custom_info = models.TextField(max_length=2000, null=True)
    quantity = models.SmallIntegerField()
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)
    is_use = models.BooleanField()

    class Meta:
        db_table = 'CART'


class Order(models.Model):
    USER = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    ORDERER = models.ForeignKey(Orderer, on_delete=models.SET_NULL, null=True)
    order_number = models.CharField(max_length=100)
    delivery_price = models.DecimalField(max_digits=18, decimal_places=2, null=True)
    sub_total_price = models.DecimalField(max_digits=18, decimal_places=2, null=True)
    total_price = models.DecimalField(max_digits=18, decimal_places=2, null=True)
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)
    is_use = models.BooleanField()

    class Meta:
        db_table = 'ORDER'


class CheckoutStatus(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'CHECKOUT_STATUS'


class CheckOut(models.Model):
    USER = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    CART = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    ORDER = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    CHECKOUT_STATUS = models.ForeignKey(CheckoutStatus, on_delete=models.SET_NULL, null=True)
    custom_info = models.TextField(max_length=3000, null=True)
    quantity = models.SmallIntegerField()
    sell_price = models.DecimalField(max_digits=18, decimal_places=2, null=True)
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)
    is_use = models.BooleanField()

    class Meta:
        db_table = 'CHECKOUT'
