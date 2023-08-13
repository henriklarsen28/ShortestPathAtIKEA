import streamlit as st
import pandas as pd
import json


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
file = open("products.json", "r",encoding="utf-8")
productList = file.read()
jsonList = json.loads(productList)

# Create the columns
col1,col2,col3 = st.columns([1,1,1])

with(col1):
    st.subheader(jsonList[0]["name"])
    st.markdown(f'<img src="{jsonList[0]["image"]}" alt="cat" width="350" height=350>', unsafe_allow_html=True)
    if st.button("Add to cart",key="0"):
        st.session_state.cart.append(jsonList[0])

with(col2):
    st.subheader(jsonList[1]["name"])
    st.markdown(f'<img src="{getImage(jsonList,7)}" alt="cat" width="350">', unsafe_allow_html=True)
    if st.button("Add to cart", key="1"):
        st.session_state.cart.append(jsonList[1])

with(col3):
    st.subheader(jsonList[7]["name"])
    st.markdown(f'<img src="{getImage(jsonList,7)}" alt="cat" width="350">', unsafe_allow_html=True)
    if st.button("Add to cart",key=7):
        st.session_state.cart.append(jsonList[7])

data = pd.DataFrame(st.session_state.cart)
st.table(data)


# Persist data from dataframe
