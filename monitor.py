import requests

URL = "https://www.auchan.fr/qilive-climatiseur-portable-q-6923-blanc/pr-C1769677"

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(URL, headers=headers)

print("HTTP :", r.status_code)

html = r.text

for texte in [
    "Bientôt dispo",
    "Ajouter au panier",
    "Ajouter au panier ",
    "Livraison dès",
    "Rupture",
]:
    print(f"{texte} :", texte in html)
