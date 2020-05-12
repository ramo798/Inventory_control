from components import get_items as gi
from components import operation_db as op
import datetime
import csv

today = str(datetime.date.today())

if __name__ == '__main__':
    items = op.get_all_item()
    # print(items)

    tomokimi_777_items = []
    merci_dsyl_items = []

    for item in items:
        if item['yahuoku_username'] == 'tomokimi_777':
            tomokimi_777_items.append(item)
        elif item['yahuoku_username'] == 'merci_dsyl':
            merci_dsyl_items.append(item)
    
    with open('csv/tomokimi_777.csv', 'w', newline="") as f:
        fieldnames = ['商品ID', 'タイトル', '価格', '肩','胸','丈', '袖','ヤフオク最終確認日','url','ヤフオクsold_out']
        writer = csv.writer(f)
        writer.writerow(fieldnames)
        for item in tomokimi_777_items:
            write_list = [
                item['model_number'],
                item['title'],
                item['price'],
                item['kata'],
                item['mune'],
                item['take'],
                item['sode'],
                item['yahuoku_last_check_date'],
                item['item_url'],
                item['sold_out']
            ]
            writer.writerow(write_list)
    
    with open('csv/merci_dsyl.csv', 'w', newline="") as f:
        fieldnames = ['商品ID', 'タイトル', '価格', '肩','胸','丈', '袖','ヤフオク最終確認日','url','ヤフオクsold_out']
        writer = csv.writer(f)
        writer.writerow(fieldnames)
        for item in merci_dsyl_items:
            write_list = [
                item['model_number'],
                item['title'],
                item['price'],
                item['kata'],
                item['mune'],
                item['take'],
                item['sode'],
                item['yahuoku_last_check_date'],
                item['item_url'],
                item['sold_out']
            ]
            writer.writerow(write_list)