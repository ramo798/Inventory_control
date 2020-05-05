import boto3
from boto3.dynamodb.conditions import Key
import datetime

def update_table(syouzai):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('inventry')
    today = str(datetime.date.today())
    
    response = table.get_item(
        Key={
            'model_number': syousai['measuring']['id']
        }
    )

    if 'Item' in response:
        # 在庫表に存在するとき
        update = table.update_item(
            Key={
                'model_number':syousai['measuring']['id']
            },
            UpdateExpression="set yahuoku_last_check_date = :yahuoku_last_check_date, price=:price",
            ExpressionAttributeValues={
                ':yahuoku_last_check_date': today,
                ':price': syousai['price']
            })
    else:
        table.put_item(
            Item={
                'model_number': syousai['measuring']['id'],
                'title':syousai['title'],
                'price':syousai['price'],
                'kata':syousai['measuring']['kata'],
                'mune':syousai['measuring']['bast'],
                'take':syousai['measuring']['take'],
                'sode':syousai['measuring']['sode'],
                'yahuoku_last_check_date': today,
            }
        )