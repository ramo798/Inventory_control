import boto3
from boto3.dynamodb.conditions import Key
import csv

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('inventry')



with open('tomokimi_777.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        table.put_item(
            Item={
                'model_number': row[0],
                'title':row[1],
                'price':row[2],
                'kata':row[3],
                'mune':row[4],
                'take':row[5],
                'sode':row[6],
                'yahuoku_last_check_date': row[7],
            }
        )
        