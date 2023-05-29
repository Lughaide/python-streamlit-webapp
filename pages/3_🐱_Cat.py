import streamlit as st
from scripts.api_func import load_img_arr_from_api

st.title("A random cat image getter")

if st.button(label="Get Cat :cat:"):
    img_arr = load_img_arr_from_api("https://cataas.com/cat")
    st.image(img_arr)
    st.write("This is a cat")