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
    return json_data

def populate():
    addGear(getJSON())
        
        
def addGear(data):
    for row in data:
        Gear.objects.get_or_create(**row)

def addArtist():
    pass

def addGenre():
    pass
    
    
    
    
    

    
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
