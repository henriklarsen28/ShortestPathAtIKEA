import streamlit as st
import pandas as pd



st.title("Upload Example")
file = st.file_uploader("Upload file", type=["csv", "txt","json"])
if file:
    shoppingList = pd.read_json(file)
    st.write(shoppingList)