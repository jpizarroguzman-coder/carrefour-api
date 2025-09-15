import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0"
}

def get_carrefour_price(query):
    url = f"https://www.carrefour.es/search?q={query.replace(' ', '+')}"
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    item = soup.select_one("div.product-card")
    if not item: return None
    title = item.select_one("a.product-card-link").text.strip()
    price = item.select_one("span.current-price").text.strip().replace("€", "").replace(",", ".")
    return title, float(price)

def get_amazon_price(query):
    url = f"https://www.amazon.es/s?k={query.replace(' ', '+')}"
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    item = soup.select_one("div.s-result-item span.a-text-normal")
    if not item: return None
    title = item.text.strip()
    price_whole = soup.select_one("span.a-price-whole")
    price_frac = soup.select_one("span.a-price-fraction")
    if price_whole and price_frac:
        price = float(price_whole.text.replace(".", "") + "." + price_frac.text)
        return title, price
    return None

def compare_products(query):
    result = []
    carrefour = get_carrefour_price(query)
    amazon = get_amazon_price(query)
    if carrefour and amazon:
        c_title, c_price = carrefour
        a_title, a_price = amazon
        diff = a_price - c_price
        margin = (diff / c_price) * 100
        result.append({
            "carrefour_title": c_title,
            "carrefour_price": round(c_price, 2),
            "amazon_title": a_title,
            "amazon_price": round(a_price, 2),
            "diferencia": round(diff, 2),
            "margen": round(margin, 2),
        })
    return result