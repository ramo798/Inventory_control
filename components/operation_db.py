import boto3
from boto3.dynamodb.conditions import Key
import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('inventry')
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

# データベースに値を登録
def put_item(dict):

    table.put_item(
        Item={
            'model_number': dict['measuring']['id'],
            'title':dict['title'],
            'price':dict['price'],
            'kata':dict['measuring']['kata'],
            'mune':dict['measuring']['bast'],
            'take':dict['measuring']['take'],
            'sode':dict['measuring']['sode'],
            'yahuoku_last_check_date': today,
            'url':dict['url']
        }
    )
    

if __name__ == '__main__':

    testdata = {'title': '☆DONNA KARAN☆チュール付きキャミソールM',
     'price': '5,800',
     'measuring': {
         'id': 'UC781',
         'kata': ' ', 
         'take': '123', 
         'bast': '38', 
         'sode': ' '
         },
     'url': 'https://page.auctions.yahoo.co.jp/jp/auction/p763454105'
     }
     
    put_item(testdata)

    # print(testdata['title'])
    if check_existence(testdata):
        
        print(True)
