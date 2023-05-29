import streamlit as st

from scripts.api_func import QRCodeMaker

st.title("QR Code Generator")

qr_obj = QRCodeMaker()

txt = st.text_input("Content to embed into QR Code")
size = st.text_input("QR Image Size. Must follow format: {height}x{width}")

if st.button("Create"):
    if "".join(txt.split()) != "":
        qr_obj.set(data=txt, size=size)
        data_load_state = st.text("Sending request...")
        try:
            st.image(qr_obj.getQRCode())
            data_load_state.text("Result: ")
        except:
            data_load_state.text("Failed to send request.")
    else:
        st.write("Empty code.")