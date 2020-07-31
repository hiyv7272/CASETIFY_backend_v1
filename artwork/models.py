from django.db import models

from user.models import User


class Item(models.Model):
    name = models.CharField(max_length=500)

    class Meta:
        db_table = 'ITEM'


class Artist(models.Model):
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=500, null=True)

    class Meta:
        db_table = 'ARTIST'


class DeviceBrand(models.Model):
    name = models.CharField(max_length=500)

    class Meta:
        db_table = 'DEVICE_BRAND'


class Device(models.Model):
    name = models.CharField(max_length=500)
    device_brand = models.ForeignKey(DeviceBrand, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'DEVICE'


class DeviceColor(models.Model):
    name = models.CharField(max_length=500)
    device = models.ForeignKey(Device, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'DEVICE_COLOR'


class ArtworkType(models.Model):
    name = models.CharField(max_length=2500, null=True)

    class Meta:
        db_table = 'ARTWORK_TYPE'


class Artwork(models.Model):
    ITME = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    DEVICE = models.ForeignKey(Device, on_delete=models.SET_NULL, null=True)
    ARTWORK_TYPE = models.ForeignKey(ArtworkType, on_delete=models.SET_NULL, null=True)
    ARTIST = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=500)
    is_customed = models.NullBooleanField(null=True)
    custom_option = models.TextField(max_length=3000, null=True)
    introduction = models.TextField(max_length=2000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ARTWORK'


class ArtworkColor(models.Model):
    name = models.CharField(max_length=500)
    info = models.CharField(max_length=2500, null=True)

    class Meta:
        db_table = 'ARTWORK_COLOR'


class ArtworkColorArtwork(models.Model):
    ARTWORK = models.ForeignKey(Artwork, on_delete=models.SET_NULL, null=True)
    ARTWORK_COLOR = models.ForeignKey(ArtworkColor, on_delete=models.SET_NULL, null=True)
    DEVICE = models.ForeignKey(Device, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'ARTWORK_COLOR_ARTWORK'


class ArtworkPrice(models.Model):
    ARTWORK = models.ForeignKey(Artwork, on_delete=models.SET_NULL, null=True)
    DEVICE = models.ForeignKey(Device, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=18, decimal_places=2, null=True)

    class Meta:
        db_table = 'ARTWORK_PRICE'


class CustomArtworkImage(models.Model):
    ARTWORK = models.ForeignKey(Artwork, on_delete=models.SET_NULL, null=True)
    ARTWORK_COLOR = models.ForeignKey(ArtworkColor, on_delete=models.SET_NULL, null=True)
    image_1 = models.URLField(max_length=2500, null=True)
    image_2 = models.URLField(max_length=2500, null=True)
    image_3 = models.URLField(max_length=2500, null=True)
    image_4 = models.URLField(max_length=2500, null=True)
    image_5 = models.URLField(max_length=2500, null=True)

    class Meta:
        db_table = 'CUSTOM_ARTWORK_IMAGE'


class RegularArtworkImage(models.Model):
    ARTWORK = models.ForeignKey(Artwork, on_delete=models.SET_NULL, null=True)
    ARTWORK_COLOR = models.ForeignKey(ArtworkColor, on_delete=models.SET_NULL, null=True)
    DEVICE_COLOR = models.ForeignKey(DeviceColor, on_delete=models.SET_NULL, null=True)
    image_1 = models.URLField(max_length=2500, null=True)
    image_2 = models.URLField(max_length=2500, null=True)
    image_3 = models.URLField(max_length=2500, null=True)
    image_4 = models.URLField(max_length=2500, null=True)
    image_5 = models.URLField(max_length=2500, null=True)

    class Meta:
        db_table = 'REGULAR_ARTWORK_IMAGE'


class ArtworkReview(models.Model):
    ARTWORK = models.ForeignKey(Artwork, on_delete=models.SET_NULL, null=True)
    USER = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    rate = models.PositiveSmallIntegerField(null=True)
    comment_title = models.CharField(max_length=500, null=True)
    comment_text = models.TextField(max_length=1000, null=True)
    is_buyer = models.NullBooleanField(null=True)

    class Meta:
        db_table = 'ARTWORK_REVIEW'
