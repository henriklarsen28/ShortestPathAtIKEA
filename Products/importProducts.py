import requests
import json
from jsonpath_ng import jsonpath, parse
import random as rd


def getProducts(data):
    productList = []
    for i in range(30):
        # Adds products from API to array
        try:
            productName = data["productListPage"]["productWindow"][i]["name"]
            productPrice = data["productListPage"]["productWindow"][i]["gprDescription"]["variants"][0]["salesPrice"][
                "numeral"]
            type = data["productListPage"]["category"]["name"]
            description = data["productListPage"]["productWindow"][i]["typeName"] + " " + \
                          data["productListPage"]["productWindow"][i]["itemMeasureReferenceText"]

            # Random aile and bin
            aile = round(rd.random() * 10 + 1)
            bin = round(rd.random() * 10 + 1)

            product = {
                "name": productName,
                "price": productPrice,
                "type": type,
                "description": description,
                "self_serve": True,
                "aile": aile,
                "bin": bin
            }

            if product["name"] not in [item["name"] for item in productList]:
                productList.append(product)

        except:
            pass

    return productList


url_list = [
    "https://sik.search.blue.cdtapps.com/no/no/product-list-page?category=10412&size=24&c=lf&v=20220826&sort=RELEVANCE&zip=0375&sessionId=6109003e-64d6-4660-a561-c59ada6b5158&optimizelyUserId=60b37688-76ae-4ea6-b7fd-43aadba3db09", ]

# Collects the different products from the API
for url in url_list:
    response = requests.get(
        "https://sik.search.blue.cdtapps.com/no/no/product-list-page?category=10412&size=24&c=lf&v=20220826&sort=RELEVANCE&zip=0375&sessionId=6109003e-64d6-4660-a561-c59ada6b5158&optimizelyUserId=60b37688-76ae-4ea6-b7fd-43aadba3db09")

    response_json = response.json()

    productList = getProducts(response_json)

    print(productList)

    # Opens the file and writes the products to it
    file = open("products.json", "r+", encoding="utf-8")

    with open("products.json", "r+", encoding="utf-8") as file:
        if len(file.read()) > 0:
            json_data = json.load(file)
            print(json_data)
            # productList.append(json_data)

    json_string = json.dumps(productList, ensure_ascii=False)
    print(json_string)
    file.write(json_string)
