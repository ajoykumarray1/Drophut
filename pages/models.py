from django.db import models

# Create your models here.
class Products_listing(models.Model):
    product_title = models.CharField(max_length=200)
    product_name = models.CharField(max_length=50)
    product_price = models.IntegerField()
    old_price = models.IntegerField(default=None, null=True,)
    product_description = models.TextField(null=True,)
    product_img = models.ImageField(upload_to ='photos/%Y/%m/%d/',blank=True)
    photo_1 = models.ImageField(upload_to ='photos/%Y/%m/%d/',blank=True)
    photo_2 = models.ImageField(upload_to ='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to ='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to ='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to ='photos/%Y/%m/%d/', blank=True)