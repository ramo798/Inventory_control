import json
import operate_db as op

def analysis_json(data):
    # dataはdict型でくる
    # res = str(type(data))

    # res = data['measuring']['id']
    res = data

    return res

if __name__ == '__main__':
    test_data = {"measuring": {"bast": " ","id": "US170","kata": " ","sode": " ","take": " "},"price": "5,980","title": "☆FENDI☆ミュールサイズ8(25.5cm)","url": "https://page.auctions.yahoo.co.jp/jp/auction/o392826623"}
    
    # test = analysis_json(test_json)

    op.operation(test_data,"aaa")

