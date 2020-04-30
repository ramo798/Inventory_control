from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
from bs4 import BeautifulSoup
import lxml

options = Options()
options.add_argument('--disable-gpu');
options.add_argument('--disable-extensions');
options.add_argument('--proxy-server="direct://"');
options.add_argument('--proxy-bypass-list=*');
options.add_argument('--start-maximized');
# options.add_argument('--headless');
DRIVER_PATH = './driver/chromedriver'

# sheetへの接続処理
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('mykey.json', scope)
gc = gspread.authorize(credentials)
SPREADSHEET_KEY = '14KEmq_Ziqf5DyB7im6-sNECmHeGR4GEio_KYPTw8R-Q'
worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1

# ブラウザの起動
driver = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=options)

username = "tomokimi_777"
URL = "https://auctions.yahoo.co.jp/seller/" + username
driver.get(URL)

time.sleep(3)


#　アクセスするURLのリスト
url_list = []
for count in range(10):
    time.sleep(5)
    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, "lxml")
    targets = soup.find(id="list01")
    target_url = targets.select("h3 > a")
    for tmp in target_url:
        url_list.append(tmp['href'])
    driver.find_element_by_class_name("next").click()
    time.sleep(5)


no = 1
# 順番にアクセスする
for access in url_list:
    print(no)
    print (access)
    driver.get(access)
    time.sleep(8)

    # title取得
    title = driver.find_element_by_css_selector("#ProductTitle h1")
    print (title.text)

    #価格取得
    # #l-sub > div.ProductInformation > ul > li.ProductInformation__item.js-stickyNavigation-start > div.Price.Price--buynow > dl > dd
    price = driver.find_element_by_css_selector(".Price__value")
    print (price.text[:price.text.find("円")])

    # 商品のコメントを取得
    comment = driver.find_element_by_css_selector(".ProductExplanation__commentArea")
    # 商品ID抽出
    start = comment.text.find("[")
    stop = comment.text.find("]")
    print (comment.text[start+1:stop])
    # 採寸取得
    t_comment = comment.text
    if t_comment.find("肩幅:")!= -1:
        kata = t_comment[t_comment.find("肩幅:"):t_comment.find("cm")]
        #print (kata[kata.find(":")+1:])
        w_kata = kata[kata.find(":")+1:]
    elif t_comment.find("ウエスト:")!= -1:
        kata = t_comment[t_comment.find("ウエスト:"):t_comment.find("cm")]
        w_kata = kata[kata.find(":")+1:]
    else:
        w_kata = " "
    print (w_kata)
    if t_comment.find("身幅:")!= -1:
        bast_text = t_comment[t_comment.find("身幅:"):]
        bast = bast_text[:bast_text.find("cm")]
        # print (bast)
        w_bast = bast[bast.find(":")+1:]
    elif t_comment.find("ヒップ:")!= -1:
        bast_text = t_comment[t_comment.find("ウエスト:"):]
        bast = bast_text[:bast_text.find("cm")]
        w_bast = bast[bast.find(":")+1:]
    else:
        w_bast = " "
    print (w_bast)
    if t_comment.find("着丈:")!= -1:
        take_text = t_comment[t_comment.find("着丈:"):]
        take = take_text[:take_text.find("cm")]
        # print (bast)
        w_take = take[take.find(":")+1:]
    elif t_comment.find("丈:")!= -1:
        take_text = t_comment[t_comment.find("丈:"):]
        take = take_text[:take_text.find("cm")]
        # print (bast)
        w_take = take[take.find(":")+1:]
    else:
        w_take = " "
    print (w_take)
    if t_comment.find("袖丈:")!= -1:
        sode_text = t_comment[t_comment.find("袖丈:"):]
        sode = sode_text[:sode_text.find("cm")]
        # print (bast)
        w_sode = sode[sode.find(":")+1:]
    else:
        w_sode = " "
    print (w_sode)

     #sheet書き込みの処理
    w_title = title.text
    w_price = price.text[:price.text.find("円")]
    w_p_id = comment.text[start+1:stop]
    today = str(datetime.date.today())
    w_list = [w_p_id,w_title,w_price,w_kata,w_bast,w_take,w_sode,today]

    # 同じ品番の物があれば日付のみ更新してpass
    try:
        being = worksheet.find(w_p_id)
        worksheet.update_cell(being.row, 8, today)
        pass
    except:
        try:
            worksheet.append_row(w_list)
        except :
            time.sleep(110)
            worksheet.append_row(w_list)

    no += 1



time.sleep(10)
print ("finish")
driver.close()
driver.quit()