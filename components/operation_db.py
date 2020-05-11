import boto3
from boto3.dynamodb.conditions import Key
import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('inventry')
today = str(datetime.date.today())

# def check_existence(dict):



if __name__ == '__main__':

    testdata = {'title': '☆DONNA KARAN☆チュール付きキャミソールM', 'price': '5,800', 'measuring': {'id': 'DUC62', 'kata': '', 'take': '123', 'bast': '38', 'sode': ''}, 'url': 'https://page.auctions.yahoo.co.jp/jp/auction/p763454105'}
    print(testdata['title'])
