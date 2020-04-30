import requests
from bs4 import BeautifulSoup

# 商品の個別のURL取得
def get_target_url(access_urls):
    url_list = []
    for url in access_urls:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        targets = soup.find(id="list01")
        target_url = targets.select("h3 > a")
        for tmp in target_url:
            url_list.append(tmp['href'])
    return url_list

# 商品一覧のURL取得
def get_list(access_url):
    page_list = []
    url = access_url
    for tmp in range(10):
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        try:
            next_button = soup.find(class_="next")
            next_button_url = next_button.find('a')
            page_list.append(next_button_url['href'])
            url = next_button_url['href']
        except TypeError as e:
            pass
    return page_list

url = 'https://auctions.yahoo.co.jp/seller/tomokimi_777'
list_url = get_list(url)
syouhin = get_target_url(list_url)
print(syouhin)



# a = 'https://auctions.yahoo.co.jp/seller/tomokimi_777'
# test = get_target_url(a)
# print(len(test))


# res = requests.get('https://auctions.yahoo.co.jp/seller/tomokimi_777')
# soup = BeautifulSoup(res.text, 'html.parser')

# test = soup.find(class_="next")
# a = test.find('a')
# print(a['href'])



