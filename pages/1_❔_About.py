import streamlit as st
import streamlit.components.v1 as components

import pandas as pd
import numpy as np

from scripts.api_func import *

load_page(__file__)

st.title("Hello World")

st.write("This is a misc web application, written in Streamlit. It can do cool things like:")

tabs = st.tabs(["About", "Dog", "Cat", "Hilite", "QR", "ProfanityFilter"])

with tabs[0]:
    df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])

    st.map(df)

    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=["a", "b", "c"])

    st.bar_chart(chart_data)

    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

with tabs[1]:
    exec(open("./pages/2_🐶_Dog.py").read())

with tabs[2]:
    exec(open("./pages/3_🐱_Cat.py").read())

with tabs[3]:
    exec(open("./pages/4_#️⃣_Hilite.py").read())

with tabs[4]:
    exec(open("./pages/5_🔢_QR.py").read())

with tabs[5]:
    exec(open("./pages/6_😡_ProfanityFilter.py").read())