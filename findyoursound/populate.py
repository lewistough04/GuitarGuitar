import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'findyoursound.settings')
import requests
import json
import csv
import django
django.setup()
from music.models import Gear, Artist, Genre

def getJSON():

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

    field_mapping = dict(zip(oldFieldNames, newFieldNames))

    transformed_data = []
    for item in json_data:
        new_item = {field_mapping[old_key]: value for old_key, value in item.items() if old_key in field_mapping}
        transformed_data.append(new_item)
    json_data = transformed_data


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
            'category' : 'GUEG',
            'price' : 659.00,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/150/180430326802008f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70",
            
        }, {
            'sku' : '230126399454008', # Nirvana Guitar
            'item_name' : 'Squier Sonic Mustang 2 Tone Sunburst Maple Fingerboard',
            'category' : 'GUEG',
            'price' : 159.00,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/170/230126399454008f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70",
            
        },{
            'sku' : '190110337350008',
            'item_name' : 'Squier Classic Vibe 70s Jaguar 3 Tone Sunburst Indian Laurel Fingerboard',
            'category' : 'GUEG',
            'price' : 389.00,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/150/190110337350008f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70",
            
        },{
            'sku' : '13122413470032',
            'item_name' : 'Fender Kurt Cobain Jaguar 3 Colour Sunburst NOS Rosewood Fingerboard',
            'category' : 'GUEG',
            'price' : 1379.00,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/160/13122413470032f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70",
            
        },{
            'sku' : '07080112173928', # The Beatles Guitar
            'item_name' : 'Epiphone Casino Vintage Sunburst',
            'category' : 'GUEG',
            'price' : 629.00,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/170/07080112173928f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70",
        },{
            'sku' : '170705312155008', # ABBA Guitar
            'item_name' : 'Hagstrom Fantomen White Gloss',
            'category' : 'GUEG',
            'price' : 749.00,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/150/170705312155008f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70"
            },
        {
            'sku' : '220614387522008',
            'item_name' : 'Epiphone Noel Gallagher Riviera',
            'category' : 'GUEG',
            'price' : 799.00,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/170/220614387522008f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70"
            },
        
        { # Jazz
            'sku' : '240717426967008', # jazz guitar
            'item_name' : 'Ibanez PM3C Pat Metheny Signature Natural Amber Low Gloss',
            'category' : 'GUEG',
            'price' : 1399.00,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/170/240717426967008f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70",
            
        },{
            'sku': '240805427735020',
            'item_name': 'Fender Limited Edition Player Stratocaster Pau Ferro Fingerboard Black with Custom Shop Pickups',
            'category': 'GUBA',
            'price': 599.00,
            'picture_main': "https://images.guitarguitar.co.uk/cdn/large/170/240805427735020f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70"
            },
        {
            'sku' : '190319340838008', # ACDC Guitar
            'item_name' : 'Gibson SG Standard Heritage Cherry',
            'category' : 'GUEG',
            'price' : 1399.00,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/150/190319340838008f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70",
            
        },
        { # Metal
            'sku' : '240430423245008', # Mettalica Guitar
            'item_name' : 'Epiphone Inspired by Gibson Custom Jimi Hendrix Love Drops Flying V',
            'category' : 'GUEG',
            'price' : 1499.00,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/170/240430423245008f.jpg",
            
        },{ 
            'sku' : '221201397184008', # Polyphia Guitar
            'item_name' : 'Ibanez TOD10 Tim Henson Signature',
            'category' : 'GUEG',
            'price' : 1469.00,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/170/221201397184008f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70",
        },{
            'sku' : '191204352060008', # Van Halen Guitar
            'item_name' : 'EVH Striped Series Frankie',
            'category' : 'GUEG',
            'price' : 1199.00,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/150/191204352060008f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70"
        },
        {
            'sku' : '191216352722008',
            'item_name' : 'Gibson Custom Shop 1959 ES-355 Reissue Stop Bar VOS Ebony',
            'category' : 'GUEG',
            'price' : 5649.00,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/170/191216352722008f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70"
        },
        #acoustic guitars
        {
            'sku' : '191216352602008', 
            'item_name' : 'Epiphone Masterbilt Texan Antique Natural Aged Gloss',
            'category' : 'GUAG',
            'price' : 799.00,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/160/191216352602008f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70"
        },

        {
            'sku' : '210111365922025', 
            'item_name' : 'Gibson Hummingbird Standard Vintage Sunburst',
            'category' : 'GUAG',
            'price' : 3199.00,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/170/210111365922025f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70"
        },
        {
            'sku' : '220803390407008', 
            'item_name' : 'Gibson Hummingbird Faded Antique Natural',
            'category' : 'GUAG',
            'price' : 2949.00,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/170/220803390407008f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70"
        },
        # bass

        {
            'sku' : '04042010374818', # beatles bass
            'item_name' : 'Epiphone Viola Short Scale Bass Vintage Sunburst',
            'category' : 'GUBA',
            'price' : 349.00,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/130/04042010374818f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70"
        },

        {
            'sku' : '15012010412032',
            'item_name' : 'Rickenbacker 4003S Jetglo',
            'category' : 'GUBA',
            'price' : 2499.00,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/170/15012010412032f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70"
        },

        {
            'sku' : '200723360507025',
            'item_name' : 'Fender American Professional II Jazz Bass 3 Tone Sunburst Rosewood Fingerboard',
            'category' : 'GUBA',
            'price' : 1599.00,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/160/200723360507025f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70"
        },

        {
            'sku' : '190110337359008',
            'item_name' : 'Squier Classic Vibe 60s Jazz Bass 3 Tone Sunburst Indian Laurel Fingerboard',
            'category' : 'GUBA',
            'price' : 389.00,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/150/190110337359008f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70"
        },
         {
            'sku' : '200723360490025',
            'item_name' : 'Fender American Professional II Precision Bass 3 Tone Sunburst Rosewood Fingerboard',
            'category' : 'GUBA',
            'price' : 1599.00,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/160/200723360490025f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70"
        },
        # Pedals
        {
            'sku' : '04122311202218',
            'item_name' : 'Electro Harmonix Big Muff Pi',
            'category' : 'PEDL',
            'price' : 89.00,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/170/04122311202218f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70",
        },
        {
            'sku' : '04052410171618',
            'item_name' : 'BOSS DS-1 Distortion Pedal',
            'category' : 'PEDL',
            'price' : 63.00,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/150/04052410171618f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70",
        },

        {
            'sku' : '211012375294025',
            'item_name' : 'BOSS RC-600 Loop Station',
            'category' : 'PEDL',
            'price' : 459.00,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/170/211012375294025f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70",
        },
        {
            'sku' : '200930362584025',
            'item_name' : 'BOSS RC-500 Loop Station',
            'category' : 'PEDL',
            'price' : 269.00,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/160/200930362584025f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70",
        },
        # Amps
        {
            'sku' : '180625328945008',
            'item_name' : 'Vox AC30S1 1x12 Combo',
            'category' : 'AMP',
            'price' : 629.00,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/170/180625328945008f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70",
        },
        {
            'sku' : '10012109542729',
            'item_name' : 'Vox AC30C2 2x12 Combo Valve Amp',
            'category' : 'AMP',
            'price' : 949.00,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/170/10012109542729f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70",
        },

        {
            'sku' : '04061716510318',
            'item_name' : 'Marshall 1960A 4x12 Guitar Cabinet',
            'category' : 'AMP',
            'price' : 589.00,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/170/04061716510318f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70",
        },
        {
            'sku' : '210623370758025',
            'item_name' : 'EVH 5150 Iconic 40W 1x12 Combo Valve Amp Ivory',
            'category' : 'AMP',
            'price' : 659.00,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/170/210623370758025f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70",
        },
        {
            'sku' : '230126399351025',
            'item_name' : 'EVH 5150 Iconic 15W Black Combo Valve Amp',
            'category' : 'AMP',
            'price' : 499.00,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/170/230126399351025f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70",
        },
        # Cables
        {
            'sku' : '190125338539008',
            'item_name' : 'Fender Professional Series 10ft Straight Instrument Cable, Black',
            'category' : 'ACC',
            'price' : 15.99,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/150/190125338539008f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70"
        },
        {
            'sku' : '220302382224027',
            'item_name' : 'Ordo 10ft/3m Angled Instrument Cable',
            'category' : 'ACC',
            'price' : 12.99,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/170/220302382224027f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70"
        },


        #capos
        {
            'sku' : '221031395730025',
            'item_name' : 'Dunlop Trigger Fly Capo Gun Metal',
            'category' : 'ACC',
            'price' : 19.99,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/170/221031395730025f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70"
        },
        {
            'sku' : '13040811470467',
            'item_name' : 'Shubb Capo C1 Nickel Steel String',
            'category' : 'ACC',
            'price' : 24.99,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/120/13040811470467f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70"
        },

        # Picks
        {
            'sku' : '11051614363558',
            'item_name' : 'Dunlop 471P3N Nylon Max Grip Jazz III Nylon 6/Play Pack',
            'category' : 'ACC',
            'price' : 5.99,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/160/11051614363558.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70"
        },
        {
            'sku' : '210120366173025',
            'item_name' : 'Dunlop EVH 5150 Max Grip Picks Pack of 6',
            'category' : 'ACC',
            'price' : 11.99,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/170/210120366173025f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70"
        },

        # gig bags
        {
            'sku' : '220302382176027',
            'item_name' : 'Ordo B-215-BG Premium 15mm Electric Bass Guitar Gig Bag',
            'category' : 'ACC',
            'price' : 49.99,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/170/220302382176027f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70"
        },
        # strings
        {
            'sku' : '05020915553318',
            'item_name' : 'DAddario EJ46 Pro Arte High Tension Classical Strings',
            'category' : 'ACC',
            'price' : 14.99,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/150/05020915553318f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70"
        },
        # percussion
        {
            'sku' : '240904429060027',
            'item_name' : 'Chord Tambourines Single D Black',
            'category' : 'ACC',
            'price' : 13.99,
            'picture_main' : "https://images.guitarguitar.co.uk/cdn/large/150/05020915553318f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70"
        },




    ]
    
    for row in extras:
        Gear.objects.get_or_create(**row)
        
    

