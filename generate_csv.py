from components import get_items as gi
import datetime
import csv

today = str(datetime.date.today())

if __name__ == '__main__':
    username = "merci_dsyl"
    items = gi.get_items(username)

    file_dir = "csv/" + username + ".csv"

    with open(file_dir, 'a', newline="") as f:
        fieldnames = ['商品ID', 'タイトル', '価格', '肩','胸','丈', '袖','ヤフオク最終更新日','url']
        writer = csv.writer(f)
        writer.writerow(fieldnames)
        for item in items:
            write_list = [
                item['measuring']['id'],
                item['title'],
                item['price'],
                item['measuring']['kata'],
                item['measuring']['bast'],
                item['measuring']['take'],
                item['measuring']['sode'],
                today,
                item['url']
            ]
            writer.writerow(write_list)

    
         
    

