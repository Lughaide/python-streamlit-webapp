import streamlit as st
import os

from scripts.api_func import get_data_from_api, load_page

load_page(__file__)

DOG_IMG_URL = "https://dog.ceo/api/breeds/image/random"
DOG_FACT_URL = "https://dogapi.dog/api/v2/facts"

st.title("A random dog image getter")

if st.button(label="Get Dog :dog:"):
    data_load_state = st.text("Grabbing image...")

    img_url = get_data_from_api(DOG_IMG_URL)["message"]
    fact_data = get_data_from_api(DOG_FACT_URL)["data"][0]["attributes"]["body"]

    st.write(img_url)
    st.image(image=img_url, caption="A dog.")
    st.write(fact_data)
    
    data_load_state.text("")