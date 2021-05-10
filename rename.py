import csv

with open("Inventory_20210510.csv", "r", encoding="utf-8") as f:
    with open("rename_result.csv", "w", encoding="utf-8", newline="") as fw:
        writer2 = csv.writer(fw)

        for row in csv.reader(f):
            title = "[" + row[1][0:4] + "]" + row[1][4:]

            print(title)

            writer2.writerow([row[0], title, row[1][0:4]])
            # writer2.writerow([1, 2])
            # print(row[1][0:4])
