# import requests

# res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# print(len(res.text))

import bs4, requests

# res = requests.get('https://otbdiscs.com/product/jawbreaker-og-glo-buzzz/')

# soup = bs4.BeautifulSoup(res.text, 'html.parser')
# elems = soup.select('#product-529927 > div.summary.entry-summary > p > span > bdi')
# print(elems[0].text)
# print(res.status_code)

def getPrice(url):
    res = requests.get(url)
    res.raise_for_status
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#product-529927 > div.summary.entry-summary > p > span > bdi')
    return elems[0].text.strip()

price = getPrice('https://otbdiscs.com/product/jawbreaker-og-glo-buzzz/')
print("The price is " + price)