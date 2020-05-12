from . import operation_db as op
import datetime


today = str(datetime.date.today())

def generate():
    items = op.get_all_item()
    # print(items)

    tomokimi_777_items = []
    merci_dsyl_items = []

    for item in items:
        if item['yahuoku_username'] == 'tomokimi_777':
            tomokimi_777_items.append(item)
        elif item['yahuoku_username'] == 'merci_dsyl':
            merci_dsyl_items.append(item)

    
    fieldnames = '商品ID,タイトル,価格,肩,胸,丈,袖,ヤフオク最終確認日,url,ヤフオクsold_out'

    tomokimi_res = "" + fieldnames + "\n"
    merci_dsyl_res = "" + fieldnames + "\n"

    for item in tomokimi_777_items:
        row = ""
        write_list = [
            item['model_number'],
            item['title'],
            item['price'].replace(',', ''),
            item['kata'],
            item['mune'],
            item['take'],
            item['sode'],
            item['yahuoku_last_check_date'],
            item['item_url'],
            str(item['sold_out'])
        ]
        for tmp in write_list:
            row += tmp + ","
        tomokimi_res += row + "\n"

    for item in merci_dsyl_items:
        row = ""
        write_list = [
            item['model_number'],
            item['title'],
            item['price'].replace(',', ''),
            item['kata'],
            item['mune'],
            item['take'],
            item['sode'],
            item['yahuoku_last_check_date'],
            item['item_url'],
            str(item['sold_out'])
        ]
        for tmp in write_list:
            row += str(tmp) + ","
        merci_dsyl_res += row + "\n"


    res = {
        'tomokimi':tomokimi_res,
        'merci_dsyl':merci_dsyl_res
        }
    return res

if __name__ == '__main__':
    a = generate()
    print(a['tomokimi'])