import streamlit as st
from monitor import run_ping_traceroute
from speedtest_cli import run_speed_test
from ai_analyzer import analyze_results
from token_handler import generate_token
from email_sender import send_cancel_email

st.set_page_config(page_title="SmartDiag Demo", layout="centered")
st.title("SmartDiag Network Diagnostics")

domain = st.text_input("Domain or IP", placeholder="example.com")
email  = st.text_input("Your Email", placeholder="you@example.com")

if st.button("Run Diagnostics"):
    if not domain or not email:
        st.error("Please enter both domain and email.")
    else:
        with st.spinner("Running tests..."):
            ping_trace = run_ping_traceroute(domain)
            speed      = run_speed_test()
        st.subheader("Ping & Traceroute")
        st.text(ping_trace)
        st.subheader("Speed Test")
        st.json(speed)

        summary = analyze_results(domain, ping_trace, speed)
        st.subheader("AI Analysis")
        st.write(summary)

        token = generate_token(domain, email)
        cancel_url = f"https://share.streamlit.io/YourUserName/SmartDiag-MVP/main/streamlit_app.py?cancel={token}"
        st.success("Diagnostics complete!")
        st.markdown(f"Your cancel link:\n\n`{cancel_url}`")

        send_cancel_email(email, domain, cancel_url)
        st.info(f"Cancel link sent to {email}.")
