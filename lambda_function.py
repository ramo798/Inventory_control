import json
from components import get_items as gi
from components import operation_db as op

def lambda_handler(event, context):
    # データベースの更新
    users = ['tomokimi_777','merci_dsyl']
    for username in users:
        items = gi.get_items(username)
        print('GET ITEM FINISH. FROM ',username)

        for item in items:
            op.operation(item,username)

    # sold_out判定用のバッチ処理
    op.sold_out_checker()
    
    return 'suc'

def lambda_handler_upload_s3(event, context):
    items = op.get_all_item()
    
    return 'suc'