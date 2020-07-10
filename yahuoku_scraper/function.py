import urllib.request
import json

def send_json(r_json):
    url = "http://0.0.0.0:5000/item_data" 
    method = "POST"
    headers = {"Content-Type" : "application/json"}

    json_data = json.dumps(r_json).encode("utf-8")
    # print(type(json_data))

    request = urllib.request.Request(url, data=json_data, method=method, headers=headers)

    # print(request.status_code)

    # print(request.status_code)
    try:
        with urllib.request.urlopen(request) as response:
            response_body = response.read().decode("utf-8")
        return True

    except urllib.error.HTTPError:
        return False

    


if __name__ == '__main__':
    json_test = {"measuring": {"bast": " ","id": "US170","kata": " ","sode": " ","take": " "},"price": "5,980","title": "☆FENDI☆ミュールサイズ8(25.5cm)","url": "https://page.auctions.yahoo.co.jp/jp/auction/o392826623","username":"test123"}
    json_test2 = {"measuring": {"bast": " ","id": "US170","kata": " ","sode": " ","take": " "},"price": "5,980","title": "☆FENDI☆ミュールサイズ8(25.5cm)","url": "https://page.auctions.yahoo.co.jp/jp/auction/o392826623"}

    
    result = (send_json(json_test))
    print(result)
