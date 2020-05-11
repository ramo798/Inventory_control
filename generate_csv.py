from components import get_items as gi
from components import operation_db as op
import datetime
import csv

today = str(datetime.date.today())

if __name__ == '__main__':
    items = op.get_all_item()
    # print(items)

    for item in items:
        if item['yahuoku_username'] == 'tomokimi_777':
            with open('csv/tomokimi_777.csv', 'a', newline="") as f:
                fieldnames = ['商品ID', 'タイトル', '価格', '肩','胸','丈', '袖','ヤフオク最終確認日','url','ヤフオクsold_out']
                writer = csv.writer(f)
                writer.writerow(fieldnames)
                for item in items:
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
        elif item['yahuoku_username'] == 'merci_dsyl':
            with open('csv/merci_dsyl.csv', 'a', newline="") as f:
                fieldnames = ['商品ID', 'タイトル', '価格', '肩','胸','丈', '袖','ヤフオク最終確認日','url','ヤフオクsold_out']
                writer = csv.writer(f)
                writer.writerow(fieldnames)
                for item in items:
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










    # file_dir = "csv/" + username + ".csv"



    # with open(file_dir, 'a', newline="") as f:
    #     fieldnames = ['商品ID', 'タイトル', '価格', '肩','胸','丈', '袖','ヤフオク最終更新日','url','ヤフオクsold_out']
    #     writer = csv.writer(f)
    #     writer.writerow(fieldnames)
    #     for item in items:
    #         write_list = [
    #             item['measuring']['id'],
    #             item['title'],
    #             item['price'],
    #             item['measuring']['kata'],
    #             item['measuring']['bast'],
    #             item['measuring']['take'],
    #             item['measuring']['sode'],
    #             today,
    #             item['url'],
    #             item['sold_out']
    #         ]
    #         writer.writerow(write_list)

    
         
    

