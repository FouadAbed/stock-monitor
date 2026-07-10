import requests
import re

url = "https://www.auchan.fr/qilive-climatiseur-portable-q-6923-blanc/pr-C1769677"

r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

print(r.status_code)

# Sauvegarde le HTML
with open("page.html", "w", encoding="utf-8") as f:
    f.write(r.text)

print("Longueur :", len(r.text))

# Cherche quelques mots intéressants
for mot in [
    "availability",
    "stock",
    "dispon",
    "pickup",
    "delivery",
    "product",
    "__NEXT_DATA__",
    "application/ld+json",
]:
    print(mot, "=>", mot.lower() in r.text.lower())
