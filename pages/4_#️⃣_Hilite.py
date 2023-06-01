import streamlit as st
import streamlit.components.v1 as components

from scripts.api_func import HiliteMeFormatter, load_page

load_page(__file__)

st.title("A Python source code highlighter tool")
hilite_obj = HiliteMeFormatter()

def update_text():
    return

c1, c2 = st.columns(2)

with c1:
    txt = st.text_area('Code to beautify', on_change=update_text, height=500)
    st.write("Current text length: " + str(len(txt)))

with c2:
    if st.button("Execute"):
        if "".join(txt.split()) != "":
            hilite_obj.set(code=txt)
            data_load_state = st.text("Sending request...")
            try:
                components.html(hilite_obj.formatCode(), height=500, scrolling=True)
                data_load_state.text("Result: ")
            except:
                data_load_state.text("Failed to send request.")
        else:
            st.write("Empty code.")