import boto3
import csv
import get_items
from decimal import Decimal
from pprint import pprint


def get_all():
    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000",
                              region_name='ap-northeast-1',
                              aws_access_key_id='fake',
                              aws_secret_access_key='fake')
    dynamodb_table = dynamodb.Table('items2')

    response = dynamodb_table.scan()

    # print(len(response["Items"]))
    # print(response["Items"])
    # for a in response["Items"]:
    # print(a["product_number"])
    # print(response["ResponseMetadata"])

    return response["Items"]


def get_data_from_csv():

    with open('Inventory_20210421.csv', 'r', encoding="utf-8_sig") as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]

    f.close()

    return data


def user_init(pn):
    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000",
                              region_name='ap-northeast-1',
                              aws_access_key_id='fake',
                              aws_secret_access_key='fake')
    dynamodb_table = dynamodb.Table('items2')

    dynamodb_table.update_item(
        Key={
            'product_number': pn,
        },
        UpdateExpression="set younghoho_1121 =:r, tomokimi_777 =:s",
        ExpressionAttributeValues={
            ':r': Decimal(0),
            ':s': Decimal(0),
        },
        ReturnValues="UPDATED_NEW"
    )


def update(pn, author):
    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000",
                              region_name='ap-northeast-1',
                              aws_access_key_id='fake',
                              aws_secret_access_key='fake')
    dynamodb_table = dynamodb.Table('items2')

    dynamodb_table.update_item(
        Key={
            'product_number': pn,
        },
        UpdateExpression="set " + author + "=:r",
        ExpressionAttributeValues={
            ':r': Decimal(1),
        },
        ReturnValues="UPDATED_NEW"
    )


# 初回登録
if __name__ == '__main__':
    all_items = []
    users = ["younghoho_1121", "tomokimi_777"]

    for a in get_all():
        user_init(a["product_number"])
        print(a)

    for user in users:
        sc_data = get_items.get_items(user)
        for item in sc_data:
            all_items.append(item)

    for item in all_items:
        update(item["measuring"]["id"], item["user"])

    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000",
                              region_name='ap-northeast-1', aws_access_key_id='fake', aws_secret_access_key='fake')
    table = dynamodb.Table('items2')

    for obj in get_data_from_csv():
        pn = obj["物品名"][0:4]

        table.update_item(
            Key={
                'product_number': pn,
            },
            UpdateExpression="set zaiko_id =:r, item_name =:s, Category = :t, quantity = :u, maron = :x",
            ExpressionAttributeValues={
                ':r':  int(obj["在庫ID"]),
                ':s': obj["物品名"],
                ':t': obj["カテゴリ"],
                ':u': int(obj["数量"]),
                ':x': Decimal(0),
            },
            ReturnValues="UPDATED_NEW"
        )
