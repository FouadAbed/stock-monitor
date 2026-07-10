import requests
from bs4 import BeautifulSoup
import os

URL = "https://www.auchan.fr/qilive-climatiseur-portable-q-6923-blanc/pr-C1769677"

headers = {
    "User-Agent": "Mozilla/5.0"
}

page = requests.get(URL, headers=headers)

print("Statut HTTP :", page.status_code)

if page.status_code != 200:
    raise Exception("Impossible de récupérer la page")

html = page.text

if "Ajouter au panier" in html:
    print("✅ DISPONIBLE")
else:
    print("❌ Toujours indisponible")
