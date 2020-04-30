import requests
from bs4 import BeautifulSoup

res = requests.get('https://auctions.yahoo.co.jp/seller/tomokimi_777')

soup = BeautifulSoup(res.text, 'html.parser')

targets = soup.find(id="list01")

target_url = targets.select("h3 > a")

for tmp in target_url:
    print(tmp.text)
