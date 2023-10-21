import requests
from bs4 import BeautifulSoup

url = 'https://www.adidas.co.id/pria/sepatu/sepak-bola.html'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}

resp = requests.get(url, headers=headers)
print(resp.status_code)

html = BeautifulSoup(resp.text, 'html.parser')

shoes_list = html.findAll('li.ProductCard')

for s in shoes_list:
    print(s)

print(shoes_list)


