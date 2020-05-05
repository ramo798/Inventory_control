import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('inventry')

# response = table.get_item(
#     Key={
#         'model_number': "UC78"
#     }
# )
# print(response['Item'])

test_data = ['UC65', '★CHRISTIAN LACROIX★半袖ニットサイズS', '11,800', '33', '36', '54', '19', '2020-05-04']



response = table.get_item(
    Key={
        'model_number': test_data[0]
    }
)

if 'Item' in response:
    print("true")
else:
    print("erro")



