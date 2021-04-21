import csv
with open('Inventory_20210421.csv', 'r', encoding="utf-8_sig") as f:
    reader = csv.DictReader(f)
    data = [row for row in reader]

    print(data[0]["物品名"])
    print(data[0])
