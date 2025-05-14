import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_cancel_email(to_email: str, domain: str, cancel_url: str):
    sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
    message = Mail(
        from_email=os.getenv("FROM_EMAIL"),
        to_emails=to_email,
        subject=f"SmartDiag Monitoring Active for {domain}",
        html_content=(
            f"<p>Monitoring for <strong>{domain}</strong> is now active.</p>"
            f"<p>Click here to cancel monitoring at any time:<br>"
            f"<a href='{cancel_url}'>Cancel Monitoring</a></p>"
        )
    )
    sg.send(message)
