import streamlit as st

from scripts.api_func import ProfanityCheck, load_page

load_page(__file__)

st.title("Profanity filter")

prof_obj = ProfanityCheck()

txt = st.text_input("Sentence to filter profanity from")
additional_word = st.text_input("Some words to manually replace. Separate with a comma (,). Ex: this, you")
fill_text = st.text_input("Custom word to replace default censor")

if st.button("Create"):
    if "".join(txt.split()) != "":
        prof_obj.set(text=txt, add=additional_word, fill_text=fill_text)
        data_load_state = st.text("Sending request...")
        try:
            st.text(prof_obj.getFilteredResults()["result"])
            data_load_state.text("Result: ")
        except:
            data_load_state.text("Failed to send request.")
    else:
        st.write("Empty code.")