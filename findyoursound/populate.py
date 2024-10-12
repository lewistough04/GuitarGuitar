import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'findyoursound.settings')

import django
django.setup()
from music.models import Gear, Artist, Genre

def getJSON():
    import requests
    import json
    import csv

    url = "https://www.guitarguitar.co.uk/hackathon/products"
    response = requests.get(url).text
    json_data = json.loads(response)
    oldFieldNames = [
    'SKU_ID',
    'ASN',
    'Category',
    'Online',
    'ItemName',
    'Title',
    'BrandName',
    'Description',
    'SalesPrice',
    'PictureMain',
    'QtyInStock',
    'QtyOnOrder',
    'Colour',
    'Pickup',
    'BodyShape',
    'CreatedOn',
    'ImageUrls',
    'Rating',
    'GlasgowQty',
    'EdinburghQty',
    'NewcastleQty'
    ]

    newFieldNames = [
    "sku",
    "asn",
    "category",
    "online",
    "item_name",
    "title",
    "brand_name",
    "description",
    "price",
    "picture_main",
    "quantity_in_stock",
    "quantity_on_order",
    "color_option",
    "pickup_option",
    "shape_option",
    "created_at",
    "image_urls",
    "rating",
    "glasgow_quantity",
    "edinburgh_quantity",
    "newcastle_quantity"
    ]

    for i in range(0, len(json_data)):
        del json_data[i]['ProductDetail']
        for j in range(0, len(oldFieldNames)):
            json_data[i][newFieldNames[j]] = json_data[i][oldFieldNames[j]]
            del json_data[i][oldFieldNames[j]]


    return json_data

def populate():
    addGear(getJSON())
    addGenre()
    addArtist()
        
        
def addGear(data):

    for row in data:
        Gear.objects.get_or_create(**row)
        
        """image
        title
        price"""
        
    extras = [
        {
            'sku' : '180430326802008',
            'item_name' : 'Fender Player Stratocaster Buttercream Maple Fingerboard',
            'price' : "659.00",
            'image_urls' : "https://images.guitarguitar.co.uk/cdn/large/150/180430326802008f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70",
            
        },
    ]
    
    for row in extras:
        Gear.objects.get_or_create(**row)
        
    
    
        
    
        
    

def addArtist():
    
    artists = [
        {
            'name' : 'The Smashing Pumpkins',
            'genre' : Genre.objects.get(name = "Rock"),
            'products' : Gear.objects.get(sku = "180430326802008")
        }#,
        # {
        #     'name' : 'Taylor Swift'
        # },
        # {
        #     'name' : 'John Williams'
        # },
        # {
        #     'name' : 'Lewis Tough'
        # }
    ]
    for artist in artists:
        Artist.objects.get_or_create(**artist)

def addGenre():
    genres= [
        {
            'name': 'Rock'
        },
        {
            'name': 'Pop'
        },
        {
            'name': 'Classical'
        },
        {
            'name': 'Jazz'
        }

    ]
    for genre in genres:
        Genre.objects.get_or_create(**genre)
    
    
    

    
if __name__ == '__main__':
    print('Starting Django population script...')
    populate()
