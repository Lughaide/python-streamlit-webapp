import streamlit as st
from scripts.api_func import get_data_from_api

CAT_IMG_URL = "https://cataas.com/cat"

st.title("A random cat image getter")

if st.button(label="Get Cat :cat:"):
    data_load_state = st.text("Grabbing image...")
    
    img_arr = get_data_from_api(CAT_IMG_URL, is_json=False)

    st.image(img_arr)
    st.write("This is a cat")

    data_load_state.text("")