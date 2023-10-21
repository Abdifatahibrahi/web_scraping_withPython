import httpx
from selectolax.parser import HTMLParser

url = 'https://www.adidas.co.id/pria/sepatu/sepak-bola.html'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}


resp = httpx.get(url, headers=headers)
print(resp.status_code)
html = HTMLParser(resp.text)
try:
    shoes_list = html.css('h1.gl-heading.gl-heading--l gl-heading--italic.gl-heading--no-margin').text()
    
    print(shoes_list)
except Exception as e:
    print(e)