import requests
import json
import csv

url = "https://www.guitarguitar.co.uk/hackathon/products"
response = requests.get(url).text
json_data = json.loads(response)

with open("output.csv", mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['sku', 'asn',"category","online","itemName","title","brandName","description","salesPrice","pictureMain","qtyInStock","colour","pickup","bodyShape","createdOn","imageUrls","rating","glasgowQty","edinburghQty","newcastleQty"])
    
    for row in json_data:
        if row["ProductDetail"]:
            del row["ProductDetail"]
    
    for row in json_data:
        writer.writerow(row.values())