import boto3
from boto3.dynamodb.conditions import Key
import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('inventry_control')
today = str(datetime.date.today())

# テーブルに存在しているデータかの判定
def check_existence(dict):
    model_number = dict['measuring']['id']
    # print(model_number)

    response = table.get_item(
    Key={
        'model_number': model_number
    }
    )

    if 'Item' in response:
        # print(response['Item'])
        return True
    else:
        return False

def remove_blank(value):
    if value == "":
        return " "
    else:
        return value

# データベースに値を登録
def put_item(dict,username):
    
    table.put_item(
        Item={
            'model_number': remove_blank(dict['measuring']['id']),
            'title':remove_blank(dict['title']),
            'price':remove_blank(dict['price']),
            'kata':remove_blank(dict['measuring']['kata']),
            'mune':remove_blank(dict['measuring']['bast']),
            'take':remove_blank(dict['measuring']['take']),
            'sode':remove_blank(dict['measuring']['sode']),
            'yahuoku_last_check_date': today,
            'item_url':remove_blank(dict['url']),
            'yahuoku_username':username
        }
    )

def update_item(dict,username):
    model_number = dict['measuring']['id']

    response = table.update_item(
    Key={
        'model_number': model_number
    },
    UpdateExpression="set title = :title, price = :price, kata = :kata, mune = :mune,take = :take, sode = :sode, yahuoku_last_check_date = :today, item_url = :url, yahuoku_username = :username",
    ExpressionAttributeValues={
        ':title':remove_blank(dict['title']),
        ':price':remove_blank(dict['price']),
        ':kata':remove_blank(dict['measuring']['kata']),
        ':mune':remove_blank(dict['measuring']['bast']),
        ':take':remove_blank(dict['measuring']['take']),
        ':sode':remove_blank(dict['measuring']['sode']),
        ':today': today,
        ':url':remove_blank(dict['url']),
        ':username':username
    },
    ReturnValues="UPDATED_NEW"
    )

def check_sold(model_number):
    table.update_item(
    Key={
        'model_number': model_number
    },
    UpdateExpression="set sold_out = :sold",
    ExpressionAttributeValues={
        ':sold':True
    },
    ReturnValues="UPDATED_NEW"
    )

def check_not_sold(model_number):
    table.update_item(
    Key={
        'model_number': model_number
    },
    UpdateExpression="set sold_out = :sold",
    ExpressionAttributeValues={
        ':sold':False
    },
    ReturnValues="UPDATED_NEW"
    )


def sold_out_checker():
    response = table.scan()
    items = response['Items']
    for item in items:
        last_date = datetime.datetime.strptime(item['yahuoku_last_check_date'], '%Y-%m-%d')
        now_date = datetime.datetime.strptime(today, '%Y-%m-%d')

        if last_date < now_date:
            check_sold(item['model_number'])
        else:
            check_not_sold(item['model_number'])


def get_all_item():
    response = table.scan()
    items = response['Items']
    return items

def operation(dict,username):
    if check_existence(dict):
        update_item(dict,username)
        print("update",dict['measuring']['id'])
    else:
        put_item(dict,username)
        print("put",dict['measuring']['id'])

    

if __name__ == '__main__':
    testdata = {
        'title': '☆DONNA KARAN☆チュール付きキャミソールM',
        'price': '5,8000',
        'measuring': {
            'id': 'UC7811',
            'kata': '123', 
            'take': '123', 
            'bast': '381', 
            'sode': ''
        },
        'url': 'https://page.auctions.yahoo.co.jp/jp/auction/p763454105'
     }
    operation(testdata)