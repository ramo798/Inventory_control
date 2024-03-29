import requests
from bs4 import BeautifulSoup

# 商品一覧ページのURL取得


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
        except AttributeError as e:
            pass
    return page_list

# 商品の個別ページのURL取得


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

# 商品詳細の取得


def get_item_info(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    title = soup.find(class_="ProductTitle__text").text
    title = title.replace('\u3000', '')

    price_tmp = soup.find(class_="Price__value").text
    price = price_tmp[:price_tmp.find("円")]
    price = price.replace('\n', '')

    exp = soup.find(class_="ProductExplanation__commentArea")
    measuring = extraction_item_info(exp.text)

    resu = {'title': title, 'price': price, 'measuring': measuring, 'url': url}
    return resu

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
        # print(kata)
    elif text.find("ウエスト:") > -1:
        start = text.find("ウエスト:")
        tmp = text[start:]
        stop = tmp.find("cm")
        kata_tmp = tmp[:stop]
        kata = kata_tmp[tmp.find(":")+1:]
        # print(kata)
    else:
        kata = " "
    # 身幅orヒップ
    if text.find("身幅:") > -1:
        start = text.find("身幅:")
        tmp = text[start:]
        stop = tmp.find("cm")
        bast_tmp = tmp[:stop]
        bast = bast_tmp[tmp.find(":")+1:]
        # print(bast)
    elif text.find("ヒップ:") > -1:
        start = text.find("ヒップ:")
        tmp = text[start:]
        stop = tmp.find("cm")
        bast_tmp = tmp[:stop]
        bast = bast_tmp[tmp.find(":")+1:]
        # print(bast)
    else:
        bast = " "
    # 着丈or丈
    if text.find("着丈:") > -1:
        start = text.find("着丈:")
        tmp = text[start:]
        stop = tmp.find("cm")
        take_tmp = tmp[:stop]
        take = take_tmp[tmp.find(":")+1:]
        # print(take)
    elif text.find("丈:") > -1:
        start = text.find("丈:")
        tmp = text[start:]
        stop = tmp.find("cm")
        take_tmp = tmp[:stop]
        take = take_tmp[tmp.find(":")+1:]
        # print(take)
    else:
        take = " "
    # 袖丈
    if text.find("袖丈:") > -1:
        start = text.find("袖丈:")
        tmp = text[start:]
        stop = tmp.find("cm")
        sode_tmp = tmp[:stop]
        sode = sode_tmp[tmp.find(":")+1:]
        # print(sode)
    else:
        sode = " "

    res = {"id": id, 'kata': kata, 'take': take, 'bast': bast, 'sode': sode}
    return res

# ユーザー名を受け取って商品リストを返す


def get_items(str_id):
    url = 'https://auctions.yahoo.co.jp/seller/' + str_id
    list_url = get_list(url)

    # 一回取得するだけではURLに漏れがあったので、複数回取得した後に重複を削除する
    syouhin_urls = []
    for count in range(5):
        syouhin_urls = syouhin_urls + get_target_url(list_url)

    # 重複の削除
    syouhin_urls = set(syouhin_urls)
    print('商品数:', len(syouhin_urls))

    # 返り値の商品の情報のリスト
    items = []
    for tmp in syouhin_urls:
        syousai = get_item_info(tmp)
        print(syousai)
        items.append(syousai)

    return items
