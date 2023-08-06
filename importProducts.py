import requests
import json
from jsonpath_ng import jsonpath, parse

response = requests.get("https://sik.search.blue.cdtapps.com/no/no/product-list-page?category=10412&size=24&c=lf&v=20220826&sort=RELEVANCE&zip=0375&sessionId=6109003e-64d6-4660-a561-c59ada6b5158&optimizelyUserId=60b37688-76ae-4ea6-b7fd-43aadba3db09")

json = response.json()

data = json
#print(data)

file = open("products.json", "w")


productList = []

for i in range(30):
    # Adds products from API to array
    try:
        productName = data["productListPage"]["productWindow"][i]["name"]
        productPrice = data["productListPage"]["productWindow"][i]["gprDescription"]["variants"][0]["salesPrice"]["numeral"]
        type = data["productListPage"]["category"]["name"]
        description = data["productListPage"]["productWindow"][i]["typeName"] + " " + data["productListPage"]["productWindow"][i]["itemMeasureReferenceText"]

        product = {
            "name": productName,
            "price": productPrice,
            "type": type,
            "description": description
        }


        if product["name"] not in [item["name"] for item in productList]:
            productList.append(product)

    except:
        pass

print(productList)