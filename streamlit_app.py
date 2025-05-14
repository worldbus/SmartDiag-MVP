import streamlit as st
from monitor import run_ping_traceroute
from speedtest_cli import run_speed_test
from ai_analyzer import analyze_results
from token_handler import generate_token
from email_sender import send_cancel_email

st.set_page_config(page_title="SmartDiag Demo", layout="centered")
st.title("SmartDiag Network Diagnostics")

# Feature toggles
do_ping = st.checkbox("📶 Ping & Traceroute", True)
do_speed = st.checkbox("⚡ Speed Test", True)
do_ai = st.checkbox("🤖 AI Analysis", True)
notify_email = st.checkbox("✉️ Email Cancel Link", True)
st.markdown("---")

# Inputs
domain = st.text_input("Domain or IP", "example.com")
email  = st.text_input("Your Email", "you@example.com")

if st.button("Run Diagnostics"):
    if not domain or (notify_email and not email):
        st.error("Please enter a domain and your email (if you want cancellation emails).")
    else:
        results = {}

        if do_ping:
            with st.spinner("Pinging..."):
                results["ping_trace"] = run_ping_traceroute(domain)
            st.subheader("📶 Ping Results")
            st.text(results["ping_trace"])

        if do_speed:
            with st.spinner("Testing speed..."):
                results["speed"] = run_speed_test()
            st.subheader("⚡ Speed Test")
            st.json(results["speed"])

        if do_ai:
            st.subheader("🤖 AI Analysis")
            summary = analyze_results(
                domain,
                results.get("ping_trace", ""),
                results.get("speed", {})
            )
            st.write(summary)

        if notify_email:
            token = generate_token(domain, email)
            cancel_url = (
                f"https://share.streamlit.io/YourUserName/SmartDiag-MVP/"
                f"main/streamlit_app.py?cancel={token}"
            )
            st.success("✅ Diagnostics complete!")
            st.markdown(f"🔗 Cancel link:\n`{cancel_url}`")
            send_cancel_email(email, domain, cancel_url)
            st.info(f"Cancel link sent to {email}.")
