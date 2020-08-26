from django.db import models

from user.models import User


class Featured(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'FEATURED'


class DeviceBrand(models.Model):
    name = models.CharField(max_length=500)

    class Meta:
        db_table = 'DEVICE_BRAND'


class DeviceColor(models.Model):
    name = models.CharField(max_length=500)
    DEVICE = models.ForeignKey('Device', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'DEVICE_COLOR'


class DeviceModel(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        db_table = 'DEVICE_MODEL'


class Device(models.Model):
    FEATURED = models.ForeignKey(Featured, on_delete=models.SET_NULL, null=True)
    DEVICE_BRAND = models.ForeignKey(DeviceBrand, on_delete=models.SET_NULL, null=True)
    DEVICE_MODEL = models.ForeignKey(DeviceModel, on_delete=models.SET_NULL, null=True)
    DEVICE_COLOR = models.ForeignKey(DeviceColor, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=300)
    is_use = models.BooleanField()

    class Meta:
        db_table = 'DEVICE'


class Artwork(models.Model):
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=1000, null=True)

    class Meta:
        db_table = 'ARTWORK'


class PhonecaseColor(models.Model):
    name = models.CharField(max_length=500)
    info = models.CharField(max_length=1000, null=True)

    class Meta:
        db_table = 'PHONECASE_COLOR'


class PhonecaseType(models.Model):
    name = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'PHONECASE_TYPE'


class Phonecase(models.Model):
    FEATURED = models.ForeignKey(Featured, on_delete=models.SET_NULL, null=True)
    DEVICE_MODEL = models.ForeignKey(DeviceModel, on_delete=models.SET_NULL, null=True)
    PHONECASE_COLOR = models.ForeignKey(PhonecaseColor, on_delete=models.SET_NULL, null=True)
    PHONECASE_TYPE = models.ForeignKey(PhonecaseType, on_delete=models.SET_NULL, null=True)
    ARTWORK = models.ForeignKey(Artwork, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=2000, null=True)
    is_custom = models.BooleanField(null=True)
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)
    is_use = models.BooleanField()

    class Meta:
        db_table = 'PHONECASE'


class PhonecasePrice(models.Model):
    PHONECASE = models.ForeignKey(Phonecase, on_delete=models.SET_NULL, null=True)
    DEVICE = models.ForeignKey(Device, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=18, decimal_places=2, null=True)

    class Meta:
        db_table = 'PHONECASE_PRICE'


class PhonecaseColorDeivce(models.Model):
    PHONECASE = models.ForeignKey(Phonecase, on_delete=models.SET_NULL, null=True)
    PHONECASE_COLOR = models.ForeignKey(PhonecaseColor, on_delete=models.SET_NULL, null=True)
    DEVICE = models.ForeignKey(Device, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'PHONECASE_COLOR_DEVICE'


class PhonecaseImage(models.Model):
    PHONECASE = models.ForeignKey(Phonecase, on_delete=models.SET_NULL, null=True)
    image_url_1 = models.URLField(max_length=2500, null=True)
    image_url_2 = models.URLField(max_length=2500, null=True)
    image_url_3 = models.URLField(max_length=2500, null=True)
    image_url_4 = models.URLField(max_length=2500, null=True)
    image_url_5 = models.URLField(max_length=2500, null=True)
    image_url_6 = models.URLField(max_length=2500, null=True)

    class Meta:
        db_table = 'PHONECASE_IMAGE'


class PhonecaseReview(models.Model):
    USER = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    PHONECASE = models.ForeignKey(Phonecase, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=500, null=True)
    comment = models.TextField(max_length=1000, null=True)
    rate = models.PositiveSmallIntegerField(null=True)
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)
    is_use = models.BooleanField()

    class Meta:
        db_table = 'PHONECASE_REVIEW'
