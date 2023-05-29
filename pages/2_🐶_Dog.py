import streamlit as st

from scripts.api_func import *

DOG_IMG_URL = "https://dog.ceo/api/breeds/image/random"
DOG_FACT_URL = "https://dogapi.dog/api/v2/facts"
st.title("A random dog image getter")

if st.button(label="Get Dog :dog:"):
    data_load_state = st.text("Grabbing image...")
    img_url = load_img_from_api(DOG_IMG_URL)
    fact_data = load_fact_from_api(DOG_FACT_URL)
    st.write(img_url)
    st.image(image=img_url, caption="A dog.")
    data_load_state.text("")
    st.write(fact_data)