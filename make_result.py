import csv
import boto3


def get_all():
    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000",
                              region_name='ap-northeast-1',
                              aws_access_key_id='fake',
                              aws_secret_access_key='fake')
    dynamodb_table = dynamodb.Table('items2')

    response = dynamodb_table.scan()

    # print(len(response["Items"]))
    # print(response["Items"])
    # for a in response["Items"]:
    # print(a["product_number"])
    # print(response["ResponseMetadata"])

    return response["Items"]


if __name__ == '__main__':
    items = get_all()
    for a in items:
        print(a)
    # print(items[0]["product_number"])
    with open('test.csv', 'a', encoding="utf_8", newline="") as f:
        writer = csv.writer(f)
        #     # "在庫ID", "物品名", "カテゴリ", "保管場所", "状態", "数量", "単位", "QRコード・バーコードの値", "備考", "データ作成日", "データ更新日", "品番", "younghoho", "tomokimi", "maron"
        #     colum = ["在庫ID", "物品名", "カテゴリ", "保管場所", "状態", "数量", "単位", "QRコード・バーコードの値",
        #              "備考", "データ作成日", "データ更新日", "品番", "younghoho", "tomokimi", "maron"]
        colum = ["在庫ID", "品番", "younghoho", "tomokimi", "maron"]
        writer.writerow(colum)
        for item in items:
            try:
                zaiko_id = item["zaiko_id"]
                # quantity = item["quantity"]
                product_number = item["product_number"]
                younghoho_1121 = item["younghoho_1121"]
                tomokimi_777 = item["tomokimi_777"]
                maron = 0
                writer.writerow(
                    (zaiko_id, product_number, younghoho_1121, tomokimi_777, maron))
            except KeyError:
                # print(1)
                pass
