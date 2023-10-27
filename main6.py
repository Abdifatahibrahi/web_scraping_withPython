import httpx
import pandas as pd
from selectolax.parser import HTMLParser
from urllib.parse import urljoin

url = "https://www.amishbaskets.com/collections/all?sort_by=best-selling"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}


resp = httpx.get(url, headers=headers)

html = HTMLParser(resp.text)

products = html.css('ul.productgrid--items.products-per-row-4 li')

name = []
urls = []
original_price = []
current_price = []
for product in products:
    name.append(product.css_first("h2.productitem--title a").text().strip())
    urls.append(urljoin("https://www.amishbaskets.com/collections/all?sort_by=best-selling", product.css_first("h2.productitem--title a").attributes['href']))
    original_price.append(product.css_first('div span.money.price__compare-at--single').text().strip())
    
    try:
        current_price.append(product.css_first('div.price__current.price__current--on-sale span.money').text().strip())
    except Exception as e:
        print(e)
    
    
    


products_df = pd.DataFrame({'Name': name, "Urls": urls, "Original Price": original_price, "Current_price": current_price})

print(products_df)