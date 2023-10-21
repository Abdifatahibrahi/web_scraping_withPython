import httpx
from selectolax.parser import HTMLParser




def get_html(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}
    resp = httpx.get(url, headers=headers, follow_redirects=True)
    print(resp.status_code)
    html = HTMLParser(resp.text)
    return html

def extract_data(html, sel):
    try:
        return html.css_first(sel).text()
    except AttributeError:
        return None

def extract_urls(html):
    hotel_lists = html.css('div.partner-listing')
    url_list = []
    for hotel in hotel_lists:
        url = hotel.css_first('p.company a').attributes['href']
        yield url
    #     url_list.append(url)
    # return url_list

def parse_hotel(url_list):
    for url in url_list:
        html = get_html(url)
        try:
            title = extract_data(html, 'h1.title.color-primary')
            print(title)
        except None:
            print('None')
def main():
    url = 'https://www.krtourism.ca/partners/partners-list/'
    html = get_html(url)
    url_list = extract_urls(html)
    parse_hotel(url_list)


main()