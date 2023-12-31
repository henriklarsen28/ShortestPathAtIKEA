import numpy as np
import streamlit as st
import pandas as pd
import json
from Graph.map import *


def addToCart(item):
    for cartItem in st.session_state.cart:
        if cartItem["name"] == item["name"]:
            cartItem["amount"] += 1
            cartItem["total"] = cartItem["amount"] * cartItem["price"]
            return

    # Build item dictionary
    newItem = {
        "name": item["name"],
        "amount": 1,
        "price": item["price"],
        "total": item["price"],
        "selfServe": item["self_serve"],
        "location": item["location"],
        "aile": item["aile"],
        "bin": item["bin"],
    }
    st.session_state.cart.append(newItem)

def removeFromCart(removeItem):
    for item in st.session_state.cart:
        if item["name"] == removeItem["name"]:
            item["amount"] -= 1
            item["total"] = item["amount"] * item["price"]

            # Remove item if new amount is 0
            if item["amount"] == 0:
                st.session_state.cart.remove(item)
                return

            return
    return "Item not found"

def getImage(list, index):
    try:
        return list[index]["image"]
    except:
        return "Not found"

# Set the page layout
st.set_page_config(layout="wide")
st.title("Upload Example")

# Session state
#"st.session_state object: ", st.session_state

if "cart" not in st.session_state:
    st.session_state.cart = []




# Read the json file
file = open("Products/products.json", "r", encoding="utf-8")
productList = file.read()
jsonList = json.loads(productList)

# Create the columns
col1,col2,col3 = st.columns([1,1,1])

with(col1):
    st.subheader(jsonList[0]["name"])
    st.markdown(f'<img src="{jsonList[0]["image"]}" alt="cat" width="350" height=350>', unsafe_allow_html=True)
    if st.button("Add to cart",key="0"):
        addToCart(jsonList[0])
    if(st.button("Remove from cart", key="remove0")):
        removeFromCart(jsonList[0])

with(col2):
    st.subheader(jsonList[1]["name"])
    st.markdown(f'<img src="{getImage(jsonList,1)}" alt="cat" width="350">', unsafe_allow_html=True)
    if st.button("Add to cart", key="1"):
        addToCart(jsonList[1])
    if(st.button("Remove from cart", key="remove1")):
        removeFromCart(jsonList[1])

with(col3):
    st.subheader(jsonList[7]["name"])
    st.markdown(f'<img src="{getImage(jsonList,7)}" alt="cat" width="350">', unsafe_allow_html=True)
    if st.button("Add to cart",key=7):
        addToCart(jsonList[7])
    if(st.button("Remove from cart", key="remove7")):
        removeFromCart(jsonList[7])


data = pd.DataFrame(st.session_state.cart)
st.table(data)

# Calculate the fastest route send cart into maptest.py
graph, G = makeGraph()
if(st.button("Calculate fastest route", key="aStar")):
    path, length = aStarCalculations(G, "Entrance", "Exit", st.session_state.cart)

    # Convert array to string and format it
    path = np.asarray(path)
    path = np.array2string(path,separator=" -> ")
    path = path.replace("[","")
    path = path.replace("]","")
    path = path.replace("'","")

    st.text(f"The fastest route is: {path}, and you will walk {length} meters")


st.pyplot(graph)


