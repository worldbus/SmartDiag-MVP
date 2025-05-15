# email_sender.py

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from python_http_client.exceptions import HTTPError

def send_cancel_email(to_email: str, domain: str, cancel_url: str):
    message = Mail(
        from_email=os.getenv("FROM_EMAIL"),
        to_emails=to_email,
        subject=f"SmartDiag: Monitoring for {domain}",
        html_content=(
            f"<p>Monitoring for <strong>{domain}</strong> is now active.</p>"
            f"<p>To cancel, click:<br><a href='{cancel_url}'>Cancel Monitoring</a></p>"
        )
    )
    try:
        sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
        sg.send(message)
    except HTTPError as e:
        # Return or log a friendly message instead of crashing
        print(f"SendGrid error: {e.status_code} {e.body}")
        # Optionally return a flag or message
        return False
    return True
