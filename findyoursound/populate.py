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
        
        """need:
        image
        title
        price"""
        
    extras = [
        {
            'sku' : '180430326802008', # Billy from Smashing Pumpkins
            'item_name' : 'Fender Player Stratocaster Buttercream Maple Fingerboard',
            'price' : "659.00",
            'image_urls' : "https://images.guitarguitar.co.uk/cdn/large/150/180430326802008f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70",
            
        },{
            'sku' : '04122311202218', # Billy from Smashing Pumpkins
            'item_name' : 'Electro Harmonix Big Muff Pi',
            'price' : "89.00",
            'image_urls' : "https://images.guitarguitar.co.uk/cdn/large/170/04122311202218f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70",
            
        },{
            'sku' : '240717426967008', # jazz guitar
            'item_name' : 'Ibanez PM3C Pat Metheny Signature Natural Amber Low Gloss',
            'price' : "1399.00",
            'image_urls' : "https://images.guitarguitar.co.uk/cdn/large/170/240717426967008f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70",
            
        },{
            'sku' : '190319340838008', # ACDC Guitar
            'item_name' : 'Gibson SG Standard Heritage Cherry',
            'price' : "1399.00",
            'image_urls' : "https://images.guitarguitar.co.uk/cdn/large/150/190319340838008f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70",
            
        },
        {
            'sku' : '240430423245008', # Mettalica Guitar
            'item_name' : 'Epiphone Inspired by Gibson Custom Jimi Hendrix Love Drops Flying V',
            'price' : "1,499.00",
            'image_urls' : "https://images.guitarguitar.co.uk/cdn/large/170/240430423245008f.jpg",
            
        }
    ]
    
    for row in extras:
        Gear.objects.get_or_create(**row)
        
    

def addArtist():
    
    artists = [
        {
            'name' : 'The Smashing Pumpkins',
            'genre' : Genre.objects.get(name = "Rock"),
            'products' : Gear.objects.get(sku = "180430326802008")
        },
        {
            'name' : 'AC/DC',
            'genre' : Genre.objects.get(name = "Rock"),
            'products' : Gear.objects.get(sku = "190319340838008")
        },
        {
            'name' : 'Taylor Swift',
            'genre' : Genre.objects.get(name = "Pop"),
            'products' : Gear.objects.get(sku = "190718346269008")
        },
        {
            'name' : 'John Williams',
            'genre' : Genre.objects.get(name = "Classical"),
            'products' : Gear.objects.get(sku = "09071411013328")
        },
        {
            'name' : 'Pat Metheny',
            'genre' : Genre.objects.get(name = "Jazz"),
            'products' : Gear.objects.get(sku = "240717426967008")
        },
        {
            'name' : 'Mettalica',
            'genre' : Genre.objects.get(name = "Metal"),
            'products' : Gear.objects.get(sku = "240430423245008")
        }
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
        },
        {
            'name': 'Metal'
        }

    ]
    for genre in genres:
        Genre.objects.get_or_create(**genre)
    
    
    

    
if __name__ == '__main__':
    print('Starting Django population script...')
    populate()
