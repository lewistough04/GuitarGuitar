from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Artist(models.Model):
    name = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, related_name='artists', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Gear(models.Model):
    artists = models.ManyToManyField(Artist, related_name='gears') #Many to many relationship with Artist
    sku = models.CharField(max_length=100)
    asn = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    online = models.BooleanField()
    item_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)            #Title for the item (deals etc)
    brand_name = models.CharField(max_length=100)
    description = models.TextField()
    productDetail = models.TextField()
    price = models.FloatField()
    picture_main = models.TextField()
    quantity_in_stock = models.IntegerField()
    quantity_on_order = models.IntegerField()
    color_option = models.IntegerField()
    pickup_option = models.IntegerField()
    shape_option = models.IntegerField()
    created_at = models.DateTimeField()    #Date and time of the product added to guitar guitar api database
    image_urls = models.TextField()
    rating = models.FloatField()
    glasgow_quantity = models.IntegerField()
    edinburgh_quantity = models.IntegerField()
    newcastle_quantity = models.IntegerField()
    #If the 3 store stock quantities are 0, but there’s still some in QtyInStock, we just have some in the warehouse.

    def __str__(self):
        return self.name