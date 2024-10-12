from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name
    

class Gear(models.Model):
    sku = models.CharField(max_length=100)
    asn = models.CharField(max_length=100, null = True, blank = True)
    category = models.CharField(max_length=100, null = True, blank = True)
    online = models.BooleanField(null = True, blank = True)
    item_name = models.CharField(max_length=100, null = True, blank = True)
    title = models.CharField(max_length=100, null = True, blank = True)            #Title for the item (deals etc)
    brand_name = models.CharField(max_length=100, null = True, blank = True)
    description = models.TextField(null = True, blank = True)
    productDetail = models.TextField(null = True, blank = True)
    price = models.FloatField(null = True, blank = True)
    picture_main = models.TextField(null = True, blank = True)
    quantity_in_stock = models.IntegerField(null = True, blank = True)
    quantity_on_order = models.IntegerField(null = True, blank = True)
    color_option = models.IntegerField(null = True, blank = True)
    pickup_option = models.IntegerField(null = True, blank = True)
    shape_option = models.IntegerField(null = True, blank = True)
    created_at = models.TextField(null = True, blank = True)    #Date and time of the product added to guitar guitar api database
    image_urls = models.TextField(null = True, blank = True)
    rating = models.FloatField(null = True, blank = True)
    glasgow_quantity = models.IntegerField(null = True, blank = True)
    edinburgh_quantity = models.IntegerField(null = True, blank = True)
    newcastle_quantity = models.IntegerField(null = True, blank = True)
    #If the 3 store stock quantities are 0, but there’s still some in QtyInStock, we just have some in the warehouse.

    def __str__(self):
        return self.sku

class Artist(models.Model):
    name = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, related_name='artists', on_delete=models.CASCADE)
    products = models.ForeignKey(Gear, related_name='uses', null=True, on_delete=models.SET_NULL)
    band = models.CharField(max_length=100, null = True, blank = True)
    def __str__(self):
        return self.name