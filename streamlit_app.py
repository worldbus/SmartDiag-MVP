import streamlit as st
from monitor import run_ping_traceroute
from speedtest_cli import run_speed_test
from ai_analyzer import analyze_results
from token_handler import generate_token
from email_sender import send_cancel_email

st.set_page_config(page_title="SmartDiag Demo", layout="centered")
st.title("SmartDiag Network Diagnostics")

# 1) Feature selection
st.markdown("### Select the diagnostics you want to run:")
do_ping = st.checkbox("📶 Ping & Traceroute", value=True)
do_speed = st.checkbox("⚡ Speed Test", value=True)
do_ai = st.checkbox("🤖 AI Analysis", value=True)
notify_email = st.checkbox("✉️ Email Cancel Link", value=True)

st.markdown("---")

# 2) Input fields
domain = st.text_input("Domain or IP", placeholder="example.com")
email  = st.text_input("Your Email", placeholder="you@example.com")

# 3) Run button
if st.button("Run Diagnostics"):
    if not domain or (notify_email and not email):
        st.error("Please enter a domain and, if email notification is on, your email.")
    elif not (do_ping or do_speed or do_ai):
        st.error("Please select at least one diagnostic.")
    else:
        results = {}
        with st.spinner("Running selected tests..."):
            if do_ping:
                results["ping_trace"] = run_ping_traceroute(domain)
            if do_speed:
                results["speed"] = run_speed_test()

        # 4) Display results
        if do_ping:
            st.subheader("Ping & Traceroute")
            st.text(results["ping_trace"])
        if do_speed:
            st.subheader("Speed Test")
            st.json(results["speed"])

        # 5) AI analysis
        if do_ai:
            st.subheader("AI Analysis")
            prompt = f"Domain: {domain}\n\n"
            if do_ping:  prompt += results["ping_trace"] + "\n\n"
            if do_speed: prompt += f"Speed test: {results['speed']}\n\n"
            summary = analyze_results(domain, results.get("ping_trace", ""), results.get("speed", {}))
            st.write(summary)

        # 6) Generate & show cancel link
        if notify_email:
            token = generate_token(domain, email)
            cancel_url = (
                f"https://share.streamlit.io/YourUserName/SmartDiag-MVP/"
                f"main/streamlit_app.py?cancel={token}"
            )
            st.success("✅ Diagnostics complete!")
            st.markdown(f"**Your cancel link:**  \n`{cancel_url}`")

            # 7) Send email with cancel link
            send_cancel_email(email, domain, cancel_url)
            st.info(f"Cancel link sent to {email}.")