def addArtist():
    
    artists = [
        {
            # Rock
            'name' : 'The Smashing Pumpkins',
            'genre' : Genre.objects.get(name = "Rock"),
            'products' : ["180430326802008", "04122311202218"]
        },
        {
            'name' : 'AC/DC',
            'genre' : Genre.objects.get(name = "Rock"),
            'products' : ["190319340838008", "04061716510318"]
        },{
            'name' : 'Nirvana',
            'genre' : Genre.objects.get(name = "Rock"),
            'products' : ["230126399454008", "04052410171618", "190110337350008", "13122413470032", "180625328945008", "10012109542729"]
        },{
            'name' : 'Oasis',
            'genre' : Genre.objects.get(name = "Rock"),
            'products' : ["240904429060027", "13040811470467", "221031395730025", "220614387522008", "191216352722008", "180625328945008", "10012109542729", "220803390407008"]
        },
        {   # Pop -------------------------------------------------------
            'name' : 'Taylor Swift',
            'genre' : Genre.objects.get(name = "Pop"),
            'products' : ["190718346269008", "210111365922025"]
        },{
            'name' : 'Ed Sheeran',
            'genre' : Genre.objects.get(name = "Pop"),
            'products' : ["08082816154628", "211012375294025", "200930362584025"]
        },{
            'name' : 'The Beatles',
            'genre' : Genre.objects.get(name = "Pop"),
            'products' : ["07080112173928", "04042010374818","220302382176027","15012010412032", "191216352602008"]
        },{
            'name' : 'ABBA',
            'genre' : Genre.objects.get(name = "Pop"),
            'products' : ["170705312155008", "200723360507025", "190110337359008"]
        },
        
        {   # Classical --------------------------------------------------
            'name' : 'John Williams',
            'genre' : Genre.objects.get(name = "Classical"),
            'products' : ["09071411013328", "05020915553318"]
        },{  # Jazz --------------------------------------------------------
            'name' : 'Pat Metheny',
            'genre' : Genre.objects.get(name = "Jazz"),
            'products' : ["240717426967008"]
        },{
            'name' : 'Vulfpeck',
            'genre' : Genre.objects.get(name = "Jazz"),
            'products' : ["200723360507025", '240805427735020']
            },
        { # Metal --------------------------------------------------------
            'name' : 'Metallica',
            'genre' : Genre.objects.get(name = "Metal"),
            'products' : ["240430423245008"]
        },{
            'name' : 'Black Sabbath',
            'genre' : Genre.objects.get(name = "Metal"),
            'products' : ["190319340838008", "200723360490025"]
        },{
            'name': 'Polyphia',
            'genre': Genre.objects.get(name = "Metal"),
            'products': ["221201397184008"],
        },{
            'name': 'Van Halen',
            'genre': Genre.objects.get(name = "Metal"),
            'products': ["191204352060008", "210120366173025", "210623370758025", "230126399351025"]
        }  
    ]
    
    
    for artist_data in artists:
        # Get or create the artist
        artist, created = Artist.objects.get_or_create(
            name=artist_data['name'],
            genre=artist_data['genre']
        )
        # Add products to the artist (multiple products now allowed)
        for sku in artist_data['products']:
            product = Gear.objects.get(sku=sku)
            artist.products.add(product)

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
