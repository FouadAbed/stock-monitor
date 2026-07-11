import os
import smtplib
from email.mime.text import MIMEText

sender = os.environ["EMAIL_ADDRESS"]
password = os.environ["EMAIL_PASSWORD"]
receiver = os.environ["EMAIL_TO"]

msg = MIMEText(
    """Si tu reçois ce message, c'est que GitHub Actions peut envoyer des e-mails avec Gmail.

Le système est prêt.
"""
)

msg["Subject"] = "✅ Test GitHub Actions"
msg["From"] = sender
msg["To"] = receiver

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(sender, password)
    smtp.send_message(msg)

print("✅ Mail envoyé avec succès")
