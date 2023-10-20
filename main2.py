import httpx
from selectolax.parser import HTMLParser
from urllib.parse import urljoin
from dataclasses import dataclass, asdict
# rei.com

@dataclass
class Item:
    name: str
    item_num: str
    price: str
    rating: float

def get_html(base_url, **kwargs):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}
    if kwargs.get('page'):
        resp = httpx.get(base_url + str(kwargs.get('page')), headers=headers, follow_redirects=True)
    else:
        resp = httpx.get(base_url, headers=headers, follow_redirects=True)
    try:
        resp.raise_for_status()
    except httpx.HTTPStatusError as exc:
        print(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}. Page limit exceded!")
        return False
    
    html = HTMLParser(resp.text)
    return html


def extract_text(html, selec):
    try:
        return html.css_first(selec).text()
    except AttributeError:
        return None
    
def parse_item_page(html: HTMLParser):
    new_item = Item(
        name = extract_text(html, 'h1#product-page-title'),
        item_num = extract_text(html, 'span#product-item-number'),
        price = extract_text(html, 'span#buy-box-product-price'),
        rating = extract_text(html, 'span.cdr-rating__number_13-5-3')
    )
    return new_item


def parse_products(html):
    products = html.css('li.VcGDfKKy_dvNbxUqm29K')
    item_list = []
    for product in products:
        yield urljoin("https://www.rei.com/c/mens-workout-clothing", product.css_first('a').attributes['href'])

        


def main():
    url = 'https://www.rei.com/c/mens-workout-clothing?page='
    products = []
    for x in range(1, 4):
        print(f"Page {x}")
        html = get_html(url, page = x)
        if html == False:
            break
        product_urls = parse_products(html)
        for url in product_urls:
            # print(url)
            html = get_html(url)
            products.append(parse_item_page(html))

        for product in products:
            print(asdict(product))

if __name__ == '__main__':
    main()

# main()