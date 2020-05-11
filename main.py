from components import get_items as gi
from components import operation_db as op

if __name__ == '__main__':
    users = ['tomokimi_777','merci_dsyl']

    for username in users:
        items = gi.get_items(username)
        print('GET ITEM FINISH. FROM ',username)

        for item in items:
            op.operation(item,username)
        

    
    
    
