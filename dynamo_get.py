import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('inventry-1')

response = table.get_item(
    Key={
        'model_number': "UC78"
    }
)
print(response['Item'])