import csv
import boto3


def get_data_from_csv():

    with open('Inventory_20210421.csv', 'r', encoding="utf-8_sig") as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]

    f.close()

    return data


# 初回登録
if __name__ == '__main__':
    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000",
                              region_name='ap-northeast-1', aws_access_key_id='fake', aws_secret_access_key='fake')
    table = dynamodb.Table('items2')

    for obj in get_data_from_csv():
        pn = obj["物品名"][0:4]

        table.put_item(
            Item={
                'zaiko_id': int(obj["在庫ID"]),
                'item_name': obj["物品名"],
                'Category': obj["カテゴリ"],
                'quantity': int(obj["数量"]),
                'product_number': pn,
                'younghoho_1121': 0,
                'tomokimi_777': 0,
                'maron': 0,
            })
        # print(item)
