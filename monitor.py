import requests
import re

url = "https://www.auchan.fr/qilive-climatiseur-portable-q-6923-blanc/pr-C1769677"

r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

html = r.text

print("HTTP :", r.status_code)

# Cherche les lignes qui parlent de disponibilité
mots = [
    "availability",
    "Available",
    "InStock",
    "OutOfStock",
    "stock",
    "dispo",
    "rupture",
]

for mot in mots:
    print(f"\n===== {mot} =====")
    for m in re.finditer(mot, html, re.IGNORECASE):
        debut = max(0, m.start() - 120)
        fin = min(len(html), m.end() + 120)
        print(html[debut:fin].replace("\n", " "))
