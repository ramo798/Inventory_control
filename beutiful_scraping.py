import requests
from bs4 import BeautifulSoup

def get_target_url(url):
    url_list = []
    for count in range(10):
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        targets = soup.find(id="list01")
        target_url = targets.select("h3 > a")
        for tmp in target_url:
            url_list.append(tmp['href'])
    return url_list


a = 'https://auctions.yahoo.co.jp/seller/tomokimi_777'
test = get_target_url(a)

print(test)


# res = requests.get('https://auctions.yahoo.co.jp/seller/tomokimi_777')
# soup = BeautifulSoup(res.text, 'html.parser')

# test = soup.find(class_="next")
# a = test.find('a')
# print(a['href'])



