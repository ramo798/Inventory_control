import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('inventry-1')

table.put_item(
    Item={
        'model_number': "UC78",
        'date': "2020-05-04",
        'price': "19,800",
    }
)