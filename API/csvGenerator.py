import requests
import json
import csv

url = "https://www.guitarguitar.co.uk/hackathon/products"
response = requests.get(url).text
json_data = json.loads(response)

print(json_data[2])