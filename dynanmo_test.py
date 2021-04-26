import boto3


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


def check_tables():
    dynamodb = boto3.client('dynamodb', endpoint_url="http://localhost:8000",
                            region_name='ap-northeast-1',
                            aws_access_key_id='fake',
                            aws_secret_access_key='fake')

    tables = dynamodb.list_tables()

    print('Tables List:', tables['TableNames'])


def put_item():
    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000",
                              region_name='ap-northeast-1',
                              aws_access_key_id='fake',
                              aws_secret_access_key='fake')
    table = dynamodb.Table('items')
    table.put_item(
        Item={
            'zaiko_id': 32794783,
            'item_name': 'HT07ツィリー　ケリー・アン・ペルル　ROSE/VERT/NORE',
            'Category': "ツィリー",
            'quantity': 1,
            'product_number': "NT07",
            'younghoho': 0,
            'tomokimi': 0,
            'maron': 0,
        }
    )
    item = table.get_item(Key={'zaiko_id': 32794783})
    print(item['Item'])


def scan():
    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000",
                              region_name='ap-northeast-1',
                              aws_access_key_id='fake',
                              aws_secret_access_key='fake')
    dynamodb_table = dynamodb.Table('items2')

    response = dynamodb_table.scan()

    # print(response["Items"])
    for a in response["Items"]:
        print(a)
    print(response["ResponseMetadata"])


def get_item():
    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000",
                              region_name='ap-northeast-1',
                              aws_access_key_id='fake',
                              aws_secret_access_key='fake')
    dynamodb_table = dynamodb.Table('items2')

    response = dynamodb_table.get_item(Key={'product_number': "HW113"})

    if "Item" in response:
        print(1)
    else:
        print(2)


if __name__ == '__main__':
    create_table()
