import requests

URL = "https://www.auchan.fr/qilive-climatiseur-portable-q-6923-blanc/pr-C1769677"

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(URL, headers=headers)
html = r.text

if 'content="https://schema.org/OutOfStock"' in html:
    print("❌ Produit indisponible")
elif '"status":false' in html:
    print("❌ Produit indisponible")
elif 'data-stock="0"' in html:
    print("❌ Produit indisponible")
else:
    print("✅ PRODUIT DISPONIBLE")
