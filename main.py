import httpx
from selectolax.parser import HTMLParser

url = 'https://www.rei.com/s/womens-hiking-clothing'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}

resp = httpx.get(url, headers=headers)
html = HTMLParser(resp.text)
products = html.css('li.VcGDfKKy_dvNbxUqm29K')

def extract_text(html, sel):
    try:
        return html.css_first(sel).text()
    except AttributeError:
        return None



for product in products:

    product_brand = extract_text(product, "span[data-ui='product-brand']")
    product_name = extract_text(product, "span[data-ui='product-title']")
    sale_price = extract_text(product, "span[data-ui='sale-price']")
    full_price = extract_text(product, "span[data-ui='full-price']")
    
    item = {
        'brand': product_brand,
        'name': product_name,
        'sale_price': sale_price,
        'full_price': full_price,
    }

    print(item)