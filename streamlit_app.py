import streamlit as st
from token_handler import generate_token

st.set_page_config(page_title="SmartDiag Demo")
st.title("SmartDiag Network Monitor Demo")

domain = st.text_input("🌐 Domain or IP")
email  = st.text_input("✉️ Email Address")

if st.button("Start Monitoring"):
    if domain and email:
        token = generate_token(domain, email)
        cancel_link = f"https://share.streamlit.io/worldbus/SmartDiag-MVP/main/streamlit_app.py?token={token}"
        st.success("✅ Monitoring started!\n\nYour cancel link:\n" + cancel_link)
    else:
        st.error("Please enter both domain and email.")
