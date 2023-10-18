import httpx
from selectolax.parser import HTMLParser

def get_html(base_url, page):
    
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}

    resp = httpx.get(base_url + str(page) , headers=headers, follow_redirects=True)
    html = HTMLParser(resp.text)
    return html


def extract_text(html, sel):
    try:
        return html.css_first(sel).text()
    except AttributeError:
        return None

def parse_page(html):
    products = html.css('li.VcGDfKKy_dvNbxUqm29K')
    product_list = []
    for product in products:
        product_brand = extract_text(product, "span[data-ui='product-brand']")
        product_name = extract_text(product, "span[data-ui='product-title']")
        sale_price = extract_text(product, "span[data-ui='sale-price']")
        full_price = extract_text(product, "span[data-ui='full-price']")
        savings = extract_text(product, "div[data-ui='savings-percent-variant2']")
        
        item = {
            'brand': product_brand,
            'name': product_name,
            'sale_price': sale_price,
            'full_price': full_price,
            'saving': savings
        }
        yield item

def main():
    base_url = 'https://www.rei.com/s/womens-hiking-clothing?page='
    for x in range(1,10):
        print(x)
        print("*********************************************")
        html = get_html(base_url, x)
        data = parse_page(html)
        for item in data:
            print(item)

if __name__ == '__main__':
    main()