import requests


resp = requests.get("https://facebook.com")
print(resp.text)
