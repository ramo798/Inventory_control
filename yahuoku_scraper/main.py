import scraping as sc
import function as fn
import json


def main():
    users = ["younghoho_1121", "tomokimi_777"]
    # users = ["merci_dsyl"]
    for username in users:
        items = sc.get_items(username)
        # print(items)
        print('GET ITEM FINISH. FROM ', username)

        for item in items:
            print(type(item))
            user = {'username': username}
            item.update(user)
            fn.send_json(item)


if __name__ == '__main__':
    # dic_test = {'title': '★HERMES★新品★Manteau detail metal コートサイズ34', 'price': '330,000', 'measuring': {'id': 'HC8', 'kata': ' ', 'take': '97.5', 'bast': '52', 'sode': ' '}, 'url': 'https://page.auctions.yahoo.co.jp/jp/auction/o396678682'}
    # user = {'username':"aa"}
    # dic_test.update(user)
    # print(dic_test)
    main()
