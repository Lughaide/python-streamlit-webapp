import streamlit as st

from scripts.api_func import ProfanityCheck

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
            st.json(prof_obj.getFilteredResults())
            data_load_state.text("Result: ")
        except:
            data_load_state.text("Failed to send request.")
    else:
        st.write("Empty code.")