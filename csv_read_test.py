import csv

def duplication_check(filename,item_id):
    with open(filename, 'r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == item_id:
                return True
    
    return False



print(duplication_check('tomokimi.csv',"NE3"))