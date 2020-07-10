import scraping as sc
import json

def main():
    users = ["younghoho_1121","tomokimi_777"]
    # users = ["merci_dsyl"]
    for username in users:
        items = sc.get_items(username)
        print('GET ITEM FINISH. FROM ',username)

        # for item in items:
        #     print(item)
        #     op.operation(item,username)
        for item in items:
            tmp = json.dumps(item).encode("utf-8")
            print(tmp)
            break


if __name__ == '__main__':
    uni_test = {"title": "\u2605HERMES\u2605\u65b0\u54c1\u30fb\u65b0\u4f5c\u2605\u30c4\u30a3\u30ea\u30fcLES ZEBRESPD/ROSE BONBON/NOIR/B", "price": "23,800", "measuring": {"id": "HT16", "kata": " ", "take": " ", "bast": " ", "sode": " "}, "url": "https://page.auctions.yahoo.co.jp/jp/auction/g429298584","username":"test222"}
    print(uni_test)    