import scraping as sc

if __name__ == '__main__':
    users = ["younghoho_1121","tomokimi_777"]
    # users = ["merci_dsyl"]
    for username in users:
        items = sc.get_items(username)
        print('GET ITEM FINISH. FROM ',username)

        # for item in items:
        #     print(item)
        #     op.operation(item,username)