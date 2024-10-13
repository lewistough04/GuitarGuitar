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
    "picture_main",
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
        { # Rock
            'sku' : '180430326802008', # Billy from Smashing Pumpkins
            'item_name' : 'Fender Player Stratocaster Buttercream Maple Fingerboard',
            'price' : 659.00,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/150/180430326802008f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70",
            
        }, {
            'sku' : '230126399454008', # Nirvana Guitar
            'item_name' : 'Squier Sonic Mustang 2 Tone Sunburst Maple Fingerboard',
            'price' : 159.00,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/170/230126399454008f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70",
            
        }, { # Pop
            
            'sku': '08082816154628', # Ed Sheeran Guitar,
            'item_name': 'Martin LX1E Little Martin',
            'price': 515.00,
            'picture_main': 'https://images.guitarguitar.co.uk/cdn/large/170/08082816154628f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70',
        }, {
            'sku' : '07080112173928', # The Beatles Guitar
            'item_name' : 'Epiphone Casino Vintage Sunburst',
            'price' : 629.00,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/170/07080112173928f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70",
        },{
            'sku' : '170705312155008', # ABBA Guitar
            'item_name' : 'Hagstrom Fantomen White Gloss',
            'price' : 749.00,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/150/170705312155008f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70"
            },
        
        
        
        {
            'sku' : '04122311202218', # Billy from Smashing Pumpkins
            'item_name' : 'Electro Harmonix Big Muff Pi',
            'price' : 89.00,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/170/04122311202218f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70",
            
        },{ # Jazz
            'sku' : '240717426967008', # jazz guitar
            'item_name' : 'Ibanez PM3C Pat Metheny Signature Natural Amber Low Gloss',
            'price' : 1399.00,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/170/240717426967008f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70",
            
        },{
            'sku' : '190319340838008', # ACDC Guitar
            'item_name' : 'Gibson SG Standard Heritage Cherry',
            'price' : 1399.00,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/150/190319340838008f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70",
            
        },
        { # Metal
            'sku' : '240430423245008', # Mettalica Guitar
            'item_name' : 'Epiphone Inspired by Gibson Custom Jimi Hendrix Love Drops Flying V',
            'price' : 1499.00,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/170/240430423245008f.jpg",
            
        },{ 
            'sku' : '221201397184008', # Polyphia Guitar
            'item_name' : 'Ibanez TOD10 Tim Henson Signature',
            'price' : 1469.00,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/170/221201397184008f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70",
        },{
            'sku' : '191204352060008', # Van Halen Guitar
            'item_name' : 'EVH Striped Series Frankie',
            'price' : 1199.00,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/150/191204352060008f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70"
        }
    ]
    
    for row in extras:
        Gear.objects.get_or_create(**row)
        
    

def addArtist():
    
    artists = [
        {
            # Rock
            'name' : 'The Smashing Pumpkins',
            'genre' : Genre.objects.get(name = "Rock"),
            'products' : Gear.objects.get(sku = "180430326802008")
        },
        {
            'name' : 'AC/DC',
            'genre' : Genre.objects.get(name = "Rock"),
            'products' : Gear.objects.get(sku = "190319340838008")
        },{
            'name' : 'Nirvana',
            'genre' : Genre.objects.get(name = "Rock"),
            'products' : Gear.objects.get(sku = "230126399456008")
        },
        {   # Pop -------------------------------------------------------
            'name' : 'Taylor Swift',
            'genre' : Genre.objects.get(name = "Pop"),
            'products' : Gear.objects.get(sku = "190718346269008")
        },{
            'name' : 'Ed Sheeran',
            'genre' : Genre.objects.get(name = "Pop"),
            'products' : Gear.objects.get(sku = "08082816154628")
        },{
            'name' : 'The Beatles',
            'genre' : Genre.objects.get(name = "Pop"),
            'products' : Gear.objects.get(sku = "07080112173928")
        },{
            'name' : 'ABBA',
            'genre' : Genre.objects.get(name = "Pop"),
            'products' : Gear.objects.get(sku = "170705312155008")
        },
        
        {   # Classical --------------------------------------------------
            'name' : 'John Williams',
            'genre' : Genre.objects.get(name = "Classical"),
            'products' : Gear.objects.get(sku = "09071411013328")
        },{  # Jazz --------------------------------------------------------
            'name' : 'Pat Metheny',
            'genre' : Genre.objects.get(name = "Jazz"),
            'products' : Gear.objects.get(sku = "240717426967008")
        },{ # Metal --------------------------------------------------------
            'name' : 'Mettalica',
            'genre' : Genre.objects.get(name = "Metal"),
            'products' : Gear.objects.get(sku = "240430423245008")
        },{
            'name' : 'Black Sabbath',
            'genre' : Genre.objects.get(name = "Metal"),
            'products' : Gear.objects.get(sku = "190319340838008")
        },{
            'name': 'Polyphia',
            'genre': Genre.objects.get(name = "Metal"),
            'products': Gear.objects.get(sku ="221201397184008"),
        },{
            'name': 'Van Halen',
            'genre': Genre.objects.get(name = "Metal"),
            'products': Gear.objects.get(sku ="191204352060008"),
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
