import boto3
import csv
import get_items
from decimal import Decimal
from pprint import pprint


def create_table():
    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000",
                              region_name='ap-northeast-1',
                              aws_access_key_id='fake',
                              aws_secret_access_key='fake')

    table = dynamodb.create_table(
        TableName='items2',
        KeySchema=[
            {
                'AttributeName': 'product_number',
                'KeyType': 'HASH'
            },

        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'product_number',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }
    )

    print('Table status:', table.table_status)


def first_register():
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


def get_data_from_csv():

    with open('Inventory_20210421.csv', 'r', encoding="utf-8_sig") as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]

    f.close()

    return data


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


def update(pn, author):
    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000",
                              region_name='ap-northeast-1',
                              aws_access_key_id='fake',
                              aws_secret_access_key='fake')
    dynamodb_table = dynamodb.Table('items2')
    try:
        response = dynamodb_table.get_item(Key={'product_number': pn})
    except:
        pass
    else:
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


if __name__ == '__main__':
    try:
        create_table()
        # first_register()
    except:
        pass

    # print(update("HT12", "younghoho"))

    # db_items = get_all()
    # print(db_items[1])

    all_items = []
    users = ["younghoho_1121", "tomokimi_777"]
    for user in users:
        sc_data = get_items.get_items(user)
        for item in sc_data:
            all_items.append(item)

    for item in all_items:
        update(item["measuring"]["id"], item["user"])

    db_items = get_all()
    for db_item in db_items:
        # print(db_item)
        # print("-----")
        # print(db_item["product_number"],
        #   db_item["younghoho_1121"], db_item["tomokimi_777"])
        # print(db_item["product_number"])

        # for item in sc_data:
        #     print(item["measuring"]["id"], item["user"])
