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
    page_list.append(access_url)
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

# 商品説明のテキストからサイズなどの取得
def extraction_item_info(text):
    # 商品ID取得
    start = text.find("[")
    stop = text.find("]")
    id = text[start+1:stop]
    # print (id)

    # 採寸情報取得
    # 肩orウエスト
    if text.find("肩幅:") > -1:
        start = text.find("肩幅:")
        tmp = text[start:]
        stop = tmp.find("cm")
        kata_tmp = tmp[:stop]
        kata = kata_tmp[tmp.find(":")+1:]
        print(kata)
    elif text.find("ウエスト:") > -1:
        start = text.find("ウエスト:")
        tmp = text[start:]
        stop = tmp.find("cm")
        kata_tmp = tmp[:stop]
        kata = kata_tmp[tmp.find(":")+1:]
        print(kata)
    else:
        kata = " "
    # 身幅orヒップ
    if text.find("身幅:") > -1:
        start = text.find("身幅:")
        tmp = text[start:]
        stop = tmp.find("cm")
        bast_tmp = tmp[:stop]
        bast = bast_tmp[tmp.find(":")+1:]
        print(bast)
    elif text.find("ヒップ:") > -1:
        start = text.find("ヒップ:")
        tmp = text[start:]
        stop = tmp.find("cm")
        bast_tmp = tmp[:stop]
        bast = bast_tmp[tmp.find(":")+1:]
        print(bast)
    else:
        bast = " "
    # 着丈or丈
    if text.find("着丈:") > -1:
        start = text.find("着丈:")
        tmp = text[start:]
        stop = tmp.find("cm")
        take_tmp = tmp[:stop]
        take = take_tmp[tmp.find(":")+1:]
        print(take)
    elif text.find("丈:") > -1:
        start = text.find("丈:")
        tmp = text[start:]
        stop = tmp.find("cm")
        take_tmp = tmp[:stop]
        take = take_tmp[tmp.find(":")+1:]
        print(take)
    else:
        sode = " "
    #袖丈
    if text.find("袖丈:") > -1:
        start = text.find("袖丈:")
        tmp = text[start:]
        stop = tmp.find("cm")
        sode_tmp = tmp[:stop]
        sode = sode_tmp[tmp.find(":")+1:]
        print(sode)
    else:
        sode = " " 



# 商品詳細の取得
def get_item_info(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    title = soup.find(class_="ProductTitle__text")
    price = soup.find(class_="Price__value")
    exp = soup.find(class_="ProductExplanation__commentArea")
    extraction_item_info(exp.text)

# url = 'https://auctions.yahoo.co.jp/seller/tomokimi_777'
# list_url = get_list(url)
# print(len(list_url))
# syouhin = get_target_url(list_url)
# print(len(syouhin))


url = "https://page.auctions.yahoo.co.jp/jp/auction/b455972441"
url2 = "https://page.auctions.yahoo.co.jp/jp/auction/c811472567"
get_item_info(url)
