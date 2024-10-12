from rest_framework import serializers
from . models import *
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']

class ArtistSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    class Meta:
        model = Artist
        fields = ['name', 'genre', 'products']

class GearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gear
        fields = ['sku', 'asn', 'category', 'online', 'item_name', 'title', 'brand_name', 'description', 'productDetail', 'price', 'picture_main', 'quantity_in_stock', 'quantity_on_order', 'color_option', 'pickup_option', 'shape_option', 'created_at', 'image_urls', 'rating', 'glasgow_quantity', 'edinburgh_quantity', 'newcastle_quantity']