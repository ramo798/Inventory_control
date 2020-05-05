import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('inventry')

# response = table.get_item(
#     Key={
#         'model_number': "UC78"
#     }
# )
response = table.scan()
print(response['Items'])
print(len(response['Items']))
