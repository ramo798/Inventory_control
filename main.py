from components import get_items as gi
from components import operation_db as op

if __name__ == '__main__':

    items = gi.get_items("merci_dsyl")

    for item in items:
        op.operation(item)
        
    
    
