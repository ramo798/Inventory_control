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

def remove_blank(value):
    if value == "":
        return " "
    else:
        return value

# データベースに値を登録
def put_item(dict):

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
            'url':remove_blank(dict['url'])
        }
    )
    

if __name__ == '__main__':

    testdata = {'title': '☆DONNA KARAN☆チュール付きキャミソールM',
     'price': '5,800',
     'measuring': {
         'id': 'UC781',
         'kata': '', 
         'take': '123', 
         'bast': '38', 
         'sode': ''
         },
     'url': 'https://page.auctions.yahoo.co.jp/jp/auction/p763454105'
     }
     
    put_item(testdata)

    # print(testdata['title'])
    # if check_existence(testdata):
        
    #     print(True)

    # remove_blank(testdata)
