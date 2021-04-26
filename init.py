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


if __name__ == '__main__':
    create_table()
