import get_items as gi
import csv
import pandas as pd

if __name__ == '__main__':
    res_list = []
    users = ["younghoho_1121", "tomokimi_777"]

    for username in users:
        items = gi.get_items(username)
        print('GET ITEM FINISH. FROM ', username)

        # for item in items:
        #     print(item)
        #     res_list.append(item)
