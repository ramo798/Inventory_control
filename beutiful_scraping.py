import requests
from bs4 import BeautifulSoup

# def get_target_url(access_url):
#     url_list = []
#     url = access_url
#     for count in range(1):
#         res = requests.get(url)
#         soup = BeautifulSoup(res.text, 'html.parser')
#         targets = soup.find(id="list01")
#         target_url = targets.select("h3 > a")
#         for tmp in target_url:
#             url_list.append(tmp['href'])
#     return url_list

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
test = get_list(url)
print(test)

# a = 'https://auctions.yahoo.co.jp/seller/tomokimi_777'
# test = get_target_url(a)
# print(len(test))


# res = requests.get('https://auctions.yahoo.co.jp/seller/tomokimi_777')
# soup = BeautifulSoup(res.text, 'html.parser')

# test = soup.find(class_="next")
# a = test.find('a')
# print(a['href'])



