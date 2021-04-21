import json
import operate_db as op

# {'measuring': {'bast': ' ', 'id': '', 'kata': ' ', 'sode': ' ', 'take': ' '}, 'price': '', 'title': '', 'url': '', 'username': ''}の形で渡せば処理できる
def analysis_json(data):
    # dataはdict型でくる
    try:
        op.operation(data)
        return True
    except:
        return False


if __name__ == '__main__':
    test_data = {"measuring": {"bast": " ","id": "US170","kata": " ","sode": " ","take": " "},"price": "5,980","title": "☆FENDI☆ミュールサイズ8(25.5cm)","url": "https://page.auctions.yahoo.co.jp/jp/auction/o392826623"}
    user = {'username': "test"}
    # test_data.update(user)
    
    print(analysis_json(test_data))

