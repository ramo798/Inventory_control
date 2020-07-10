from components import get_items as gi
from components import operation_db as op
from components import s3_upload as up
from components import generate_csv_components as ge


if __name__ == '__main__':
    # データベースの更新
    users = ["younghoho_1121","tomokimi_777"]
    # users = ["merci_dsyl"]
    for username in users:
        items = gi.get_items(username)
        print('GET ITEM FINISH. FROM ',username)

        for item in items:
            print(item)
            op.operation(item,username)

    # sold_out判定用のバッチ処理
    op.sold_out_checker()

    items = ge.generate()
    up.upload_csv(items)
    