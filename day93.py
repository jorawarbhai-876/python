import requests
url = "https://www.codewithharry.com"
r = requests.get(url)
print(r.text)
