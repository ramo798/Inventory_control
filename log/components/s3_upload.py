import boto3

s3 = boto3.resource('s3')

bucket = s3.Bucket('inventory1237')

def upload_csv(items):
    objkey = 'tomokimi_777.csv'
    putobj = bucket.Object(objkey)
    putobj.put(Body=items['tomokimi'])

    
    objkey = 'merci_dsyl.csv'
    putobj = bucket.Object(objkey)
    putobj.put(Body=items['merci_dsyl'])