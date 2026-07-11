import os
import smtplib
import requests
from email.mime.text import MIMEText

URL = "https://www.auchan.fr/qilive-climatiseur-portable-q-6923-blanc/pr-C1769677"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/138.0.0.0 Safari/537.36"
    )
}

print("Vérification du stock...")

response = requests.get(URL, headers=headers, timeout=30)
response.raise_for_status()

html = response.text

# Détection de l'indisponibilité
indisponible = (
    'content="https://schema.org/OutOfStock"' in html
    or '"status":false' in html
    or 'data-stock="0"' in html
)

if indisponible:
    print("❌ Produit indisponible")
    exit(0)

print("✅ PRODUIT DISPONIBLE")

sender = os.environ["EMAIL_ADDRESS"]
password = os.environ["EMAIL_PASSWORD"]
receiver = os.environ["EMAIL_TO"]

message = MIMEText(
    f"""
Le produit est de nouveau disponible !

Produit :
QILIVE Climatiseur portable Q.6923 Blanc

Lien :
{URL}

Dépêche-toi avant la rupture de stock.
"""
)

message["Subject"] = "🚨 ALERTE STOCK AUCHAN"
message["From"] = sender
message["To"] = receiver

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(sender, password)
    smtp.send_message(message)

print("📧 Mail envoyé")
