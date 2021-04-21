from components import get_items as gi
import csv
import pandas as pd

if __name__ == '__main__':
    res_list = []
    # データベースの更新
    users = ["younghoho_1121", "tomokimi_777"]
    # users = ["merci_dsyl"]
    for username in users:
        items = gi.get_items(username)
        print('GET ITEM FINISH. FROM ', username)

        for item in items:
            print(item)
            res_list.append(item)

            # writer.writerow(item)
            # op.operation(item, username)

    df = pd.io.json.json_normalize(res_list)
    print(df)
    df.to_csv('dogs.csv')

    # sold_out判定用のバッチ処理
    # op.sold_out_checker()

    # items = ge.generate()
    # up.upload_csv(items)
