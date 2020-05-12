import boto3

s3 = boto3.resource('s3')

bucket = s3.Bucket('inventory1237')



with open('csv/tomokimi_777.csv', 'r', newline="") as f:
    objkey = 'tomokimi_777.csv'
    putobj = bucket.Object(objkey)
    putobj.put(Body=f.read())

with open('csv/merci_dsyl.csv', 'r', newline="") as f:
    objkey = 'merci_dsyl.csv'
    putobj = bucket.Object(objkey)
    putobj.put(Body=f.read())
